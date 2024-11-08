from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import numpy as np
import optuna


def search_space(trial):
    params = dict()
    params['max_depth'] = trial.suggest_int('max_depth', 2, 6)
    params['min_samples_split'] = trial.suggest_int('min_samples_split', 2, 40)
    params['min_samples_leaf'] = trial.suggest_int('min_samples_leaf', 5, 45)
    params['criterion'] = 'entropy'
    params['class_weight'] = 'balanced'
    params['random_state'] = trial.suggest_int('random_state', 0, 100)
    params['max_features'] = trial.suggest_int('max_features', 1, 6)
    return params

def optm_score(scores):

    std2 = np.std(scores)
    std = np.sqrt(std2)
    mean = np.mean(scores)

    #if mean < 0.65:
        #raise optuna.TrialPruned()
    
    if std == 0:
        raise optuna.TrialPruned()

    variation = mean/std
    
    if variation == np.inf:
        raise optuna.TrialPruned()
    else:
        variation = np.log10(variation)

    return mean + variation

def early_prune(pipe, X_train, y_train):

    X_att, X_valid, y_att, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=42) 

    pipe.fit(X_att, y_att)

    roc_auc = roc_auc_score(y_valid, pipe.predict_proba(X_valid)[:, 1])

    #if roc_auc < 0.5:
        #raise optuna.TrialPruned()
    
    return roc_auc