import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # bike()
    titanic()


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

    return


def titanic():
    data = pd.read_csv("data/titanic.csv")

    # Total and survived passengers
    total = len(data)
    survived = len(data[data["Survived"] == 1])
    percentage_survived = survived / total * 100
    print("Survival rate: ", percentage_survived)
    print()

    # Survival rate male vs female passengers
    male_passengers = data[data["Sex"] == "male"]
    male_survived = len(male_passengers[male_passengers["Survived"] == 1])
    male_percentage_survived = male_survived / len(male_passengers) * 100
    female_passengers = data[data["Sex"] == "female"]
    female_survived = len(female_passengers[female_passengers["Survived"] == 1])
    female_percentage_survived = female_survived / len(female_passengers) * 100

    print("Male survival rate: ", male_percentage_survived)
    print("Female survival rate: ", female_percentage_survived)
    print()

    # Average fares
    survivors = data[data["Survived"] == 1]
    survivor_fares = survivors["Fare"]
    non_survivors = data[data["Survived"] == 0]
    non_survivor_fares = non_survivors["Fare"]

    print("Average Survivor Fare: ", survivor_fares.mean())
    print("Average Non-survivor Fare: ", non_survivor_fares.mean())
    print()

    return


main()

