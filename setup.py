from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirement = []
    with open(file_path) as f:
        requirement = f.readlines()
    requirement = [read.replace('\n','') for read in requirement]
    if hypen_e_dot in requirement:
        requirement.remove(hypen_e_dot)
        
setup(
name = 'mlproject',
version= '0.0.1',
author = 'pankaj',
author_email = 'rawatpankaj9919@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')
)