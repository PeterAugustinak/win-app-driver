# coding=utf-8
"""Calculator page object"""


class Calculator:
    """POP for Calculator"""

    def __init__(self, driver):
        self.driver = driver

    def button(self, button):
        return self.driver.find_element_by_name(button)

    def get_display_result(self):
        text = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        return text.strip("Display is ").rstrip(" ").lstrip(" ")
