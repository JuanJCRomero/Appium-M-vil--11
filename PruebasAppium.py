from appium import webdriver
from time import sleep
import unittest

class CalculadoraTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "emulator-5554",
            "automationName": "UiAutomator2",
            "appPackage": "com.android.calculator2",
            "appActivity": "com.android.calculator2.Calculator",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(2)

    def test_suma(self):
        self.driver.find_element_by_id("digit_7").click()
        self.driver.find_element_by_accessibility_id("plus").click()
        self.driver.find_element_by_id("digit_5").click()
        self.driver.find_element_by_accessibility_id("equals").click()
        resultado = self.driver.find_element_by_id("result").text
        self.assertEqual(resultado, "12")

    def test_resta(self):
        self.driver.find_element_by_id("digit_9").click()
        self.driver.find_element_by_accessibility_id("minus").click()
        self.driver.find_element_by_id("digit_4").click()
        self.driver.find_element_by_accessibility_id("equals").click()
        resultado = self.driver.find_element_by_id("result").text
        self.assertEqual(resultado, "5")

    def test_multiplicacion(self):
        self.driver.find_element_by_id("digit_6").click()
        self.driver.find_element_by_accessibility_id("multiply").click()
        self.driver.find_element_by_id("digit_3").click()
        self.driver.find_element_by_accessibility_id("equals").click()
        resultado = self.driver.find_element_by_id("result").text
        self.assertEqual(resultado, "18")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
