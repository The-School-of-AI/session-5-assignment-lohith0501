## Assignment 5 on Functional Parameters
- Submission by Lohith G N (EPAI batch 3)

### Summary of assignment
- This is an assignment where we are expected to write a time it function which is descrived below
- Write a function that gives out the average run time per call, such that its definition is:
- def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

- We should be able to call it like this:

- time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
- time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
- time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
- time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
- time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph

### Functions in session 5 main module
There are six functions in this module as explained below. custom_print is the shortest which just prints the parameters that are passed to it from test module.

- time_it(fn, *args, repetitions=5, **kwargs)
    - This is a function which takes all positional and kyword arguments using args and kwargs concept. There is 1 defined positional argument named fn and keyword argument named repitations with default value set to 5. fn takes function as argyment and is a genralized function to call any function user specified number of times and return the average time taken for calls

- squared_power_list(number, *args, start=0, end=5, **kwargs)
	- This function retruns list by raising number to power from start to end
	- number**start to number**end. Default start is 0 and end is 5
    - There is 1 positional argument named number and keyword argument named start and end. rest are taken care by args and kwargs.

- polygon_area(length, *args, sides=3, **kwargs)
	- This function retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive
    - Here length needs to be greater than 0 and sides need to be between 3 and 6.

- temp_converter(temp, *args, temp_given_in='F', **kwargs)
	- This function converts temprature from celsius 'C' to fahrenheit 'F' or
    fahrenheit to celsius

- speed_converter(speed, *args, dist='KM', time='MIN', **kwargs)
	- This function converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day

- __eq__(self, value)
	- Checks if value of the qualean object is equal to value
	- value can be int, float, bool or decimal

### Test cases 
- Readme contents check for is a list of keywords which will be checked in readme file if it is present or not. Below is the list for reference.
    - README_CONTENT_CHECK_FOR = [
    'time_it(fn, *args, repetitions= 1, **kwargs)',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

- test_session5_readme_exists()
    - Thuis will check if readme file exists along with other modules.

- test_session5_readme_500_words()
    - This will check if contents in readme file are having greater than 500 words.

- test_session5_readme_proper_description()
    - This will check if README_CONTENT_CHECK_FOR content of words are present in readme file or not.
	
- test_session5_readme_file_for_more_than_10_hashes
    - This will check formating of session5.py. It will check for atleast 10 hashes are present in readme file.

- test_session5_indentations()
    - This will check if Your script contains misplaced indentations.
    - Also check code indentation whether it follows PEP8 guidelines

- test_session5_function_name_had_cap_letter()
    - This test will check if you have used Capital letter(s) in your function names

- test_session5_time_it_print()
    - This function will print whatever is passed through here to main module.

- test_function_qualean_type
    - This will check if the input number is of Qualean class type.

- Some of the other test cases are pertaining to
    - Validations for time_it
    - Validations for squared_power_list
    - Validations for polygon_area
    - Validations for temp_converter
    - Validations for speed_converter

Thank You

