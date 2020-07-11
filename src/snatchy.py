import time
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo

import requests
from requests.exceptions import MissingSchema
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException


def no_uorp():
    showinfo('Username or Password Error', 'Enter in reddit info and try again.')

def no_path():
    showinfo('No Path!', 'Select a path you would like to save your files in.')

def page_not_found():
    showinfo('Page Not Found', 'Make sure your username and password information is correct.')

def snatch_snatch():
    user = urname_text.get()
    password = pass_text.get()
    if user == '' or password == '':
        no_uorp()
        return None
    elif path_text.get() == '':
        no_path()
        return None
    else:
        pass
    page_count = 0
    driver = webdriver.Chrome('chromedriver.exe')
    driver.minimize_window()

    driver.get(f"https://old.reddit.com/login")

    search = driver.find_element_by_id('user_login')
    search.send_keys(user)

    search = driver.find_element_by_id('passwd_login')
    search.send_keys(password)

    search.submit()

    time.sleep(1)
    driver.get(f"https://old.reddit.com/user/{user}/saved/")
    

    while True:
        stored_pics = []
        count = 0
        images = driver.find_elements_by_class_name('expando')

        for i in images:
            try:
                stored_pics.insert(count, i.get_attribute('data-cachedhtml').split()[8].split('"')[1])
            except AttributeError:
                pass
            except IndexError:
                pass
            count += 1

        for s in stored_pics:
            print(s)
            try:
                name = s.split()[0].split('/')[3].split('.')[0]
                type = s.split()[0].split('/')[3].split('.')[1]
                if 'png' in type or 'jpg' in type:
                    request = requests.get(s)
                    file = open(f'{path_text.get()}/{name}.png', 'wb')
                    file.write(request.content)
                    file.close()
                elif 'gifv' in type or 'gif' in type:
                    request = requests.get(s)
                    file = open(f'{path_text.get()}/{name}.gif', 'wb')
                    file.write(request.content)
                    file.close()
                else:
                    pass
            except InvalidArgumentException:
                pass
            except MissingSchema:
                pass
            except IndexError:
                pass

        try:
            find_next = driver.find_element_by_class_name('next-button')
            next_page = find_next.find_element_by_css_selector('a').get_attribute('href')
        except NoSuchElementException:
            break
        except NameError:
            break
        page_count += 1
        print("PAGE COUNT" + str(page_count))
        driver.get(next_page)

    time.sleep(1)
    driver.quit()


def path():
    root.directory = filedialog.askdirectory()
    path_text.insert(1, root.directory)


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
root.geometry('300x200')
root.title('Snatchy')

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='reddit.png'))

urname_label = tk.Label(text='User Name')
urname_label.grid(row=1, column=1)
urname_text = tk.Entry(root)
urname_text.grid(row=2, column=1)

pass_label = tk.Label(text='Password')
pass_label.grid(row=3, column=1)
pass_text = tk.Entry(root, show='*')
pass_text.grid(row=4, column=1)

pass_label = tk.Label(text='Path')
pass_label.grid(row=5, column=1)
path_text = tk.Entry(root, width=50)
path_text.grid(row=6, column=1)

path_btn = tk.Button(root, height=1, width=20, text="Choose Path", command=path)
path_btn.grid(row=7, column=1)

save_btn = tk.Button(root, height=1, width=20, text="Snatch!", command=snatch_snatch)
save_btn.grid(row=8, column=1)

root.mainloop()
