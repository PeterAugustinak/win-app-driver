# coding=utf-8

# local library imports
from setup import Setup
from calculator_po import Calculator as Calc

import unittest


class CalculatorTest(unittest.TestCase):
    """Test Scenario for Calculator"""

    setup = Setup()
    calc = None

    def setUp(self):
        calcsession = self.setup.setUp()
        self.calc = Calc(calcsession)

    def tearDown(self):
        self.setup.tearDown()

    def test_addition(self):
        """Addition test"""

        print("Adding Test")
        self.calc.button("One").click()
        self.calc.button("Nine").click()
        self.calc.button("Plus").click()
        self.calc.button("Three").click()
        self.calc.button("Equals").click()

        self.assertEqual(self.calc.get_display_result(), "22")

    def test_subtraction(self):
        """Subtraction test"""

        print("Subtraction Test")
        self.calc.button("One").click()
        self.calc.button("Nine").click()
        self.calc.button("Minus").click()
        self.calc.button("Three").click()
        self.calc.button("Equals").click()

        self.assertEqual(self.calc.get_display_result(), "16")



    # # BY CLASS_NAME
    # def choose_calculator(self, locator):
    #     print(f"Selected calc: {locator}")
    #
    #     # open the hamburger combo
    #     self.calcsession.find_element_by_accessibility_id("TogglePaneButton").click()
    #     # read all items in combo into the list
    #     lst_of_elements_in_menu = self.calcsession.find_elements_by_class_name(
    #         "Microsoft.UI.Xaml.Controls.NavigationViewItem")
    #
    #     print(f"Calculator combo elements: {len(lst_of_elements_in_menu)} -> "
    #           f"{', '.join([item.get_attribute('AutomationId') for item in lst_of_elements_in_menu])}")
    #
    #     # find item by locator inputed and click on it
    #     for item in lst_of_elements_in_menu:
    #         if item.get_attribute("AutomationId") == locator:
    #             item.click()
    #             # if locator was found, stop looking further
    #             break
    #
    #     # TODO: How to add break?
    #     # [item.click() for item in lst_of_elements_in_menu if item.get_attribute("AutomationId") == locator]
    #
    # def test_choose_another_calc(self):
    #     print(f"Selecting another calc ...")
    #     self.choose_calculator("Scientific")
    #
    # # BY XPATH
    # def choose_calculator_xpath(self, locator):
    #     print(f"Selected calc: {locator}")
    #
    #     # open the hamburger combo
    #     self.calcsession.find_element_by_accessibility_id("TogglePaneButton").click()
    #     # read all items in combo into the list
    #     lst_of_elements_in_menu = self.calcsession.find_elements_by_xpath("//ListItem")
    #
    #     print(f"Calculator combo elements: {len(lst_of_elements_in_menu)} -> "
    #           f"{', '.join([item.get_attribute('Name') for item in lst_of_elements_in_menu])}")
    #
    #     # find item by locator inputed and click on it
    #     for item in lst_of_elements_in_menu:
    #         if item.get_attribute("Name") == locator:
    #             item.click()
    #             # if locator was found, stop looking further
    #             break
    #
    # def test_choose_another_calc_xpath(self):
    #     print(f"Selecting another calc ...")
    #     self.choose_calculator_xpath("Scientific Calculator")
    #
    # # BY XPATH SIMPLE
    # def choose_calculator_xpath_simple(self, locator):
    #     print(f"Selected calc: {locator}")
    #
    #     # open the hamburger combo
    #     self.calcsession.find_element_by_accessibility_id("TogglePaneButton").click()
    #     self.calcsession.find_element_by_xpath(f"//ListItem[contains(@Name, \"{locator}\")]").click()
    #
    # def test_choose_another_calc_xpath_simple(self):
    #     print(f"Selecting another calc ...")
    #     self.choose_calculator_xpath_simple("Scientific Calculator")
