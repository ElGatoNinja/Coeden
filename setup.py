
from setuptools import setup, find_packages

setup(
    name='coeden',
    version='0.1.0',
    license='MIT',
    author="Jaime G Alonso",
    author_email='JaimeGAlonso@outlook.com',
    packages=find_packages('src'),
    python_requires= '>=3.10',
    package_dir={'': 'src'},
    url='https://github.com/ElGatoNinja/Trees',
    keywords='tree trees python data structure',
)