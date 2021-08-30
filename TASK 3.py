# Challenge : Functions !
# Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.

def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1

    return d


string=input("Enter the String")
output=most_frequent(string)
print(output)





##################################################################################
"""
we can also do it using a python library  -"collections"
from this package we import counter
"""

from collections import Counter
def most_frequent(string):

    res = Counter(string)
    return res


string=input("Enter the String")
output2=most_frequent(string)
print(str(output2))