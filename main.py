import numpy as np
import pandas as pd


def main():
    bike()


def bike():
    data = pd.read_csv("data/day.csv")

    # Holiday vs Non-holiday rentals
    non_holiday = data[data["holiday"] == 0][["casual", "registered"]]
    holiday = data[data["holiday"] == 1][["casual", "registered"]]
    print("Non-Holiday rentals:")
    print()
    print(non_holiday.mean())
    print("Holiday rentals:")
    print()
    print(holiday.mean())
    print()

    # Min & Max temperature
    temperatures = data["temp"] * (39 - (-8)) + (-8)
    print("Minimum temperature: ", temperatures.min())
    print("Maximum temperature: ", temperatures.max())
    print()



main()

