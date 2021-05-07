import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model1 = None
__locations1 = None
__data_columns1 = None
__model2 = None


# Bangalore model
def get_estimated_price(location, total_sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model1.predict([x])[0], 2)


# Ahmedabad model

def get_estimated_price1(location, total_sqft, size, bath):
    try:
        loc_index = __data_columns1.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns1))
    x[0] = size
    x[1] = total_sqft
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model2.predict([x])[0], 2)


# Bangalore
def get_location_names():
    return __locations


# Ahmedabad
def get_location_names1():
    return __locations1


# Bangalore
def load_saved_artifacts():
    print("Loading saved artifacts")
    global __data_columns
    global __locations
    global __model1

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/DataScience.pickle", 'rb') as f:
        __model1 = pickle.load(f)

    print("Loading the artifacts is done")


# Ahmedabad
def load_saved_artifacts1():
    print("Loading saved artifacts")
    global __data_columns1
    global __locations1
    global __model2

    with open("./artifacts/col.json", 'r') as f1:
        __data_columns1 = json.load(f1)['data_columns']
        __locations1 = __data_columns1[3:]

    with open("./artifacts/ahmed.pickle", 'rb') as f1:
        __model2 = pickle.load(f1)

    print("Loading the artifacts is done")


# Bangalore
def get_data_columns():
    return __data_columns


# Ahmedabad
def get_data_columns1():
    return __data_columns1


if __name__ == '__main__':
    load_saved_artifacts()
    load_saved_artifacts1()
    print('#Bangalore')
    print(get_location_names())
    print('#Ahmedabad')
    print(get_location_names1())
    print('#Bangalore')
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print('#Ahmedabad')
    print(get_estimated_price('Bopal', 3000, 2, 2))
    print(get_estimated_price('SG Highway', 2000, 2, 2))
