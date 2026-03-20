import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def start_parser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    url = "https://www.ozon.ru/search/?text=скидки"
    driver.get(url)

    time.sleep(5)

    products = driver.find_elements(By.CSS_SELECTOR, "div.tile-root")

    results = []

    for product in products:
        try:
            name = product.find_element(By.CSS_SELECTOR, "span.tsBody500Medium").text
            
            price_text = product.find_element(By.CSS_SELECTOR, "span.tsHeadline500Medium").text
            price = int(price_text.replace("₽", "").replace(" ", ""))

            link = product.find_element(By.TAG_NAME, "a").get_attribute("href")

            try:
                bonus_text = product.find_element(By.XPATH, ".//*[contains(text(),'балл')]").text
                bonus = int(''.join(filter(str.isdigit, bonus_text)))
            except:
                continue

            percent = (bonus / price) * 100

            if percent > 100:
                results.append({
                    "name": name,
                    "price": price,
                    "bonus": bonus,
                    "percent": round(percent, 1),
                    "link": link
                })

        except:
            continue

    driver.quit()
    return results
