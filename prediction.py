import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

b0 = 206864.41293140475
b1 = 25132.383289392073
b2 = -30142.386444149404
b3 = 41260.25726397974
b4 = 88441.61377916373

dataframe = pd.read_csv("housing.csv")
dataframe = dataframe.dropna().reset_index(drop=True)

def show_graphs(user_income,predicted_price):
    plt.scatter(
    dataframe['median_income'],
    dataframe['median_house_value'],
    alpha=0.3
)

    plt.scatter(
        user_income,
        predicted_price,
        s=200,
        marker='x'
    )

    plt.xlabel("Median Income")
    plt.ylabel("House Price")
    plt.show()


def normalizing():
    housing_median_age = float(input("Enter the median age: "))
    total_rooms = float(input("Enter the total number of rooms: "))
    total_bedrooms = float(input("Enter the total number of bedrooms: "))
    median_income = float(input("Enter the median income of the area: "))

    housing_median_age1 = (housing_median_age - dataframe['housing_median_age'].mean())/dataframe['housing_median_age'].std()
    total_rooms1 = (total_rooms- dataframe['total_rooms'].mean())/dataframe['total_rooms'].std()
    total_bedrooms1 = (total_bedrooms - dataframe['total_bedrooms'].mean())/dataframe['total_bedrooms'].std()
    median_income1 = (median_income - dataframe['median_income'].mean())/dataframe['median_income'].std()

    return housing_median_age1,total_rooms1,total_bedrooms1,median_income1,housing_median_age,total_rooms,total_bedrooms,median_income



array = normalizing()
h = b0 + b1*array[0] + b2*array[1] + b3*array[2] + b4*array[3]



print("Predicted price of house is: ")
print(h)

show_graphs(array[7],h)