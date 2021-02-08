# coding=utf-8

# standard library imports
from appium import webdriver


class Setup:
    """set up class for driver"""
    calcsession = None

    def setUp(self, app):
        """Setup method"""
        print("Setup is running ...")
        desired_caps = {"app": app}
        try:
            self.calcsession = webdriver.Remote(
                command_executor="http://127.0.0.1:4723",
                desired_capabilities=desired_caps)
            return self.calcsession
        except ConnectionRefusedError as e:
            print(f"EXCEPTION:  {e}")

    def tearDown(self):
        """Finisher method"""
        print("Tearing down ...")
        self.calcsession.quit()
