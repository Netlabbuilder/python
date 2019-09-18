#!/usr/bin/env python3.6

###
#
# We will create the dictionary inside the FOR loop
# Initiate an empty list
list_test = []
#
###

###
#
# Create a list of lists of values. These values will be assigned to dictionary
split_output = [['1', '2'], ['11', '22']]
#
###

###
#
for output in split_output:
    dict_test = {
        'one': '',
        'two': ''
    }
    list_index = 0
    for key in dict_test.keys():
        dict_test[key] = output[list_index]
        list_index += 1
        
    # Append the dictionaries to existing 'list_test' list
    list_test.append(dict_test)
#
###
# Print and check the value of 'list_test' list
print(list_test)
#
###


##########
#
# Returned results - this is expected.
# [{'one': '1', 'two': '2'}, {'one': '11', 'two': '22'}]
#
##########
