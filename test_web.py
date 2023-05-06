
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
url = "https://www.mozilla.org/en-US/"
title = "Internet for people"


@pytest.fixture
def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        wait(driver, 10).until(EC.title_contains(title))
    except Exception as e:
        print(e)
    yield driver

    driver.quit()


def test_web_link(webFix):
    webFix.find_element(By.LINK_TEXT, 'Learn more').click()
    title = webFix.title
    assert "Firefox" in title


def test_web_links(webFix):
    links = webFix.find_elements(By.TAG_NAME, "a")
    for link in links[:3]:
        href = link.get_attribute("href")
        assert 'mozilla' in href or 'youtu' in href or 'spotify' in href


@pytest.mark.test3
def test_account_form(webFix):
    sample_email = "test@gmail.com"
    webFix.find_element(By.LINK_TEXT, 'Learn more').click()
    try:
        wait(webFix, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'mzp-c-form-title')))
    except Exception as e:
        print(e)
    text_input = webFix.find_element(By.ID, 'fxa-email-field')
    text_input.send_keys(sample_email)
    webFix.find_element(By.ID, 'fxa-email-form-submit').click()

    pre_fill_email = None
    try:
        pre_fill_email = wait(webFix, 3).until(
            EC.presence_of_element_located((By.ID, 'prefillEmail')))
    except Exception as e:
        print(e)
    assert sample_email in pre_fill_email.text
