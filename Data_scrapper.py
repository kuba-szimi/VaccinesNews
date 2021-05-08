# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os


class DailyReportScrapper():

    def __init__(self, driver_options):
        self.driver_options = driver_options
        self.driver = webdriver.Chrome(chrome_options=self.driver_options)
        #self.download_tab_xpath = "/html[@class='js']/body[@class='StandaloneGrapherOrExplorerPage']/main/figure/div[@class='GrapherComponent']/div[@class='ControlsFooter']/div[@class='footerRowSingle'][2]/nav[@class='tabs']/ul/li[@class='tab clickable icon download-tab-button']/a"
        #self.download_button_xpath = "/html[@class='js']/body[@class='StandaloneGrapherOrExplorerPage']/main/figure/div[@class='GrapherComponent']/div[@class='DownloadTab']/div[@class='download-csv']/a[@class='btn btn-primary']"

    def get_page(self, exec_path):
        self.driver.get(exec_path)
    

    def download_data(self, download_tab_xpath, download_button_xpath):
        download_tab = self.driver.find_element_by_xpath(download_tab_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", download_tab)
        self.driver.execute_script("arguments[0].click();", download_tab)
        self.driver.execute_script("scrollBy(0,-200);")
        download_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, download_button_xpath))) 
        download_button.click()

    
    def adjust_filename(self, old_filename):
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        new_filename = old_filename.replace(".csv", f"_{today}.csv")
        os.rename(old_filename, new_filename)


    def __del__(self):
        self.driver.close()


"""
url_path = 'https://ourworldindata.org/grapher/share-people-vaccinated-covid?tab=chart'

#Chrome driver options
options = webdriver.ChromeOptions() 

# Set the download Path
download_dir = "/home/kuba/MyProjects/VaccinesNews/VaccinesNews/Our_world_daily_reports"
options.add_experimental_option("prefs", {"download.default_directory": download_dir})

# Open Chrome
driver = webdriver.Chrome(chrome_options=options)


# Open URL
driver.get(url_path)

# Click on Download tab
download_tab = driver.find_element_by_xpath("/html[@class='js']/body[@class='StandaloneGrapherOrExplorerPage']/main/figure/div[@class='GrapherComponent']/div[@class='ControlsFooter']/div[@class='footerRowSingle'][2]/nav[@class='tabs']/ul/li[@class='tab clickable icon download-tab-button']/a")
driver.execute_script("arguments[0].scrollIntoView();", download_tab)
driver.execute_script("arguments[0].click();", download_tab)
#download_tab.click()

#Scroll up to make the download button visible
driver.execute_script("scrollBy(0,-200);")

# Click on Download Button
download_path = "/html[@class='js']/body[@class='StandaloneGrapherOrExplorerPage']/main/figure/div[@class='GrapherComponent']/div[@class='DownloadTab']/div[@class='download-csv']/a[@class='btn btn-primary']"
download_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, download_path))) 
download_button.click()
driver.close()

today = datetime.datetime.today().strftime('%Y-%m-%d')
old_filename = os.path.dirname(__file__) + '/Our_world_daily_reports/share-people-vaccinated-covid.csv'
new_filename = old_filename.replace(".csv", f"_{today}.csv")
#new_filename = f'Our_world_daily_reports\share-people-vaccinated-covid_{today}.csv'
os.rename(old_filename, new_filename)

"""