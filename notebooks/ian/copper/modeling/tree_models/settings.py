from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.pipeline import Pipeline
from category_encoders import BinaryEncoder
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer

from constants import NUM_FEATURES, CAT_FEATURES, NUM_SELECTED, CAT_SELECTED, N_COMP

######################### TRANSFORMATIONS #########################
OVER = SMOTE(sampling_strategy="auto")
UNDER = RandomUnderSampler(sampling_strategy="auto")

CAT_PIPE = Pipeline(steps=[
    ('binary_encoder', BinaryEncoder())
])

NUM_BASIC_STEPS =  [
        ('scaler', StandardScaler()),
        ('imputer', KNNImputer(n_neighbors=5)),
]

NUM_PIPE = Pipeline(steps=NUM_BASIC_STEPS)

NUM_PCA_PIPE = Pipeline(steps=NUM_BASIC_STEPS + [( 'pca', PCA(n_components=N_COMP))])


####################### PREPROCESSORS #######################
FEAT_SEL_PRE = ColumnTransformer(
    transformers=[
        ('num', NUM_PIPE, NUM_FEATURES),
        ('cat', CAT_PIPE, CAT_FEATURES), 
        ('array', FunctionTransformer(lambda X: X.values, validate=False), [])
    ]
)

MODEL_PRE = ColumnTransformer(
    transformers=[
        ('num', NUM_PCA_PIPE, NUM_SELECTED),
        ('cat', CAT_PIPE, CAT_SELECTED),
        ('array', FunctionTransformer(lambda X: X.values, validate=False), [])
    ]
)

###################### CROSS VALIDATION ##########################

RKF = RepeatedStratifiedKFold(n_splits=2, n_repeats=5, random_state=42)