from setuptools import setup, find_packages # type: ignore
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(filename)->List[str]:
    get_requirements=[]
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
        return requirements


setup(
    name='endtoendmlproject',
    version='0.1',
    packages=find_packages(),
    author="Ankit",
    install_requires=get_requirements('requirements.txt')
)