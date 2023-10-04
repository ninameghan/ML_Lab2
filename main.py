import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import svm


def main():
    plt.close("all")
    bike()
    titanic()
    data, target = generate_data()
    decision_boundaries(data, target)
    plt.show()


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


def generate_data():
    no_of_clusters = 3
    cluster_mean = np.random.rand(no_of_clusters, 2)

    data = np.array([[]])
    target = np.array([[]], dtype='int')

    points_per_cluster = 100
    sigma = 0.1
    for i in range(no_of_clusters):
        noise = sigma * np.random.randn(points_per_cluster, 2)
        cluster = cluster_mean[i, :] + noise
        data = np.append(data, cluster).reshape((i + 1) * points_per_cluster, 2)
        target = np.append(target, [i] * points_per_cluster)

    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], c=target)
    plt.show()
    return data, target


def decision_boundaries(data, target):
    clf = svm.SVC()
    clf.fit(data, target)

    x_min = min(data[:, 0])
    x_max = max(data[:, 0])
    y_min = min(data[:, 1])
    y_max = max(data[:, 1])

    granularity = 0.01
    x, y = np.meshgrid(np.arange(x_min, x_max, granularity), np.arange(y_min, y_max, granularity))
    xy = np.array([x.flatten(), y.flatten()]).transpose()

    prediction = clf.predict(xy)
    prediction = prediction.reshape(x.shape)

    plt.figure()
    plt.imshow(prediction, extent=(x_min, x_max, y_min, y_max), alpha=0.4, origin="lower")
    plt.scatter(data[:, 0], data[:, 1], c=target)

    return


main()

