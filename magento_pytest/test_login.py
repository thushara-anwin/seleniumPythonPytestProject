import random
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("set_up_and_tear_down")
class TestLogin:
    def test_login_with_valid_credential(self):
        self.driver.find_element(By.XPATH,
                            "//ul[@class='header links']"
                            "//following::li[@data-label='or']/a[contains(text(),'Sign In')][1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('thushara@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('south_middle_123')
        self.driver.find_element(By.XPATH,"//div[@class='primary']"
                                     "/button[@id='send2' and @type ='submit' and @name ='send']/span").click()
        displayed_message = 'Welcome'
        assert self.driver.find_element(By.XPATH,"//span[contains(text(),'Welcome')]").text.__contains__(displayed_message)
    def test_login_with_invalid_email_valid_password(self):
        self.driver.find_element(By.CSS_SELECTOR,"li.authorization-link>a").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(self.random_email())
        self.driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('south_middle_123')
        self.driver.find_element(By.CSS_SELECTOR,"div+div>div.primary>button#send2").click()
        assert self.driver.find_element(By.CSS_SELECTOR,"div[data-ui-id='message-error']").is_displayed()
    def test_login_with_valid_email_invalid_password(self):
        self.driver.find_element(By.CSS_SELECTOR,"li.authorization-link>a").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('thushara@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('123')
        self.driver.find_element(By.CSS_SELECTOR,"div+div>div.primary>button#send2").click()
        assert self.driver.find_element(By.CSS_SELECTOR,"div[data-ui-id='message-error']").is_displayed()
    def test_login_with_no_credentials(self):
        self.driver.find_element(By.CSS_SELECTOR,"li.authorization-link>a").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('')
        self.driver.find_element(By.CSS_SELECTOR, "input[name='login[password]']").send_keys('')
        expected_warning_message='This is a required field.'
        self.driver.find_element(By.CSS_SELECTOR,"div+div>div.primary>button#send2").click()
        assert self.driver.find_element(By.CSS_SELECTOR,"div#email-error").text.__contains__(expected_warning_message)
        assert self.driver.find_element(By.CSS_SELECTOR,"div#pass-error").is_displayed()

    def random_email(self):
        num = random.randint(10,90)
        num =str(num)
        return 'thushara'+ num +'@gmail.com'

