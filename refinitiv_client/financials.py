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


def get_income_statement(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """Revenue, gross profit, EBITDA, EBIT, net income, EPS."""
    return ld.get_data(universe=universe, fields=INCOME_STATEMENT, parameters=_params(year))


def get_balance_sheet(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """Total assets, liabilities, equity, and debt."""
    return ld.get_data(universe=universe, fields=BALANCE_SHEET, parameters=_params(year))


def get_ratios(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """ROE, ROA, net margin, debt/equity, P/B, P/E."""
    return ld.get_data(universe=universe, fields=RATIOS, parameters=_params(year))