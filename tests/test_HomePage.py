import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        # ID, Xpath, CSSSelector, Classname, name, linkText
        homePage = HomePage(self.driver)
        log.info("Sending data to application: Name is "+getData["Name"])
        homePage.getName().send_keys(getData["Name"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getPassword().send_keys(getData["Gender"])
        homePage.checkBox().click()
        self.selectOptionByText(homePage.selectGender(), "Female")
        # Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
        # CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
        self.driver.implicitly_wait(20)
        self.selectRadioByText(homePage.selectRadio(), "Student")
        log.info("Submitting form..")
        # homePage.selectRadio().click()
        homePage.submitForm().click()
        log.info("Form submitted!")
        message = homePage.alertSuccess().text
        log.info(message)
        assert "Success" in message
        self.driver.refresh()

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

    @pytest.fixture(params=HomePageData.getTestData("Testcase6"))
    def getData(self, request):
        return request.param
