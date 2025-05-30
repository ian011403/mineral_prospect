import optuna
import pandas as pd
import numpy as np
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from optuna.samplers import TPESampler
from optuna_functions import search_space_random_forest, early_prune, optm_score

from settings import MODEL_PRE, OVER, UNDER, RKF

import warnings

warnings.filterwarnings(
    "ignore",
    category=np.VisibleDeprecationWarning,
)

##########################################################################################


def objective(trial):

    params = search_space_random_forest(trial)

    steps_list = [('preprocessor', MODEL_PRE),
                  ('over', OVER),
                  ('under', UNDER),
                  ('classifier', RandomForestClassifier(**params))]

    pipe = ImbPipeline(steps_list)

    early_prune(pipe, X_train, y_train.values.ravel())

    scores = cross_val_score(pipe, X_train, y_train.values.ravel(), cv=RKF, scoring="roc_auc")

    score1, score2 = optm_score(scores)

    return score1, score2


if __name__ == "__main__":

    X_train = pd.read_parquet("../../../../../data/interim/copper/X_train.parquet")
    y_train = pd.read_parquet("../../../../../data/interim/copper/y_train_cat.parquet")

    SAMPLER = TPESampler(
        multivariate=True,
        n_startup_trials=100,
        group=True,
        warn_independent_sampling=False,
        n_ei_candidates=50,
        constant_liar=True
    )

    study = optuna.create_study(
        directions=['maximize', 'minimize'],
        storage='sqlite:///random_forest.db',
        study_name="random_forest",
        load_if_exists=True,
        sampler=SAMPLER
    )

    study.optimize(objective, n_trials=3500, n_jobs=-1)
