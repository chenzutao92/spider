from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/signup?next=%2F")

browser.find_element_by_css_selector("#root > div > main > div > div > div > div.SignContainer-inner > div.SignContainer-switch > span").click()

browser.find_element_by_css_selector("#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > div.SignFlow-account > div.SignFlowInput.SignFlow-accountInputContainer > div.SignFlow-accountInput.Input-wrapper > input").send_keys("18924220519")
#browser.find_element_by_css_selector(".SignFlow-passwordInput input[name='password']").send_keys("chen123456789")
browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys("chen123456789")
browser.find_element_by_css_selector("#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > button").click()