"""
simple example python file to provide an example class and and a function that is not 
bound to the class

Author: Tano Müller
"""

# print info when this script is loaded
print("loaded the exampleclassfile.py file")

def independent_function():
    """
    simple function that does not depend on anything else and does not belong to a class
    """
    print("calling a function in exampleclass.py file that deos not belong to a class")

def do_stuff_with_data_file():
    """
    read a data file that is provided with the package
    """
    import os
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, "data/exampledata.txt")
    print("reading the data file that was added to the installation:")
    with open(file_path, "r") as f:
        print(f.read())

class exampleclass():
    """
    example class that can be loaded
    """

    def __init__(self):
        print("creating an exampleclass object")
    
    def sample_class_function(self):
        print("calling a class function")

