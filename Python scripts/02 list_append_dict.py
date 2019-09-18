#!/usr/bin/env python3.6

###
#
# Initiate a dictionary (with 'keys' only) outside of FOR loop and an empty list
list_test = []
dict_test = {'one': '', 'two': ''}
#
###

###
#
# First dictionary
split_output = ['1', '2']
list_index = 0
for key in dict_test.keys():
    dict_test[key] = split_output[list_index]
    list_index += 1

# Append the 1st dictionary to existing 'list_test' list
list_test.append(dict_test)

# Print and check the value of 'list_test' list
print(list_test)
#
###

###
#
# Second dictionary
split_output = ['11', '22']
list_index = 0
for key in dict_test.keys():
    dict_test[key] = split_output[list_index]
    list_index += 1

# Print and check the value of 'list_test' list again before append the 2nd dictionary.
# We notice that the value of the list changes automatically | immediately right after the value of dictionary changes
print(list_test)

# Append the 2nd dictionary to existing 'list_test' list
list_test.append(dict_test)

# Print and check the value of 'list_test' list
print(list_test)
#
###


##########
#
# Returned results - this is not expected. We have revised the script (check '03 list_append_dict_v2.py' for more details)
# [{'one': '1', 'two': '2'}]
# [{'one': '11', 'two': '22'}]
# [{'one': '11', 'two': '22'}, {'one': '11', 'two': '22'}]
#
##########
