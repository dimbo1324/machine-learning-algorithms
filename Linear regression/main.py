import numpy as np
import pandas as pd


class MyLineReg:
    def __init__(self, n_iter: int = 100, learning_rate: float = 0.1, weights=None):
        self.n_iter = n_iter
        self.learning_rate = learning_rate
        self.weights = weights

    def __str__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"

    def fit(self, X: pd.DataFrame, y: pd.Series, verbose=False):
        X_mod = X.copy()
        X_mod.insert(0, 'x0', 1)

        X_mat = X_mod.values
        y_vec = y.values
        m, n = X_mat.shape

        self.weights = np.ones(n)

        if verbose:
            y0 = X_mat.dot(self.weights)
            print(f"start | loss: {np.mean((y0 - y_vec) ** 2):.2f}")

        for i in range(1, self.n_iter + 1):
            y_hat = X_mat.dot(self.weights)
            errors = y_hat - y_vec
            grad = (2 / m) * X_mat.T.dot(errors)
            self.weights -= self.learning_rate * grad

            if verbose and i % verbose == 0:
                print(f"{i} | loss: {np.mean(errors ** 2):.2f}")

    def get_coef(self) -> np.ndarray:
        return self.weights[1:]
