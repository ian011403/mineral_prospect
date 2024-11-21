"""Constants for copper data processing"""

RENAME_DICT = {
    'Property Name': 'PROPERTY_NM',
    'Activity Status': 'ACTIVITY_STATUS',
    'Mine Type 1': 'MINE_TYPE',
    'Initial Capital Cost\r\n($M)': 'INITIAL_COST',
    'NPV Discount % - Base Case\r\n(%)': 'NPV_DISCOUNT', 
    'Post-Tax IRR % - Base Case\r\n(%)': 'TIR',
    'Study Price per tonne - Base Case\r\n($/tonne)': 'PRICE_PER_TONNE_MAIN_ORE',
    'Geologic Ore Body Type': 'GEOLOGIC_ORE_BODY_TYPE',
    'Country / Region Name': 'PLACE_NM',
    'Reserves & Resources: Ore Tonnage\r\n(tonnes)': 'ORE_TONNAGE',
    'Grade, Reserves & Resources Copper\n(%)': 'COPPER_GRADE',
    'Grade, Reserves & Resources Lead\n(%)': 'LEAD_GRADE',
    'Grade, Reserves & Resources Zinc\n(%)': 'ZINC_GRADE',
    'Grade, Reserves & Resources Gold\n(g/tonne)': 'GOLD_DENSITY',
    'Grade, Reserves & Resources Silver\n(g/tonne)': 'SILVER_DENSITY',
    'Global Region': 'GLOBAL_REGION',
    }

DROP_COLUMNS = ['PROPERTY_NM', 'ACTIVITY_STATUS', 'PLACE_NM', 'NPV_DISCOUNT']

NUM_FEATURES = [
        "GOLD_DENSITY",
        "SILVER_DENSITY",
        "PRECIOUS_ORE_DENSITY",
        "COPPER_GRADE",
        "INITIAL_COST",
        "ORE_TONNAGE",
        "PRECIOUS_GRAMS",
        "COPPER_TONNAGE",
        "ECONOMIC_AMOUNT",
        "GOLD_GRAMS",
        "SILVER_GRAMS",
        'INITIAL_COST_PER_AMOUNT',
        "LOG_10_GOLD_DENSITY",
        "LOG_10_SILVER_DENSITY",
        "LOG_10_PRECIOUS_ORE_DENSITY",
        "LOG_10_COPPER_GRADE",
        "LOG_10_INITIAL_COST",
        "LOG_10_ORE_TONNAGE",
        "LOG_10_PRECIOUS_GRAMS",
        "LOG_10_COPPER_TONNAGE",
        "LOG_10_ECONOMIC_AMOUNT",
        "LOG_10_GOLD_GRAMS",
        "LOG_10_SILVER_GRAMS",
        'LOG_10_INITIAL_COST_PER_AMOUNT'
    ]

TO_LOG10 = [
    "GOLD_DENSITY",
    "SILVER_DENSITY",
    "PRECIOUS_ORE_DENSITY",
    "COPPER_GRADE",
    "INITIAL_COST",
    "ORE_TONNAGE",
    "PRECIOUS_GRAMS",
    "COPPER_TONNAGE",
    "ECONOMIC_AMOUNT",
    "GOLD_GRAMS",
    "SILVER_GRAMS",
    'INITIAL_COST_PER_AMOUNT',

]

CAT_FEATURES = [
    "GEOLOGIC_ORE_BODY_TYPE",
    "GLOBAL_REGION",
    "MINE_TYPE"
]

FEATURES = NUM_FEATURES + CAT_FEATURES

FILL_COLS = ['COPPER_GRADE', 'LEAD_GRADE', 'ZINC_GRADE',
       'GOLD_DENSITY', 'SILVER_DENSITY']

LOG_INF_REPL = -100

UPPER_LIMIT_TIR = 125

MIN_TIR = 15