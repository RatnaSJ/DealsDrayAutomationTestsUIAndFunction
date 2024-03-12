import datetime

import pytest
from selenium import webdriver


resolutions = {
    'Desktop': ['1920x1080', '1366x768', '1536x864'],
    'Mobile': ['360x640', '414x896', '375x667']
}


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    yield driver
    driver.quit()


def test_screenshots(driver):
    driver.get("https://www.getcalley.com/page-sitemap.xml")

    links = ['https://www.getcalley.com/',
             'https://www.getcalley.com/calley-call-from-browser/',
             'https://www.getcalley.com/calley-pro-features/',
             'https://www.getcalley.com/best-auto-dialer-app/',
             'https://www.getcalley.com/how-calley-auto-dialer-app-works/'
             ]
    for resolution_type, resolution_list in resolutions.items():
        for resolution in resolution_list:
            width, height = map(int, resolution.split('x'))
            driver.set_window_size(width, height)

            # Iterate links
            for i, link in enumerate(links, start=1):
                driver.get(link)

                assert 'Calley' in driver.title

                now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                screenshot_name = f"{driver.capabilities['browserName']}_{resolution_type}_{resolution}_link_{i}_{now}.png"
                screenshot_path = f"../Screenshots/{screenshot_name}"
                driver.save_screenshot(screenshot_path)



