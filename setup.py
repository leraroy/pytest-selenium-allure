from setuptools import setup

setup(
    name='WebTesting',
    version='0.0.1',
    install_requires=[
        'pytest',
        'selenium',
        "webdriver-manager",
        "allure-pytest",
        "faker"
    ],
)