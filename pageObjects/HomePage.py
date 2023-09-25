from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    #radio = (By.XPATH, "//input[@id='inlineRadio1']")
    radio = (By.XPATH, "//input[@type='radio']")
    submit = (By.XPATH, "//input[@type='submit']")
    alert_success = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)

    def selectRadio(self):
        return self.driver.find_elements(*HomePage.radio)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def alertSuccess(self):
        return self.driver.find_element(*HomePage.alert_success)