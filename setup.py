"""
setup script for the example package
call ist e.g. by:
python3 setup.py bdist_wheel
pip3 install dist/examplepkg-0.0.1-py3-none-any.whl --user

alternative just apply:
pip3 install .

Author: Tano Müller
"""
import setuptools

# do the actual setup
setuptools.setup(
    name="examplepkg",
    version="0.1",
    author="enter your name here",
    author_email="some@email.com",
    description="example package to have a basic structur that is installable",
    long_description="example package to have a basic structur that is installable",
    url="www.enter-your-url.here",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "Operating System :: OS Independent"],
    include_package_data=True,
    python_requires='>=3.0',
)
