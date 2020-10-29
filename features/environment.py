from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome("../resources/chromedriver_86")

def after_all(context):
    context.browser.quit()
