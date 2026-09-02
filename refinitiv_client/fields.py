# -----------------------------------------------------------------------
# All TR. field codes live here.
# Add or remove fields in this file — nothing else needs to change.
# Use the Data Item Browser (DIB) in Workspace to find codes.
# -----------------------------------------------------------------------

ESG_SCORES = [
    "TR.TRESGScore",                # Overall ESG score
    "TR.EnvironmentPillarScore",    # Environment pillar
    "TR.SocialPillarScore",         # Social pillar
    "TR.GovernancePillarScore",     # Governance pillar
]

ESG_ENVIRONMENT = [
    "TR.EnergyUseTotal",
    "TR.CO2EmissionTotal",
    "TR.WaterWithdrawalTotal",
    "TR.RenewableEnergyUseRatio",
]

ESG_SOCIAL = [
    "TR.WomenEmployees",
    "TR.EmployeeSatisfaction",
    "TR.TrainingHoursAverage",
    "TR.WorkplaceAccidentRate",
]

ESG_GOVERNANCE = [
    "TR.BoardFemaleMembers",
    "TR.CSRSustainabilityCommittee",
    "TR.BoardIndependentMembers",
]

INCOME_STATEMENT = [
    "TR.Revenue",
    "TR.GrossProfit",
    "TR.EBITDA",
    "TR.EBIT",
    "TR.NetIncome",
    "TR.EPS",
]

BALANCE_SHEET = [
    "TR.TotalAssets",
    "TR.TotalLiabilities",
    "TR.TotalEquity",
    "TR.TotalDebt",
]

RATIOS = [
    "TR.ROEActValue",
    "TR.ROAActValue",
    "TR.NetProfitMargin",
    "TR.TotalDebtToEquity",
    "TR.PriceToBVPerShare",
    "TR.PriceToEarnings",
]