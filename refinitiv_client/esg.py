"""
Pull ESG data for one or more companies.

Usage:
    from refinitiv_client import esg

    esg.get_scores(["COST.O", "NVDA.O"], year="2023")
    esg.get_environment(["COST.O", "NVDA.O"], year="2023")
"""

import pandas as pd
import lseg.data as ld
from typing import Union

from refinitiv_client.fields import (
    ESG_SCORES,
    ESG_ENVIRONMENT,
    ESG_SOCIAL,
    ESG_GOVERNANCE,
)


def _params(year: str | None) -> dict:
    return {"SDate": f"{year}-12-31"} if year else {}


def get_scores(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """Overall ESG score plus the three pillar scores."""
    return ld.get_data(universe=universe, fields=ESG_SCORES, parameters=_params(year))


def get_environment(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """Environmental metrics: energy, emissions, water, renewables."""
    return ld.get_data(universe=universe, fields=ESG_ENVIRONMENT, parameters=_params(year))


def get_social(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """Social metrics: workforce diversity, safety, training."""
    return ld.get_data(universe=universe, fields=ESG_SOCIAL, parameters=_params(year))


def get_governance(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """Governance metrics: board composition, independence, committees."""
    return ld.get_data(universe=universe, fields=ESG_GOVERNANCE, parameters=_params(year))


def get_full_measures(
    universe: Union[str, list[str]],
    year: str | None = None,
) -> pd.DataFrame:
    """
    All ~400 raw ESG data points. Useful for discovering which measures
    are populated for your universe. Inspect df.columns to see everything available.
    """
    return ld.get_data(universe=universe, fields=["TR.ESGMeasures"], parameters=_params(year))