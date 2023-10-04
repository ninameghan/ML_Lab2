import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


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

    # Days with more casual than registered rentals
    casual_days = data[data["registered"] < data["casual"]][["dteday"]]
    print("Days with more casual rentals than registered rentals: ")
    print()
    print(casual_days)

    # Plot temperatures against casual & registered rentals
    plt.figure()
    plt.scatter(temperatures, data["registered"])
    plt.scatter(temperatures, data["casual"])
    plt.show()



main()

