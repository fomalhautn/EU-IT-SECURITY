def arrayCheck(nums):
    '''return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.'''
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False
#print(arrayCheck([1, 1, 2, 3, 1]))
#print(arrayCheck([1, 1, 2, 4, 1]))
#print(arrayCheck([1, 1, 2, 1, 2, 3]))


def stringBits(str):
    '''return a new string made of every other character starting with the first'''
    new_str=''
    for i in range(len(str)):
        if i%2==0:
            new_str+=str[i]
    return new_str

#print(stringBits('Hello'))
#print(stringBits('Hi'))
#print(stringBits('Heeololeo'))


# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string. Examples: end_other('Hiabc',
# 'abc') → True end_other('AbC', 'HiaBc') → True end_other('abc', 'abXabc') → True

def end_other(a, b):
    '''return True if either of the strings appears at the very end of the other string'''
    a=a.lower()
    b=b.lower()
    if len(a)>=len(b):
        if a[len(a)-len(b):]==b:
            return True
    else:
        if b[len(b)-len(a):]==a:
            return True
    return False

#print(end_other('Hiabc', 'abc'))
#print(end_other('AbC', 'HiaBc'))
#print(end_other('abc', 'abXabc'))


#Given a string, return a string where for every char in the original, there are two chars.
#doubleChar('The') → 'TThhee' doubleChar('AAbb') → 'AAAAbbbb' doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    '''return a string where for every char in the original, there are two chars.'''
    new_str=''
    for i in range(len(str)):
        new_str+=str[i]*2
    return new_str

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))