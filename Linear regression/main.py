import numpy as np
import pandas as pd


class MyLineReg:
    def __init__(self, n_iter: int = 100, learning_rate: float = 0.1):
        self.n_iter = n_iter
        self.learning_rate = learning_rate

    def __str__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"



def main():
    a = MyLineReg(10, 0.05)
    print(a)


if __name__ == "__main__":
    main()

