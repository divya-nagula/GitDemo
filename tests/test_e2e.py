import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        #  //a[contains(@href,'shop')]    a[href*='shop']
        checkOutPage = homePage.shopItems()
        log.info("Getting all card titles")
        cards = checkOutPage.getCardTitles()
        # h-100']")

        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooters()[i].click()

        checkOutPage.checkOutShop().click()
        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering country name as ind")
        confirmPage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.checkboxAgree().click()
        confirmPage.purchase().click()
        successText = confirmPage.alertSuccess().text
        assert "Success! Thank you!" in successText
        log.info(successText)
        log.info(successText+" "+successText)
        log.info(successText + "_" + successText)
        log.info(successText + "-" + successText)
        log.info(successText + "*" + successText)
        self.driver.close()
