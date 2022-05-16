import pytest
from selenium import webdriver
from datetime import datetime
from utilites.ReadConfig import ReadConfig
from utilites.logger import Logger

logger =Logger.get_logger()

@pytest.fixture()
def setup(request):
    url = ReadConfig.get_app_url()
    driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')
    logger.info(f'Opening {driver.name} browser')
    driver.get(url)
    logger.info(f'Navigating to {url}')

    def teardown():
        image_name = fr".\screenshots\image-{datetime.today().strftime('%m%d%y-%H%M%S')}.png"
        driver.save_screenshot(image_name)
        logger.info(f'Taking a screenshot {image_name}')
        logger.info(f'Closing the browser')
        driver.quit()
    request.addfinalizer(teardown)
    return driver

def pytest_configure(config):
    config._metadata['Project Name'] = 'Homework'
    config._metadata['Tester'] = 'Elena Lysenko'
