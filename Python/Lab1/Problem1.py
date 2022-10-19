# Given the string:s = 'Lexicon' Use indexing to print the out the following: 'L' 'n' 'Lexi' 'con' 'on'
# Bonus: Use indexing to reverse the string

s = 'Lexicon'
print(s[0])
print(s[-1])
print(s[0:4])
print(s[4:7])
print(s[5:7])


# Given this nested list: my_list = [3,7,[1,4,'hello']] Reassign "hello to be "goodbye"
my_list = [3,7,[1,4,'hello']]
my_list[2][2] = 'goodbye'
print(my_list)

# Using keys and indexing, grab the 'hello' from the following dictionaries: d1 = {'simple_key':'hello'} d2 = {'k1':{'k2':'hello'}} d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

# Use a set to find the unique values of the list below: my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(my_list))

# You are given two variables: age = 4 name = "Sammy"
# Use print formatting to print the following string: "Hello my dog's name is Bobby and he is 4 years old"
age = 4
name = "Sammy"
print("Hello my dog's name is {} and he is {} years old".format(name,age))