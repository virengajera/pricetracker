from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pickle

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#driver.get("https://www.amazon.de/Google-Pixel-Entsperrtes-Android-Smartphone-Weitwinkelobjektiv/dp/B0BDJFKY7B/ref=sr_1_1_sspa?keywords=google+pixel+8&qid=1671905403&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
#driver.get("https://www.amazon.de/SONAX-Winter-Scheibenwaschwasser-mischbereit-schlierenfrei-Antikalk-Effekt/dp/B001050QSA/ref=zg-bs_automotive_sccl_2/262-6899482-3568810?pd_rd_w=kHVZD&content-id=amzn1.sym.a6d00793-4052-45a8-b02b-f64c7eefbdaa&pf_rd_p=a6d00793-4052-45a8-b02b-f64c7eefbdaa&pf_rd_r=QGX7Z236JPZHJENXSZN5&pd_rd_wg=LLEYv&pd_rd_r=cece86aa-59a5-4b5a-a5d2-758a24850a66&pd_rd_i=B001050QSA&th=1")

#content = driver.page_source

#soup = BeautifulSoup(content)

def scrapping(link):
    soup = ""
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")
    
    result = soup.find('span',attrs={'class':'a-offscreen'}).text
    print(result)


if __name__=='__main__':

    link = input('Please enter the link of product link :')
    scrapping(link)