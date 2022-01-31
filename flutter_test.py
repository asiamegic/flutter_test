from appium import webdriver
import allure


@allure.story('Story/Requirement Name')
@allure.feature('Feature Name')
class AppiumTest:

    def __init__(self):
        self.dc = {}
        self.driver = None

    @allure.testcase("Test Case name")
    @allure.step("Open application")
    def setUp(self):
        self.dc['app'] = "C:\\Users\Artem\\Desktop\\flutter-test.apk"
        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'emulator-5554'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)

    @allure.step("Testing")
    def testFirstAutomation(self):
        self.driver.implicitly_wait(10)
        for _ in range(5):
            self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='3']").click()
            self.driver.implicitly_wait(1)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='1']").click()
        for _ in range(5):
            self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='3']").click()
            self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@class='android.view.View' and @index='3']")

        for _ in range(5):
            self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='4']").click()
            self.driver.implicitly_wait(1)
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='1']").click()
        for _ in range(3):
            self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='4']").click()
            self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[@class='android.widget.Button' and @index='5']").click()



    @allure.step("Stopping")
    def tearDown(self):
        self.driver.quit()


def test_main():
    a = AppiumTest()
    a.setUp()
    a.testFirstAutomation()
    a.tearDown()
