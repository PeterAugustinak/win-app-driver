# coding=utf-8

# local library imports
from helpers.setup import Setup
from page_objects.notepad_po import Notepad as Note
# external library imports
import unittest
from selenium.webdriver.common.action_chains import ActionChains as Action
from selenium.webdriver.common.keys import Keys
import time


class NotepadTest(unittest.TestCase):
    """Test Scenario for Notepad"""

    setup = Setup()
    notepad_session = None
    notepad = None
    action = None
    app = "c:\\windows\\system32\\notepad.exe"

    def setUp(self):
        self.notepad_session = self.setup.setUp(self.app)
        self.notepad = Note(self.notepad_session)
        self.action = Action(self.notepad_session)

    def tearDown(self):
        self.setup.tearDown()

    def test_01(self):
        print("Test Case 01")
        input_text = "Windriver is awesome?"
        self.notepad.text_area().send_keys(input_text)
        text_area = self.notepad.text_area()
        self.assertEqual(text_area.text, input_text)

        self.notepad.text_area().send_keys(Keys.ALT, Keys.F4)
        self.notepad.exit_dialog("Cancel").click()
        self.notepad.text_area().send_keys(Keys.ALT, Keys.F4)
        self.notepad.exit_dialog("Don't Save").click()

    def test_02(self):
        print("Test Case 02")
        self.notepad.menu("File").click()
        time.sleep(3)

    def test_03(self):
        print("Test Case 03")
        self.notepad.window("Minimize").click()
        time.sleep(3)

