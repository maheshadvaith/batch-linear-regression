import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("housing.csv")
dataframe = dataframe.dropna().reset_index(drop=True)

m = len(dataframe)
iterations = 600
b0 = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
weightArray = [b0,b1,b2,b3,b4]
n = 4

# housing_median_age, total_rooms, total_bedrooms, median_income

alpha = 1e-6

def normalizing():
    dataframe['housing_median_age'] = (dataframe['housing_median_age'] - dataframe['housing_median_age'].mean())/dataframe['housing_median_age'].std()
    dataframe['total_rooms'] = (dataframe['total_rooms'] - dataframe['total_rooms'].mean())/dataframe['total_rooms'].std()
    dataframe['total_bedrooms'] = (dataframe['total_bedrooms'] - dataframe['total_bedrooms'].mean())/dataframe['total_bedrooms'].std()
    dataframe['median_income'] = (dataframe['median_income'] - dataframe['median_income'].mean())/dataframe['median_income'].std()

normalizing()
costs = []
def costFunction():
    predictions = (
        weightArray[0]
        + weightArray[1]*dataframe['housing_median_age']
        + weightArray[2]*dataframe['total_rooms']
        + weightArray[3]*dataframe['total_bedrooms']
        + weightArray[4]*dataframe['median_income']
    )

    errors = predictions - dataframe['median_house_value']
    print("COST FUNCTION:")
    print(np.sum(errors**2) / (2*m))
    costs.append(np.sum(errors**2) / (2*m))







print("starting process...")
for i in range(0,iterations):
    sum = 0
    for j in range(0,m):
        sum += (weightArray[0] + weightArray[1]*dataframe['housing_median_age'][j] + weightArray[2]*dataframe['total_rooms'][j] + weightArray[3]*dataframe['total_bedrooms'][j] + weightArray[4]*dataframe['median_income'][j] - dataframe['median_house_value'][j])*1
    
    sum1 = 0
    for j in range(0,m):
        sum1 += (weightArray[0] + weightArray[1]*dataframe['housing_median_age'][j] + weightArray[2]*dataframe['total_rooms'][j] + weightArray[3]*dataframe['total_bedrooms'][j] + weightArray[4]*dataframe['median_income'][j]- dataframe['median_house_value'][j])*dataframe['housing_median_age'][j]
    
    sum2 = 0
    for j in range(0,m):
        sum2 += (weightArray[0] + weightArray[1]*dataframe['housing_median_age'][j] + weightArray[2]*dataframe['total_rooms'][j] + weightArray[3]*dataframe['total_bedrooms'][j] + weightArray[4]*dataframe['median_income'][j]- dataframe['median_house_value'][j])*dataframe['total_rooms'][j]
    
    sum3 = 0
    for j in range(0,m):
        sum3 += (weightArray[0] + weightArray[1]*dataframe['housing_median_age'][j] + weightArray[2]*dataframe['total_rooms'][j] + weightArray[3]*dataframe['total_bedrooms'][j] + weightArray[4]*dataframe['median_income'][j]- dataframe['median_house_value'][j])*dataframe['total_bedrooms'][j]
    
    sum4 = 0
    for j in range(0,m):
        sum4 += (weightArray[0] + weightArray[1]*dataframe['housing_median_age'][j] + weightArray[2]*dataframe['total_rooms'][j] + weightArray[3]*dataframe['total_bedrooms'][j] + weightArray[4]*dataframe['median_income'][j]- dataframe['median_house_value'][j])*dataframe['median_income'][j]
    
    weightArray[0] = weightArray[0] - alpha*(sum)
    weightArray[1] = weightArray[1] - alpha*(sum1)
    weightArray[2] = weightArray[2] - alpha*(sum2)
    weightArray[3] = weightArray[3] - alpha*(sum3)
    weightArray[4] = weightArray[4] - alpha*(sum4)
    costFunction()
    
print("finished")
print(weightArray)
plt.plot(costs)
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.title("Cost vs Iteration")
plt.show()