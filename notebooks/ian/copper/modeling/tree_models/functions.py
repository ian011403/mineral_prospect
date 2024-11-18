def importance_estimation_decision_tree(X, y, pipe):

    pipe.fit(X, y)

    model = pipe.named_steps["classifier"]

    feature_importances = model.feature_importances_

    return feature_importances


def importance_experiment_decision_tree(X_list, y_list, pipe):

    importances_list = [importance_estimation_decision_tree(X, y, pipe) for X, y in zip(X_list, y_list)]

    return importances_list
