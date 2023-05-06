
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
        element = wait(driver, 10).until(EC.title_contains(title))
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
