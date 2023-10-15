import pandas as pd  # importing the pandas

colors = pd.Series(["red", "yellow", "green"])
vehicles = pd.Series(["car", "van", "bus"])
numbers = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # creating a series


data_frame = pd.DataFrame(
    {"color": colors, "vehicles": vehicles}
)  # data frame creation
print(data_frame)

cars_data = pd.read_csv("car-sales.csv")  # read csv file
print(cars_data)

print(data_frame.describe())  # it describes the hole dataset
print(
    data_frame.info()
)  # it gives us information about how many rows and how many columns
print(numbers.mean())  # to know the mean

doors = cars_data["Doors"]  # to copy a column in the dataset
print(doors)

print(cars_data.head())  # it returns the top 5 rows in the dataset
print(cars_data.head(8))  # it returns the top 8 rows in the dataset
print(cars_data.tail())  # it return the last 5 rows in the dataset
print(cars_data.tail(8))  # it returns the last 8 rows in the dataset

birds = pd.Series(
    ["crow", "peacock", "parrot", "pigeon"], index=[3, 4, 5, 3]
)  # new thing here is we can set indexes on our own choose too.
print(birds)


# .loc() && .iloc()
print(
    birds.loc[3]
)  # loc is based on the indexes. it will returns the data having index value of 3
# another thing is we can manually set the indexes to an series.beacuse indexes can duplicated
print(
    birds.iloc[3]
)  # it returns the data presented at position 3 and positions are starts with 0 to n-1


# Howw to access a column in a dataset
print(cars_data.Make)  # one way (dot notation)
print(cars_data["Make"])  # another way (normal notation)

# if column name containing the space in it, then dot notation does not works,go with the normal notation

print(
    cars_data[cars_data["Make"] == "Toyota"]
)  # it will return the where make equals to toyota

import matplotlib.pyplot as plt  # importing matplotlib

cars_data["Doors"].hist()
plt.show()
