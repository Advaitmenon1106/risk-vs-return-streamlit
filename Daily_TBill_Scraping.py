from selenium import webdriver as wd
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt

def get_todays_rf():
    url = "https://in.investing.com/rates-bonds/india-10-year-bond-yield-historical-data"

    options = ChromeOptions()

    driver = wd.Chrome(options=options)
    driver.get(url=url)
    el = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, r'#__next > div.md\:relative.md\:bg-white > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto.xl\:gap-10.xl\:px-10 > div.min-w-0 > div.flex.flex-col.gap-6.md\:gap-0 > div.flex.gap-6 > div.flex-1 > div.mb-3.flex.flex-wrap.items-center.gap-x-4.gap-y-2.md\:mb-0\.5.md\:gap-6 > div.text-5xl\/9.font-bold.text-\[\#232526\].md\:text-\[42px\].md\:leading-\[60px\]')))

    print(el.text)