from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a") # driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button") # product.find_element(By.CSS_SELECTOR, ".card-footer
    # button").click()
    checkoutShop = (By.CSS_SELECTOR, "a[class*='btn-primary']") # driver.find_element(By.CSS_SELECTOR,
    # "a[class*='btn-primary']"
    checkoutFinal = (By.XPATH, "//button[@class='btn btn-success']") # driver.find_element(By.XPATH, "//button[
    # @class='btn btn-success']")



    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutShop(self):
        return self.driver.find_element(*CheckOutPage.checkoutShop)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkoutFinal).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
