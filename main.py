import numpy as np
import pandas as pd


def main():
    bike()


def bike():
    data = pd.read_csv("data/day.csv")
    non_holiday = data[data["holiday"] == 0][["casual", "registered"]]
    holiday = data[data["holiday"] == 1][["casual", "registered"]]

    # Print results:
    print("Non-Holiday rentals:")
    print()
    print(non_holiday.mean())
    print("Holiday rentals:")
    print()
    print(holiday.mean())


main()