import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import pandas as pd

def mean_of_YTMs(date_as_string):
    driver = webdriver.Chrome()
    driver.get('https://in.investing.com/rates-bonds/india-10-year-bond-yield-historical-data')
    myElem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
    dateChoiceMain = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, r'#__next > div.md\:relative.md\:bg-white > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto.xl\:gap-10.xl\:px-10 > div.min-w-0 > div.mb-4.md\:mb-10 > div.sm\:flex.sm\:items-end.sm\:justify-between > div.relative.flex.items-center.md\:gap-6 > div > div')))
    
    dateChoiceMain.click()
    startingDatePicker = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, r'#__next > div.md\:relative.md\:bg-white > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto.xl\:gap-10.xl\:px-10 > div.min-w-0 > div.mb-4.md\:mb-10 > div.sm\:flex.sm\:items-end.sm\:justify-between > div.relative.flex.items-center.md\:gap-6 > div.absolute.right-0.top-\[42px\].z-5.inline-flex.flex-col.items-end.gap-4.rounded.border.border-solid.bg-white.p-4.shadow-secondary > div.flex.items-start.gap-3 > div:nth-child(1) > input')))
    
    startingDatePicker[0].clear()
    startingDatePicker[0].send_keys(date_as_string)

    applyButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, r'#__next > div.md\:relative.md\:bg-white > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto.xl\:gap-10.xl\:px-10 > div.min-w-0 > div.mb-4.md\:mb-10 > div.sm\:flex.sm\:items-end.sm\:justify-between > div.relative.flex.items-center.md\:gap-6 > div.absolute.right-0.top-\[42px\].z-5.inline-flex.flex-col.items-end.gap-4.rounded.border.border-solid.bg-white.p-4.shadow-secondary > div.flex.cursor-pointer.items-center.gap-3.rounded.bg-v2-blue.py-2\.5.pl-4.pr-6.shadow-button.hover\:bg-\[\#116BCC\]')))
    applyButton.click()

    table = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
    unformatted_data = table.text.splitlines()
    columns = unformatted_data[0].split(' ')
    columns.pop()

    data_list = [line.split(' ') for line in unformatted_data[1:]]
    df = pd.DataFrame(data=data_list, columns=columns)
    df['Price'] = pd.to_numeric(df['Price'])
    mean = df['Price'].mean()

    return mean
