import numpy as np
import pandas as pd


class MyLineReg:
    def __init__(self, weights, n_iter: int = 100, learning_rate: float = 0.1):
        self.n_iter = n_iter
        self.learning_rate = learning_rate

    def __str__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"

    def fit(self, X: pd.DataFrame, y: pd.Series, verbose: bool = False):
        X.insert(0, 'x0', 1)


def main():
    myLineReg = MyLineReg(10, 0.05)


if __name__ == "__main__":
    main()
