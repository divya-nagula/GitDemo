from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")  # driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CLASS_NAME, "alert-success")  # driver.find_element(By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def checkboxAgree(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def alertSuccess(self):
        return self.driver.find_element(*ConfirmPage.alert)
