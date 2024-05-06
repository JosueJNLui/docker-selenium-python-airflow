from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from io import StringIO
import os

class Driver:

    def __init__(self, command_executor: str, url: str, options: str):

        self.driver = webdriver.Remote(
        command_executor = command_executor,
        options = options
        )
        self.driver.get(url)


    def get_table_by_id(self, id: str) -> pd.DataFrame:

        try:
            table = self.driver.find_element(By.ID, id).get_attribute('outerHTML')
            df = pd.read_html(StringIO(table))[0]
            return df
        except Exception as e:
            print(f'Error: {e}')

        finally:
            self.driver.quit()

class Utils:

    def save_data(df: pd.DataFrame, output_format: str, path: str):

        if output_format == 'csv':
            df.to_csv(path, index=False)

try:
    DOMAIN = os.environ["DOMAIN"]
except:
    DOMAIN = 'localhost'

driver = Driver(
    command_executor = f'http://{DOMAIN}:4444/wd/hub',
    url = 'https://www.w3schools.com/html/html_tables.asp',
    options = webdriver.FirefoxOptions()
)

df = driver.get_table_by_id('customers')

Utils.save_data(df, 'csv', './extracted_data/customers.csv')
