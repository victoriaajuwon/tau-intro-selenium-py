"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for phrase
    search_page.search(phrase)

    # Then the search result title contains "panda"
    # assert PHRASE in result_page.title()
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    # WebDriverWait(driver, 10).until(EC.title_contains(PHRASE))

    # Then the search result query is phrase
    assert phrase == result_page.search_input_values()

    # And the search result links pertain to phrase
    # for title in result_page.result_link_titles():
    #     assert PHRASE.lower() in title.lower()

    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains phrase
    # (Putting this assertion last guarantees that the page title will be ready)
    assert phrase in result_page.title()
