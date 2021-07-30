from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:


        @allure.severity(allure.severity_level.MINOR)
        def test_Logo(self):
            self.driver=webdriver.Chrome()
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
            status=self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
            if status==True:
                assert True
            else:
                assert False
            self.driver.close()

        @allure.severity(allure.severity_level.NORMAL)
        def test_listemployees(self):
            pytest.skip('Skipping test! Later i will implement.')

        @allure.severity(allure.severity_level.BLOCKER)
        def test_Login(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
            self.driver.find_element_by_id("txtUsername").send_keys("Admin")
            self.driver.find_element_by_id("txtPassword").send_keys("admin123")
            self.driver.find_element_by_id("btnLogin").click()
            act_title=self.driver.title

            if act_title=="OrangeHRM 00-00":
                self.driver.close()
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="LoginScreen-30-07", attachment_type=(AttachmentType.PNG))
                self.driver.close()
                assert False

        @allure.severity(allure.severity_level.NORMAL)
        def test_info(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://opensource-demo.orangehrmlive.com/")
            self.driver.find_element_by_id("txtUsername").send_keys("Admin")
            self.driver.find_element_by_id("txtPassword").send_keys("admin123")
            self.driver.find_element_by_id("btnLogin").click()
            self.driver.find_element_by_link_text("My Info")
            self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewMyDetails") # в копии этого файла тест помечен в отчёте аллюра как Broken - AttributeError: 'WebDriver' object has no attribute 'getCurrentUrl'
            subscribe = self.driver.find_element_by_id("Subscriber_link").is_displayed()

            if subscribe==True:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="TrueScreen-30-07",
                              attachment_type=(AttachmentType.PNG))
            else:
                assert False
                allure.attach(self.driver.get_screenshot_as_png(), name="FalseScreen-30-07",
                              attachment_type=(AttachmentType.PNG))
            self.driver.close()

