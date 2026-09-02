"""
refinitiv_client/explore.py

Utility for discovering available fields for a company.
Not used in production — run this when building out fields.py.

Usage:
    from refinitiv_client import explore
    explore.esg_fields("COST.O")
"""

import lseg.data as ld


def esg_fields(ticker: str) -> list[str]:
    """Prints all ESG fields that have data for a company."""
    # Request all known ESG fields at once
    from refinitiv_client.fields import ESG_CODES
    df = ld.get_data(universe=[ticker], fields=ESG_CODES)
    # Only return columns that have at least one non-null value
    populated = [col for col in df.columns if df[col].notna().any()]
    for f in populated:
        print(f)
    return populated

def financial_fields(ticker: str) -> list[str]:
    """Prints and returns all available financial field names for a company."""
    df = ld.get_data(universe=[ticker], fields=["TR.Financials"])
    fields = df.columns.tolist()
    for f in fields:
        print(f)
    return fields


if __name__ == "__main__":
    import sys
    from refinitiv_client.session import open_session, close_session

    ticker = sys.argv[1] if len(sys.argv) > 1 else "COST.O"
    mode = sys.argv[2] if len(sys.argv) > 2 else "esg"

    open_session()
    if mode == "esg":
        esg_fields(ticker)
    elif mode == "financial":
        financial_fields(ticker)
    close_session()