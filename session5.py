"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
import math
import timeit
import numpy as np

from attr import validate


def time_it(fn, *args, repetitions=5, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    # Repetition should be positive number
    if repetitions == 0:
        return 0
    else:
        start = timeit.timeit()
        for _ in range(0, repetitions):
            value = fn(*args, **kwargs)
        end = timeit.timeit()
        print("Total Time:", end - start)
        speed = end - start
        return value, speed


def custom_print(*args, **kwargs):
    print(*args, **kwargs)


def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block

    # Return the list of number to the power of numbers from start to end
    if start < 0 or end < 0:
        raise ValueError("Value of start or end can't be negative")

    if start > end:
        raise ValueError("Value of start should be less than end")

    if isinstance(number, str) or isinstance(number, complex):
        raise TypeError("Only integer type arguments are allowed")

    if number > 10:
        raise ValueError("Value of number should be less than 10")

    if args:
        raise TypeError("takes maximum 1 positional arguments")

    if kwargs:
        raise TypeError("maximum 2 keyword/named arguments")

    else:
        s_list = []
        for i in range(start, end):
            s_list.append(pow(number, i))
    return s_list


def polygon_area(length, *args, sides=3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if isinstance(length, str) or isinstance(length, complex):
        raise TypeError("Only integer type arguments are allowed")

    if isinstance(sides, str) or isinstance(sides, complex):
        raise TypeError("Only integer type arguments are allowed")

    if args:
        raise TypeError(
            "polygon_area function takes maximum 1 positional arguments, more provided")

    if kwargs:
        raise TypeError(
            "polygon_area function take maximum 1 keyword/named arguments, more provided")

    # Return area
    if (sides >= 3 and sides <= 6) and (length > 0):
        area = sides * (length ** 2) / (4 * math.tan(math.pi / sides))
        return area
    else:
        raise ValueError(
            "Sides haves to be greater than 2 or less than 7 and length shouldnt be negative or zero, it should be positive")


def temp_converter(temp, *args, temp_given_in='F', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if isinstance(temp, str) or isinstance(temp, complex):
        raise TypeError("Only integer type arguments are allowed")

    if isinstance(temp_given_in, str) and temp_given_in not in ['F', 'C']:
        raise ValueError("Only f or c is allowed")

    if isinstance(temp_given_in, complex):
        raise TypeError("Charcater string expected")

    if args:
        raise TypeError(
            "temp_converter function takes maximum 1 positional arguments, more provided")

    if kwargs:
        raise TypeError(
            "temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature

    if temp_given_in == 'F':
        if temp > -459.67:
            celcius_temp = ((temp - 32)*5)/9
            return celcius_temp
        else:
            raise ValueError(
                "Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
    elif temp_given_in == 'C':
        if temp > -273.15:
            fahrenheit_temp = (temp*9)/5 + 32
            return fahrenheit_temp
        else:
            raise ValueError(
                "Temprature can't go below -273.15 celsius = 0 Kelvin")


def speed_converter(speed, *args, dist='KM', time='MIN', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if isinstance(speed, str) or isinstance(speed, complex):
        raise TypeError("Speed can be int or float type only")
    # Return the converted speed

    if isinstance(dist, int) or isinstance(dist, complex):
        raise TypeError("Charcater string expected for distance unit")

    if isinstance(time, int) or isinstance(time, complex):
        raise TypeError("Charcater string expected")

    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")

    if isinstance(time, str) and time not in ['MS', 'S', 'MIN', 'HR', 'DAY']:
        raise ValueError(
            "Incorrect unit of Time. Only ms/s/min/hr/day allowed")

    if isinstance(dist, str) and dist not in ['KM', 'M', 'FT', 'YRD']:
        raise ValueError(
            "Incorrect unit of distance. Only km/m/ft/yrd allowed")

    if args:
        raise TypeError(
            "speed_converter function takes maximum 1 positional arguments, more provided")
    if kwargs:
        raise TypeError(
            "speed_converter function take maximum 2 keyword/named arguments, more provided")

    if speed > 0:
        if dist == 'KM':
            speed = speed
        elif dist == 'M':
            speed = speed * 1000
        elif dist == 'FT':
            speed = speed * 3280.8375
        elif dist == 'YRD':
            speed = speed * 1093.609
        if time == 'HR':
            speed = speed
        elif time == 'DAY':
            speed = speed * 24
        elif time == 'MIN':
            speed = speed / 60
        elif time == 'S':
            speed = speed / (60 * 60)
        elif time == 'MS':
            speed = speed / 3600000
        return round(speed)
    else:
        raise ValueError("Speed can't be negative")
