from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from io import StringIO
import os

class Driver:

    def __init__(self, command_executor: str, url: str, options: str):
        """
        Initializes an instance of the Driver class.

        Args:
            command_executor (str): The URL of the remote WebDriver server.
            url (str): The URL to navigate to upon initializing the WebDriver.
            options (str): Options for configuring the WebDriver.
        """

        self.driver = webdriver.Remote(
            command_executor = command_executor,
            options = options
        )
        self.driver.get(url)
    
    def get_element_text(self, locator: str, value: str) -> str:
        """
        Finds text content of an HTML element based on locator and value.
            
        Args:
            locator (str): The type of locator, such as 'ID', 'CSS_SELECTOR', etc.
            value (str): The value of the locator.

        Returns:
            str or None: The text content of the found HTML element, or None if not found.
        """

        try:
            if locator.upper() == "ID":
                element = self.driver.find_element(By.ID, value)

            if locator.upper() == "CSS_SELECTOR":
                element = self.driver.find_element(By.CSS_SELECTOR, value)

            if locator.upper() == "XPATH":
                element = self.driver.find_element(By.XPATH, value)
            
            return element.text
        except Exception as e:
            print(f'Error: {e}')

    def get_elements(self, locator_values: list[dict]) -> dict:
        """
        Retrieves text content of HTML elements based on locator-value pairs and returns a dictionary.

        Args:
            locator_values (list[dict]): A list of dictionaries where each dictionary contains
                locator (str): The type of locator, such as 'ID', 'CSS_SELECTOR', etc.
                value (str): The value of the locator.
                name (str): A name to associate with the retrieved text content.

        Returns:
            dict: A dictionary where keys are the names of elements and values are their text content.
        """

        return {
            element['name']: self.get_element_text(
                element['locator'],
                element['value']
            ) for element in locator_values
        }
    
    def quit_session(self):
        """
        Quits the WebDriver session.
        """

        self.driver.quit()

try:
    DOMAIN = os.environ["DOMAIN"]
except:
    DOMAIN = 'localhost'

driver = Driver(
    command_executor = f'http://{DOMAIN}:4444/wd/hub',
    url = 'https://investing.com/crypto/bitcoin',
    options = webdriver.FirefoxOptions()
)

locator_values = [
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]',
        'name'   : 'bitcoin_price'
    },
    {
        'locator': 'XPATH',
        'value'  : '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[4]/div[2]/div[2]/div[2]',
        'name'   : 'techinical'
    },
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/time',
        'name'   : 'time'
    },
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/dl[1]/div[8]/dd',
        'name'   : 'ranking'
    },
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/dl[2]/div[1]/dd/span/span[2]',
        'name'   : 'chg_7d'
    },
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/dl[2]/div[2]/dd/span/span[2]',
        'name'   : 'chg_1m'
    },
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/dl[2]/div[3]/dd/span/span[2]',
        'name'   : 'chg_1y'
    },
    {
        'locator': 'XPATH',
        'value'  : '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/dl[2]/div[4]/dd/span/span[2]',
        'name'   : 'ytd'
    }
]

teste = driver.get_elements(locator_values)

for name, value in teste.items():
    print(name, value)

driver.quit_session()
