from selenium import webdriver
import time
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('chromedriver.exe')

user = ''
driver.get(f"https://old.reddit.com/login")
search = driver.find_element_by_id('user_login')
search.send_keys(user)

search = driver.find_element_by_id('passwd_login')
search.send_keys('')

search.submit()
time.sleep(1)
driver.get(f"https://old.reddit.com/user/{user}/saved/")
images = driver.find_elements_by_class_name('expando')
# while True:
#     stored_pics = []
#     count = 0
#     for i in images:
#         try:
#             stored_pics.insert(count, i.get_attribute('data-cachedhtml').split()[8].split('"')[1])
#         except AttributeError:
#             pass
#         count += 1
#
#     for s in stored_pics:
#         print(s)
#         try:
#             name = s.split()[0].split('/')[3].split('.')[0]
#         except IndexError:
#             name = 'null'
#         try:
#             driver.get(s)
#             driver.get_screenshot_as_file(s)
#             driver.save_screenshot(f'pictures/{name}.png')
#             time.sleep(.5)
#         except InvalidArgumentException:
#             pass
#     try:
#         find_next = driver.find_element_by_class_name('next-button')
#         next_page = find_next.find_element_by_css_selector('a').get_attribute('href')
#         driver.get(next_page)
#         print('next page')
#     except NoSuchElementException:
#         print('no next page')
#         break
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL't')



