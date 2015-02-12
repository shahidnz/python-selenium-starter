from tests.base_test import BaseTest


class Test(BaseTest):
    """An example test to show how to structure your tests"""
    def __init__(self, driver, base_url):
        super(Test, self).__init__(driver, base_url)

    def run(self):
        self.driver.get(self.base_url)
        if "Google" not in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("BrowerStack")
        elem.submit()
        print self.driver.title
        self.passed("example_a.py")
        # No need to quit driver at the end of the test. The run.py file will
        # handle that
