from setuptools import setup

setup(
    name='WebTesting',
    version='0.0.1',
    packages=['tests'],
    install_requires=[
        'pytest',
        'selenium',
        "webdriver-manager",
        "allure-pytest",
        "faker"
    ],
)