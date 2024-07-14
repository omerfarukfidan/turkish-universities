import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# ChromeDriver'ı kullanarak Selenium'u başlatma
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.studyinturkiye.gov.tr/StudyinTurkey/Universities")

# Sayfanın tamamen yüklenmesini bekleme
time.sleep(10)  # Bu süreyi gerektiği gibi ayarlayabilirsiniz

# Sayfanın kaynak kodunu alma
page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")
university_list_container = soup.find("ul", id="myUL")
universities = university_list_container.find_all("li") if university_list_container else []

university_list = []

for uni in universities:
    categoryid = uni.get("categoryid")
    data_order = uni.get("data-order")

    div = uni.find("div", class_="okul-liste-detay")
    name = div.find("h4").get_text(strip=True) if div.find("h4") else "N/A"
    website_div = div.find("div", class_="city-okul-satir")
    website = website_div.find("a").get("href") if website_div and website_div.find("a") else "N/A"
    address_div = div.find("div", class_="city-okul-satir mb-3")
    address = address_div.find("span").get_text(strip=True) if address_div and address_div.find("span") else "N/A"
    details_link = div.find("a", class_="mobil-detail").get("href") if div.find("a", class_="mobil-detail") else "N/A"
    programs_link = div.find("a", class_="sehir-buton").get("href") if div.find("a", class_="sehir-buton") else "N/A"
    image_div = div.find("div", class_="sehir-okul-resim")
    image_url = image_div.get("style").split("url('")[1].split("')")[0] if image_div else "N/A"
    logo_img = uni.find("img")
    logo_url = logo_img.get("src") if logo_img else "N/A"

    university_list.append({
        "categoryid": categoryid,
        "data_order": data_order,
        "name": name,
        "website": website,
        "address": address,
        "details_link": details_link,
        "programs_link": programs_link,
        "image_url": image_url,
        "logo_url": logo_url
    })

# CSV dosyasına yazma
with open('universities.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["CategoryID", "DataOrder", "Name", "Website", "Address", "DetailsLink", "ProgramsLink", "ImageURL", "LogoURL"])
    for uni in university_list:
        writer.writerow([
            uni["categoryid"], uni["data_order"], uni["name"], uni["website"],
            uni["address"], uni["details_link"], uni["programs_link"], uni["image_url"], uni["logo_url"]
        ])

print("Data has been written to universities.csv")
