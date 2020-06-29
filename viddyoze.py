import os
import time
from driver import driver, URL
from helpers import click, key, wait_for_download
from selenium.webdriver.support.wait import WebDriverWait


def login():
    key('#user_email', os.getenv('VIDDYOZE_USERNAME'))
    key('#user_password', os.getenv('VIDDYOZE_PASSWORD'))

    click('#login')


def render_template_by_name(name, webpage, logo_path):
    driver.get(URL + '?filters%5Bname%5D=' + name.replace(' ', '+'))

    template = driver.find_element_by_css_selector(
        'body > div.pusher > div.ui.container > div.ui.three.stackable.grid.template-list > div > div > div.preview.template-card')

    click(template)
    time.sleep(4)

    click('a[href*="/new"]')
    time.sleep(4)

    total_categories = len(driver.find_elements_by_css_selector(
        'body > div.pusher > header > div.ui.fluid.second-header.container.customize-container > div > div > a'))

    print('Total Categories: ' + str(total_categories))
    for _ in range(total_categories):
        current_category = driver.find_element_by_css_selector(
            'a.item.active.hovered').text
        print(current_category)
        if (current_category == 'Texts'):
            texts = driver.find_elements_by_css_selector(
                'input[name*="render[texts]"]')
            print(texts)
            for text in texts:
                key(text, webpage)
            click('a[title="Next Step"]')
        elif (current_category == 'Colors'):
            click('a[title="Next Step"]')
        elif (current_category == 'Images'):
            images = driver.find_elements_by_css_selector(
                'input[name*="render[images]"]')
            for image in images:
                key(image, os.getcwd() + '/' + logo_path)
            click('a[title="Next Step"]')
        elif (current_category == 'Create'):
            click("//*[contains(text(), 'Create Your Video')]")
        time.sleep(4)

    print('Rendering...')

    wait = WebDriverWait(driver, 60*60*24)
    wait.until(lambda driver: "/download" in driver.current_url)

    wait_for_download(os.getcwd() + '/renders')


def render_all_logo_templates():
    for page in range(1, 5):
        for template_index in range(15):
            driver.get(URL + '/' + str(page) +
                       '?filters%5Bcategory%5D=3&sort%5Bfield%5D=&filters%5Bname%5D=&filters%5Btag%5D=')

            templates = driver.find_elements_by_css_selector(
                'body > div.pusher > div.ui.container > div.ui.three.stackable.grid.template-list > div > div > div.preview.template-card')

            click(templates[template_index])
            time.sleep(4)

            click('a[href*="/new"]')
            time.sleep(4)

            total_categories = len(driver.find_elements_by_css_selector(
                'body > div.pusher > header > div.ui.fluid.second-header.container.customize-container > div > div > a'))

            for i in range(total_categories):
                current_category = driver.find_element_by_css_selector(
                    'a.item.active').text
                if (current_category == 'Texts'):
                    texts = driver.find_elements_by_css_selector(
                        'input[name*="render[texts]"]')
                    for index, text in enumerate(texts):
                        key(text, f"(Text #{index + 1})")
                    click('a[title="Next Step"]')
                elif (current_category == 'Colors'):
                    click('a[title="Next Step"]')
                elif (current_category == 'Images'):
                    images = driver.find_elements_by_css_selector(
                        'input[name*="render[images]"]')
                    for image in images:
                        key(image, '/Users/simon/Dev/viddyoze-bot/assets/logo-black.png')
                    click('a[title="Next Step"]')
                elif (current_category == 'Create'):
                    click("//*[contains(text(), 'Create Your Video')]")
                time.sleep(4)

            print('Rendering...')

            wait = WebDriverWait(driver, 60*60*24)
            wait.until(lambda driver: "/download" in driver.current_url)
