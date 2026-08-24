#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    pass

def main():
    lst = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {lst[0]}")
    print(f"R2-score with feature(s) X1: {lst[1]}")
    print(f"R2-score with feature(s) X2: {lst[2]}")
    print(f"R2-score with feature(s) X3: {lst[3]}")
    print(f"R2-score with feature(s) X4: {lst[4]}")
    print(f"R2-score with feature(s) X5: {lst[5]}")


if __name__ == "__main__":
    main()
