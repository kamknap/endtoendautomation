from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get("https://thetestingworld.com/testings/")
    
def after_scenario(context, scenario):
    context.driver.close()