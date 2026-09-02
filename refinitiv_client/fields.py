# fields.py

# Maps TR. code -> display name LSEG returns as the column header
# Discover display names by printing df.columns after a pull

ESG_FIELDS = {
    "TR.TRESGScore":              "ESG Score",
    "TR.EnvironmentPillarScore":  "Environmental Pillar Score",
    "TR.SocialPillarScore":       "Social Pillar Score",
    "TR.GovernancePillarScore":   "Governance Pillar Score",
    "TR.EnergyUseTotal":          "Energy Use Total",
    "TR.CO2EmissionTotal":        "CO2 Equivalent Emissions Total",
    "TR.WaterWithdrawalTotal":    "Water Withdrawal Total",
    "TR.RenewableEnergyUseRatio": "Renewable Energy Use Ratio",
    "TR.WomenEmployees":          "Women Employees",
    "TR.EmployeeSatisfaction":    "Employee Satisfaction",
    "TR.TrainingHoursAverage":    "Training Hours Average",
    "TR.WorkplaceAccidentRate":   "Workplace Accident Rate",
    "TR.BoardFemaleMembers":      "Board Female Members",
    "TR.CSRSustainabilityCommittee": "CSR Sustainability Committee",
    "TR.BoardIndependentMembers": "Board Independent Members",
}

FINANCIAL_FIELDS = {
    "TR.Revenue":           "Revenue",
    "TR.GrossProfit":       "Gross Profit",
    "TR.EBITDA":            "EBITDA",
    "TR.EBIT":              "EBIT",
    "TR.NetIncome":         "Net Income Incl Extra Before Distributions",
    "TR.EPS":               "EPS",
    "TR.TotalAssets":       "Total Assets",
    "TR.TotalLiabilities":  "Total Liabilities",
    "TR.TotalEquity":       "Total Equity",
    "TR.TotalDebt":         "Total Debt",
    "TR.ROEActValue":       "Return On Equity - Actual",
    "TR.ROAActValue":       "Return On Assets - Actual",
    "TR.NetProfitMargin":   "Net Profit Margin, (%)",
    "TR.TotalDebtToEquity": "Total Debt To Equity",
    "TR.PriceToBVPerShare": "Price To Book Value Per Share (Daily Time Series Ratio)",
    "TR.PriceToEarnings":   "Price To Earnings",
}

# Derived lists used by the library functions
ESG_CODES        = list(ESG_FIELDS.keys())
FINANCIAL_CODES  = list(FINANCIAL_FIELDS.keys())

# Display name sets used by the UI for column categorisation
ESG_DISPLAY_NAMES       = set(ESG_FIELDS.values())
FINANCIAL_DISPLAY_NAMES = set(FINANCIAL_FIELDS.values())