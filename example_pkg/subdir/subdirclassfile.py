"""
simple example python file to provide an example how to use subdirectories with python files

Author: Tano Müller
"""

# print info when this script is loaded
print("loaded the subdirclassfile.py file from the subdirectory")

def independent_subdir_function():
    """
    simple function that does not depend on anything else and does not belong to a class
    """
    print("calling a function in subdirclassfile.py file that deos not belong to a class")

def call_function_from_parent_directory():
    """
    call a function that depends on something from the parent directory
    """
    print("calling the function that tries to call a function from the parent directory")
    from example_pkg.exampleclassfile import independent_function
    independent_function()


class subdirclass():
    """
    example class that can be loaded
    """

    def __init__(self):
        print("creating an subdirclass object")
    
    def sample_class_function(self):
        print("calling a class function from the subdirclass")

