from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'AI_Product_Recommender',
    version = '0.1',
    author = 'Nishant',
    packages = find_packages(),
    install_requires = requirements,
)