from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver=driver
    email=(By.NAME, "email")
    password=(By.CSS_SELECTOR, "input[type='password']")
    loginbutton=(By.NAME, "login")
    home=(By.CSS_SELECTOR, "span[class='l9j0dhe7']")
    blanktext=(By.CSS_SELECTOR, "div[class='_9ay7']")

    def getemail(self):
        return self.driver.find_element(*LoginPage.email)
    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)
    def clickloginbutton(self):
        return self.driver.find_element(*LoginPage.loginbutton)
    def Home(self):
        return self.driver.find_element(*LoginPage.home)
    def getblanktext(self):
        return self.driver.find_element(*LoginPage.blanktext)
