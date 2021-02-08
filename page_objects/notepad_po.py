# coding=utf-8

class Notepad:
    """Page object for Notepad"""

    def __init__(self, driver):
        self.driver = driver

    def window(self, button):
        """Use: Maximize, Minimize, Close"""
        return self.driver.find_element_by_name(button)

    def menu(self, menu):
        """Use: File, Edit, Format, View, Help"""
        return self.driver.find_element_by_name(menu)

    def text_area(self):
        """Text area location"""
        return self.driver.find_element_by_name("Text Editor")

    def exit_dialog(self, button):
        """Use: Save, Don't Save, Cancel"""
        return self.driver.find_element_by_name(button)
