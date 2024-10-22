RENAME_DICT = {
    'Property Name': 'PROPERTY_NM',
    'Activity Status': 'ACTIVITY_STATUS',
    'Mine Type 1': 'MINE_TYPE',
    'Initial Capital Cost\r\n($M)': 'INITIAL_COST',
    'NPV Discount % - Base Case\r\n(%)': 'NPV_DISCOUNT', #
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
        "PRECIOUS_TONNAGE",
        "COPPER_TONNAGE",
        "ECONOMIC_TONNAGE",
        "GOLD_TONNAGE",
        "SILVER_TONNAGE",
        'INITIAL_COST_PER_TONNE',
        "LOG_10_GOLD_DENSITY",
        "LOG_10_SILVER_DENSITY",
        "LOG_10_PRECIOUS_ORE_DENSITY",
        "LOG_10_COPPER_GRADE",
        "LOG_10_INITIAL_COST",
        "LOG_10_ORE_TONNAGE",
        "LOG_10_PRECIOUS_TONNAGE",
        "LOG_10_COPPER_TONNAGE",
        "LOG_10_ECONOMIC_TONNAGE",
        "LOG_10_GOLD_TONNAGE",
        "LOG_10_SILVER_TONNAGE",
        'LOG_10_INITIAL_COST_PER_TONNE'
        #Capacidade de processamento
        #"PRICE_PER_TONNE_MAIN_ORE",
    ]

TO_LOG10 = [
    "GOLD_DENSITY",
    "SILVER_DENSITY",
    "PRECIOUS_ORE_DENSITY",
    "COPPER_GRADE",
    "INITIAL_COST",
    "ORE_TONNAGE",
    "PRECIOUS_TONNAGE",
    "COPPER_TONNAGE",
    "ECONOMIC_TONNAGE",
    "GOLD_TONNAGE",
    "SILVER_TONNAGE",
    'INITIAL_COST_PER_TONNE',

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

NUM_SELECTED = ['GOLD_DENSITY',
 'SILVER_DENSITY',
 'PRECIOUS_ORE_DENSITY',
 'COPPER_GRADE',
 'INITIAL_COST',
 'ORE_TONNAGE',
 'COPPER_TONNAGE',
 'GOLD_TONNAGE',
 'LOG_10_PRECIOUS_ORE_DENSITY',
 'INITIAL_COST_PER_TONNE',
 'LOG_10_SILVER_DENSITY',
 'LOG_10_GOLD_DENSITY',
 'LOG_10_COPPER_GRADE',
 'LOG_10_COPPER_TONNAGE',
 'LOG_10_ORE_TONNAGE',
 'LOG_10_INITIAL_COST',
 'LOG_10_INITIAL_COST_PER_TONNE']

CAT_SELECTED = ['GLOBAL_REGION_2', 'MINE_TYPE_1', 'GLOBAL_REGION_0']

SELECTED_FEATURES = NUM_SELECTED + CAT_SELECTED