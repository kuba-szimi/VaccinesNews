import pandas as pd
import numpy as np
import plotly.express as px
import datetime
from Data_scrapper import DailyReportScrapper
from selenium import webdriver
import os


#Chrome driver options
options = webdriver.ChromeOptions() 
download_dir = "/home/kuba/MyProjects/VaccinesNews/VaccinesNews/Our_world_daily_reports"
options.add_experimental_option("prefs", {"download.default_directory": download_dir})

report_scrapper = DailyReportScrapper(options)

url_path = 'https://ourworldindata.org/grapher/share-people-vaccinated-covid?tab=chart'
report_scrapper.get_page(url_path)

download_tab_xpath = "/html[@class='js']/body[@class='StandaloneGrapherOrExplorerPage']/main/figure/div[@class='GrapherComponent']/div[@class='ControlsFooter']/div[@class='footerRowSingle'][2]/nav[@class='tabs']/ul/li[@class='tab clickable icon download-tab-button']/a"
download_button_xpath = "/html[@class='js']/body[@class='StandaloneGrapherOrExplorerPage']/main/figure/div[@class='GrapherComponent']/div[@class='DownloadTab']/div[@class='download-csv']/a[@class='btn btn-primary']"
report_scrapper.download_data(download_tab_xpath=download_tab_xpath, download_button_xpath=download_button_xpath)

current_filename = download_dir + '/share-people-vaccinated-covid.csv'
print(current_filename)
report_scrapper.adjust_filename(old_filename=current_filename)


today = datetime.datetime.today().strftime('%Y-%m-%d')
filename = f'Our_world_daily_reports/share-people-vaccinated-covid_{today}.csv'

df = pd.read_csv(filename)

df = df.drop(df.columns[-1], axis=1)
df = df.drop('Code', axis=1)

chosen_countries = ['Austria', 'Belgium', 'Czechia', 'Denmark', 'Estonia','Finland','France','Germany', 
                   'Hungary', 'Greece', 'Ireland', 'Italy', 'Lithuania','Netherlands', 'Norway', 
                    'Portugal', 'Poland', 'Romania', 'Serbia','Slovakia', 'Slovenia', 'Spain', 
                    'Sweden', 'Switzerland', 'Turkey', 'United Kingdom', 'United States']
                    

newest_dates = df.groupby('Entity').max()['Day']

df = df.join(newest_dates, on='Entity', rsuffix=' - Current')

df = df[(df['Entity'].isin(chosen_countries)) & (df['Day']==df['Day - Current'])]

df = df.sort_values(by='people_vaccinated_per_hundred', ascending=True)

fig = px.bar(df, x='people_vaccinated_per_hundred', y='Entity', 
            orientation='h', title='Share of people who received at least one dose of vaccine')

fig.update_xaxes(range=[0, 70])
fig.show()