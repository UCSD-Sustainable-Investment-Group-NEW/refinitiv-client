"""
Pull financial statement data for one or more companies (single year snapshot).

Usage:
    from refinitiv_client import financials

    financials.get_income_statement(["COST.O", "NVDA.O"], year="2023")
    financials.get_ratios(["COST.O", "NVDA.O"], year="2023")
"""

import pandas as pd
import lseg.data as ld
from typing import Union

from refinitiv_client.fields import FINANCIAL_CODES


def _params(year: str | None) -> dict:
    return {"SDate": f"{year}-12-31", "Period": "FY0"} if year else {}


def get_financials(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """All financial metrics — income statement, balance sheet, and ratios."""
    return ld.get_data(universe=universe, fields=FINANCIAL_CODES, parameters=_params(year))