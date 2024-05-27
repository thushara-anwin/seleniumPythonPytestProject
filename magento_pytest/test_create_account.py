import random
import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("set_up_and_tear_down")
class TestCreateAccount:
    def test_create_account_with_required_fields(self):
        self.driver.find_element(By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#firstname").send_keys("Alaaya")
        self.driver.find_element(By.CSS_SELECTOR, "input#lastname").send_keys("Latta")
        self.driver.find_element(By.CSS_SELECTOR, "input#email_address").send_keys(self.random_email())
        self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("south_middle_123")
        self.driver.find_element(By.CSS_SELECTOR, "input#password-confirmation").send_keys("south_middle_123")
        self.driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div[data-ui-id='message-success']").is_displayed()
    def test_create_account_with_duplicate_email(self):

        self.driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#firstname").send_keys("Alaya")
        self.driver.find_element(By.CSS_SELECTOR, "input#lastname").send_keys("Latta")
        self.driver.find_element(By.CSS_SELECTOR, "input#email_address").send_keys("thushara@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("south_middle_123")
        self.driver.find_element(By.CSS_SELECTOR, "input#password-confirmation").send_keys("south_middle_123")
        self.driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div[data-ui-id='message-error']").is_displayed()
    def test_create_account_with_different_confirmation_password(self):
        self.driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
        self.driver.find_element(By.CSS_SELECTOR,"input#firstname").send_keys("Alaya")
        self.driver.find_element(By.CSS_SELECTOR,"input#lastname").send_keys("Latta")
        self.driver.find_element(By.CSS_SELECTOR,"input#email_address").send_keys("lattaalaya@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("south_middle_123")
        self.driver.find_element(By.CSS_SELECTOR,"input#password-confirmation").send_keys("south_middle")
        self.driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
        #expected_warning_message="password-confirmation-error"
        assert self.driver.find_element(By.CSS_SELECTOR, "div#password-confirmation-error").is_displayed()
    #@pytest.mark.smoke
    def test_create_account_without_required_fields(self):
        self.driver.find_element(By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']").click()
        self.driver.find_element(By.CSS_SELECTOR,"input#firstname").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR,"input#lastname").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR,"input#email_address").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR,"input#password-confirmation").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div#firstname-error").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "div#lastname-error").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "input#email_address+div").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "div#password-error").is_displayed()
        assert self.driver.find_element(By.CSS_SELECTOR, "input#password-confirmation+div").is_displayed()


    def random_email(self):
        num = random.randint(10,90)
        num =str(num)
        return 'alayalatta'+ num +'@gmail.com'

