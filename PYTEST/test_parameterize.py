import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#how do we do parametrization in pytest-QA



@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


'''to run test for diff data sets- use parameterize marker just above the test'''

class TestHubSpot(BaseTest):
    @pytest.mark.parametrize(
                              "username,pswd",
                              [
                                  ('admin@gmail.com','test123'),
                                  ('vineethac@gmail.com','test234@')
                              ]
                              )
    def testLogin(self,username,pswd):
        '''
        This method is used to login to hub spot application
        :param username:
        :param pswd:
        :return:
        '''

        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID,'username').send_keys(username)
        self.driver.find_element(By.ID,'password').send_keys(pswd)
