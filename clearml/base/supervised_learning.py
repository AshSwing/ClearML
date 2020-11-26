from .model import Model

class SupervisedLearning(Model):
    
    def fit(self, X_train, y_train, X_valid=None, y_valid=None):
        pass

    def predict(self, X, y_true):
        pass

    def _compare(self, y_true, y_pred, method='mse'):
        pass
