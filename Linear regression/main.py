import numpy as np
import pandas as pd


def main():
    # Простейшая проверка NumPy
    a = np.array([1, 2, 3])
    print("NumPy array:", a)
    print("NumPy version:", np.__version__)

    # Простейшая проверка Pandas
    df = pd.DataFrame({"col1": [10, 20, 30], "col2": ["a", "b", "c"]})
    print("\nPandas DataFrame:")
    print(df)
    print("Pandas version:", pd.__version__)


if __name__ == "__main__":
    main()
