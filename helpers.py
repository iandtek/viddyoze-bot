from driver import driver
from selenium.webdriver.common.keys import Keys
import time
import os
import glob

video_prefix = "VIDDYOZE-"


def click(selector):
    if type(selector) == str:
        print('Clicking: ' + selector)
        if selector[0] == '/':
            driver.find_element_by_xpath(selector).click()
        else:
            driver.find_element_by_css_selector(selector).click()
    else:
        print('Clicking: ' + str(selector))
        selector.click()


def key(selector, text):
    if type(selector) == str:
        print('Sending ' + text + ' to ' + selector)
        if selector[0] == '/':
            driver.find_element_by_xpath(selector).send_keys(text)
        else:
            driver.find_element_by_css_selector(selector).send_keys(text)
    else:
        print('Sending ' + text + ' to ' + str(selector))
        selector.send_keys(text)


def enter(selector):
    if type(selector) == str:
        print('Sending ' + Keys.ENTER + ' to ' + selector)
        if selector[0] == '/':
            driver.find_element_by_xpath(selector).send_keys(Keys.ENTER)
        else:
            driver.find_element_by_css_selector(selector).send_keys(Keys.ENTER)
    else:
        print('Sending ' + Keys.ENTER + ' to ' + str(selector))
        selector.send_keys(Keys.ENTER)


def wait_for_download(path):
    while not glob.glob(path + '/' + video_prefix + '*'):
        time.sleep(1)
        print('Downloading...')
    if os.path.isfile(path):
        print('Downloaded!')
        rename()
        return True
    else:
        return False


def rename():
    print('Renaming files...')
    for dpath, dnames, fnames in os.walk(os.getcwd() + '/' + 'renders'):
        for f in fnames:
            os.chdir(dpath)
            if f.startswith(video_prefix):
                print("|--- " + f)
                os.rename(f, f.replace(video_prefix, ''))
