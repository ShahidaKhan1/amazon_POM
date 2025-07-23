import sys
import os

# Add parent directory to path to allow imports
sys.path.append(os.path.abspath(".."))

from POM.search_results_page import SearchResultsPage

def test_searchresultpage(browser_setup):
    search_obj = SearchResultsPage(browser_setup)
    search_obj.select_first_result()