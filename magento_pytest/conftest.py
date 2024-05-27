#import os
#import sys
import pytest
from utilities import ReadConfigurations
#current_path = os.path.dirname(os.path.realpath(__file__))
#utilities_path = os.path.join(current_path, '..', 'utilities')
#sys.path.append(utilities_path)
from selenium import webdriver
#import ReadConfigurations as readConfigurations
# from utilities import ReadConfigurations



@pytest.fixture()
def set_up_and_tear_down(request):
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid name")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    URL = ReadConfigurations.read_configurations("basic info", "url")
    driver.get(URL)
    request.cls.driver = driver
    yield
    driver.close()