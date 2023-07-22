# pytest-selenium-allure
This repo contains tests written with WebdriverIO for [OrangeHRM](https://opensource-demo.orangehrmlive.com/) website.

To manage project customized config files are used so user is able to run project without making any change in the code

## Setup

### Install software and check out the project
- Download and install Pyhton ( at least 3.X )
- Install PyCharm
- Clone and checkout the github project 
- Go to the terminal and execute "pip install ." command
  
### Command to run test 
```
pytest
```
Run the "pytest" command for run test on the chrome browser and create dir allure-results

```
pytest --browser firefox
```
Run the "pytest --browser firefox" command for run test on the firefox browser and create dir allure-results

```
pytest --browser edge
```
Run the "pytest --browser edge" command for run test on the edge browser and create dir allure-results

```
pytest --headless false
```
Run the "pytest --headless false" command for run test with a graphical user interface and create dir allure-results

You can see [Allure](https://leraroy.github.io/pytest-selenium-allure/) Report on GitHub Pages
