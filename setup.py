from setuptools import find_packages,setup
from typing import List

HYPEN_e_dot="-e."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_obj:
        reuiqrements=file_obj.readlines()
        requirements=[req.replcae("\n","")for req in requirements]
        if HYPEN_e_dot in requirements:
            requirements.remove(HYPEN_e_dot)

        return requirements


setup(
    name="DS_ML_Project",
    version='0.0.1',
    author="Harsh",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)