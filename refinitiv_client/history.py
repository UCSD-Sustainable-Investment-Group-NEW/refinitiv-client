"""
Pull annual time series data for one or more companies.

Usage:
    from refinitiv_client import history

    history.get_esg(["COST.O", "NVDA.O"], start="2018", end="2023")
    history.get_financials("COST.O", start="2018", end="2023")
    history.get_combined(["COST.O", "NVDA.O"], start="2018", end="2023")
"""

import pandas as pd
import lseg.data as ld
from typing import Union

from refinitiv_client.fields import ESG_CODES, ESG_SCORES, FINANCIAL_CODES, INCOME_STATEMENT, RATIOS


def get_esg(
    universe: Union[str, list[str]],
    start: str,
    end: str,
) -> pd.DataFrame:
    """Annual ESG pillar scores over time."""
    return ld.get_history(universe=universe, fields=ESG_SCORES, start=start, end=end, interval="1Y")


def get_financials(
    universe: Union[str, list[str]],
    start: str,
    end: str,
) -> pd.DataFrame:
    """Annual income statement and ratio metrics over time."""
    return ld.get_history(universe=universe, fields=INCOME_STATEMENT + RATIOS, start=start, end=end, interval="1Y")


def get_combined(
    universe: Union[str, list[str]],
    start: str,
    end: str,
) -> pd.DataFrame:
    """ESG scores and financial metrics together — the main input for correlation work."""
    return ld.get_history(universe=universe, fields=ESG_CODES + FINANCIAL_CODES, start=start, end=end, interval="1Y")