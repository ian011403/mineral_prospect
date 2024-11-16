from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np
import pandas as pd
import optuna


def search_space_decision_tree(trial):
    params = dict()
    params['max_depth'] = trial.suggest_int('max_depth', 2, 6)
    params['min_samples_split'] = trial.suggest_int('min_samples_split', 2, 40)
    params['min_samples_leaf'] = trial.suggest_int('min_samples_leaf', 5, 45)
    params['criterion'] = 'entropy'
    params['class_weight'] = 'balanced'
    params['random_state'] = trial.suggest_int('random_state', 0, 100)
    params['max_features'] = trial.suggest_int('max_features', 1, 6)
    return params


def search_space_xgboost(trial):
    params = dict()
    params['n_estimators'] = trial.suggest_int('n_estimators', 1, 500, log = True)
    params['max_depth'] = trial.suggest_int('max_depth', 2, 6)
    params['learning_rate'] = trial.suggest_float('learning_rate', 0.01, 0.2)
    params['min_child_weight'] = trial.suggest_int('min_child_weight', 1, 5)
    params['gamma'] = trial.suggest_float('gamma', 0.0, 0.5)
    params['subsample'] = trial.suggest_float('subsample', 0.6, 0.9)
    params['colsample_bytree'] = trial.suggest_float('colsample_bytree', 0.6, 0.9)
    params['reg_alpha'] = trial.suggest_float('reg_alpha', 0.0, 0.5)
    params['reg_lambda'] = trial.suggest_float('reg_lambda', 0.0, 0.5)
    params['importance_type'] = trial.suggest_categorical('importance_type', 
                                                          ['gain', 'weight', 'cover', 'total_gain', 'total_cover'])
    params['random_state'] = trial.suggest_int('random_state', 0, 100)
    return params


def search_space_random_forest(trial):
    params = dict()
    params['n_estimators'] = trial.suggest_int('n_estimators', 1, 100)
    params['max_depth'] = trial.suggest_int('max_depth', 2, 7)
    params['max_features'] = trial.suggest_int('max_features', 1, 27)
    params['min_samples_split'] = trial.suggest_int('min_samples_split', 2, 50)
    params['min_samples_leaf'] = trial.suggest_int('min_samples_leaf', 1, 30)
    params['random_state'] = trial.suggest_int('random_state', 1, 100) 
    params['class_weight'] = 'balanced'
    return params


def optm_score(scores):

    std2 = np.std(scores)
    std = np.sqrt(std2)
    mean = np.mean(scores)

    #if mean < 0.65:
        #raise optuna.TrialPruned()
    
    if std == 0:
        raise optuna.TrialPruned()

    #variation = mean/std
    
    #if variation == np.inf:
    #    raise optuna.TrialPruned()
    #else:
    #    variation = np.log10(variation)

    #return mean + variation

    return mean, np.log10(std)

def early_prune(pipe, X_train, y_train):

    X_att, X_valid, y_att, y_valid = train_test_split(X_train, y_train, test_size=30, random_state=42) 

    X_att = pd.DataFrame(X_att, columns=X_train.columns)
    X_valid = pd.DataFrame(X_valid, columns=X_train.columns)

    pipe.fit(X_att, y_att)

    roc_auc = roc_auc_score(y_valid, pipe.predict_proba(X_valid)[:, 1])

    if roc_auc < 0.5:
        raise optuna.TrialPruned()
    
    return roc_auc