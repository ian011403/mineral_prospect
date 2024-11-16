from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.pipeline import Pipeline
from category_encoders import BinaryEncoder
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer

from constants import NUM_FEATURES, CAT_FEATURES

######################### TRANSFORMATIONS #########################
OVER = SMOTE(sampling_strategy="auto")
UNDER = RandomUnderSampler(sampling_strategy="auto")

CAT_PIPE = Pipeline(steps=[
    ('binary_encoder', BinaryEncoder())
])

num_steps = [
        ('scaler', StandardScaler()),
        ('imputer', KNNImputer(n_neighbors=5)),
]

NUM_PIPE = Pipeline(steps=num_steps)


####################### PREPROCESSORS #######################
FEAT_SEL_PRE = ColumnTransformer(
    transformers=[
        ('num', NUM_PIPE, NUM_FEATURES),
        ('cat', CAT_PIPE, CAT_FEATURES), 
        ('array', FunctionTransformer(lambda X: X.values, validate=False), [])
    ]
)

###################### CROSS VALIDATION ##########################

RKF = RepeatedStratifiedKFold(n_splits=2, n_repeats=5, random_state=42)