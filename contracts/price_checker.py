# price_checker.py
# GenLayer Intelligent Contract – Live Price Validator via Web + LLM
# Testnet: Bradbury
#
# Fetches live asset prices from public sources and uses LLM consensus
# to validate and normalize the data — no centralized oracle needed.

from genlayer import *


@gl.contract
class PriceCheckerContract:
    """
    Decentralized price checker using LLM consensus instead of oracles.
    Validators independently fetch and agree on prices via multi-LLM voting.
    """

    owner: str
    last_price: str
    last_asset: str
    check_count: u256

    def __init__(self) -> None:
        self.owner = contract_runner.from_account
        self.last_price = ""
        self.last_asset = ""
        self.check_count = 0

    @gl.public.view
    def get_last_check(self) -> dict:
        return {
            "asset": self.last_asset,
            "price": self.last_price,
            "total_checks": int(self.check_count),
        }

    @gl.public.write
    def fetch_price(self, asset: str, source_url: str) -> str:
        """
        Fetches the current price of an asset from a public URL using LLM extraction.

        Args:
            asset: Asset name/ticker (e.g. "BTC", "ETH", "GEN")
            source_url: Public URL containing the price information

        Returns:
            Extracted price as string (e.g. "42,350 USD")
        """
        web_content = contract_runner.get_webpage(source_url, mode="text")

        prompt = f"""
Extract the current price of {asset} from the following web content.

Content:
---
{web_content[:2000]}
---

Return ONLY the price with currency (e.g. "42,350 USD" or "0.85 EUR").
If the price cannot be found, return: "PRICE_NOT_FOUND"
"""
        price = contract_runner.call_llm(prompt).strip()

        self.last_asset = asset
        self.last_price = price
        self.check_count += 1

        return price

    @gl.public.write
    def validate_price_range(
        self, asset: str, source_url: str, min_price: str, max_price: str
    ) -> bool:
        """
        Checks whether an asset's price is within an expected range.
        Useful for automated contract conditions (e.g. DeFi triggers).

        Args:
            asset: Asset to check
            source_url: URL with current price data
            min_price: Minimum acceptable price (as string, e.g. "30000")
            max_price: Maximum acceptable price (as string, e.g. "60000")

        Returns:
            True if price is within range, False otherwise
        """
        web_content = contract_runner.get_webpage(source_url, mode="text")

        prompt = f"""
You are checking if the current price of {asset} is within a valid range.

Web content:
---
{web_content[:2000]}
---

Minimum acceptable price: {min_price}
Maximum acceptable price: {max_price}

Extract the current price of {asset} from the content.
Then determine if it falls within the range [{min_price}, {max_price}].

Respond with exactly one word: YES or NO
"""
        result = contract_runner.call_llm(prompt).strip().upper()
        self.check_count += 1
        return result == "YES"

    @gl.public.write
    def compare_prices(self, asset: str, url_1: str, url_2: str) -> str:
        """
        Compares prices from two different sources and returns consensus analysis.
        Demonstrates GenLayer's ability to cross-validate real-world data.

        Args:
            asset: Asset to compare
            url_1: First source URL
            url_2: Second source URL

        Returns:
            LLM consensus analysis of both prices
        """
        content_1 = contract_runner.get_webpage(url_1, mode="text")
        content_2 = contract_runner.get_webpage(url_2, mode="text")

        prompt = f"""
Compare the price of {asset} from two different sources:

Source 1 ({url_1}):
---
{content_1[:1500]}
---

Source 2 ({url_2}):
---
{content_2[:1500]}
---

Extract the price from each source and provide a brief comparison.
Format: "Source 1: [price] | Source 2: [price] | Difference: [diff] | Assessment: [note]"
"""
        self.check_count += 1
        return contract_runner.call_llm(prompt)
