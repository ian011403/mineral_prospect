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

CAT_FEATURES = [
    "GEOLOGIC_ORE_BODY_TYPE",
    "GLOBAL_REGION",
    "MINE_TYPE"
]

FEATURES = NUM_FEATURES + CAT_FEATURES

NUM_SELECTED = ['COPPER_GRADE', 'GOLD_DENSITY',
       'LOG_10_COPPER_GRADE', 'INITIAL_COST_PER_AMOUNT', 'INITIAL_COST',
       'LOG_10_GOLD_DENSITY', 'LOG_10_INITIAL_COST',
       'LOG_10_INITIAL_COST_PER_AMOUNT']

CAT_SELECTED = ['GLOBAL_REGION_2', 'GLOBAL_REGION_0']

SELECTED_FEATURES = NUM_SELECTED + CAT_SELECTED

#Random Forest parameters for feature selection with Boruta
RF_FEATURE_SELECTION_PARAMS = {
    "n_estimators":6,
    "max_depth":5,
    "max_features":1,
    "min_samples_split":50,
    "min_samples_leaf":4,
    "random_state":17,
    "n_jobs":-1,
    "class_weight":'balanced'
}