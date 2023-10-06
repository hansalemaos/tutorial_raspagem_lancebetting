import re
from time import sleep

from seleniumbase import Driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from PrettyColorPrinter import add_printer

add_printer(1)


def obter_dataframe(query="*"):
    df = pd.DataFrame()
    while df.empty:
        df = get_df(
            driver,
            By,
            WebDriverWait,
            expected_conditions,
            queryselector=query,
            with_methods=True,
        )
    return df


driver = Driver(uc=True)
driver.get("https://www.lancebetting.com/sports-hub/football/brazil/brasileirao_serie_a")
while True:
    try:
        df = obter_dataframe(query='li')
        df=df.loc[ (df.aa_classList=='KambiBC-sandwich-filter__event-list-item')].aa_innerText.str.split(r'[\r\n]',regex=True,expand=True)[range(7)].reset_index(drop=True).rename( columns={0: 'dia', 1: 'hora', 2: 'team1_nome', 3: 'team2_nome', 4: 'team1', 5: 'empate', 6:'team2'}).assign(team1=lambda q:q.team1.str.replace(',', '.'),team2=lambda q:q.team2.str.replace(',', '.'),empate=lambda q:q.empate.str.replace(',', '.')).astype({'team1': 'Float64', 'empate': 'Float64', 'team2': 'Float64'})
        break
    except Exception as e:
        print(e)
        sleep(1)
