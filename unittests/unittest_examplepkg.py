"""
test the import and the call for different functions
Author: Tano Müller
"""

import unittest


class TestExamplePKG(unittest.TestCase):
    
    def test_exampleclassfile(self):
        from example_pkg.exampleclassfile import exampleclass, independent_function, do_stuff_with_data_file
        independent_function()
        ec = exampleclass()
        ec.sample_class_function()
        do_stuff_with_data_file()

    def test_subdirclassfile(self):
        from example_pkg.subdir.subdirclassfile import subdirclass, call_function_from_parent_directory
        call_function_from_parent_directory()
        sdc = subdirclass()
        sdc.sample_class_function()



if __name__ == '__main__':
    unittest.main()
