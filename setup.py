from typing import List

from setuptools import setup,find_packages
EXCLUDE_FROM_PACKAGES = ['-e .']
def get_requirements(file_name:str) ->List[str]:
    """
    get list of requirements
    :param file_name:
    :return:
    """
    with open(file_name) as file_object:
         file_data = file_object.readlines()
         file_data = [x.strip() for x in file_data if x not in EXCLUDE_FROM_PACKAGES]
    return file_data

setup(

    name='srinivas-mlproject',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('reqirements.txt'),
    author='srinivas',
    author_email='r.l.srinivas64@gmail.com',

)