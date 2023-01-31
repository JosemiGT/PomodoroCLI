from setuptools import setup, find_packages

setup(
    name='pomodoroCLI',
    version='0.1',
    description='Pomodoro CLI',
    author='JosemiGT',
    author_email='jmgt93@gmail.com',
    packages=find_packages(),
    install_requires=[
        'time',
    ],
)