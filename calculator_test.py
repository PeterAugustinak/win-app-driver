# coding=utf-8
import unittest
from appium import webdriver


class CalculatorTest(unittest.TestCase):
    calcsession = None
    calcresult = None

    def setUp(self):
        """Setup method"""
        print("Setup is running ...")
        desired_caps = {"app": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"}
        self.calcsession = webdriver.Remote(
            command_executor = "http://127.0.0.1:4723",
            desired_capabilities=desired_caps
        )

    def tearDown(self):
        """Finisher method"""
        print("Tearing down ...")
        self.calcsession.quit()

    def test_add(self):
        """Add test"""
        print("Adding Test")

    def test_subtraction(self):
        """Subtraction test"""
        print("Subtraction Test")

    def test_division(self):
        """Division test"""
        print("Division Test")

    def test_multiplication(self):
        """Multiplication test"""
        print("Multiplication Test")

