import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def set_window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_positive_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('myaumyau').press_enter()
    browser.element('[id="search"]').should(have.text('Page not Found'))
