# 1
""" prevent the program from crashing. If the user enters something that is out of range just print a default output of 'Fruit pie'
"""

fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)
