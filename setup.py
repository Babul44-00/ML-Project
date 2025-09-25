from setuptools import find_packages,setup
from typing import List
hypen_e_dot = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''This function will return the list of requirements'''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove(hypen_e_dot)

    return requirements       
 
setup(
name='Ml project',
version="0.0.1",
author='krishna',
author_email='krishna123@gail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)