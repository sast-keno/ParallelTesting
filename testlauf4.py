from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


ffoptions = webdriver.FirefoxOptions()
ffoptions.add_argument("--headless")

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--headless")


# shopping cart - backpack 
def test_1_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Backpack" in shopping_cart_item
    driver.quit()


# shopping cart - backpack 
def test_1_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Backpack" in shopping_cart_item
    driver.quit()


# shopping cart - bike light
def test_2_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bike Light" in shopping_cart_item
    driver.quit()


# shopping cart - bike light
def test_2_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bike Light" in shopping_cart_item
    driver.quit()


# shopping cart - bolt t-shirt
def test_3_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bolt T-Shirt" in shopping_cart_item
    driver.quit()


# shopping cart - bolt t-shirt
def test_3_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bolt T-Shirt" in shopping_cart_item
    driver.quit()


# shopping cart - Fleece Jacket
def test_4_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Fleece Jacket" in shopping_cart_item
    driver.quit()


# shopping cart - Fleece Jacket
def test_4_chrome():
    driver = webdriver.Chrome(options=chromeoptions)    
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Fleece Jacket" in shopping_cart_item
    driver.quit()


# shopping cart - Onesie
def test_5_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Onesie" in shopping_cart_item
    driver.quit()


# shopping cart - Onesie
def test_5_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Onesie" in shopping_cart_item
    driver.quit()

# shopping cart - test.allthethings()-t-shirt-(red)
def test_6_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Test.allTheThings() T-Shirt (Red)" in shopping_cart_item
    driver.quit()


# shopping cart - test.allthethings()-t-shirt-(red)
def test_6_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Test.allTheThings() T-Shirt (Red)" in shopping_cart_item
    driver.quit()

# title
def test_login_and_title_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    assert driver.title == "Swag Labs"
    driver.quit()


# title
def test_login_and_title_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    assert driver.title == "Swag Labs"
    driver.quit()


# shopping cart - backpack 
def test_7_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Backpack" in shopping_cart_item
    driver.quit()


# shopping cart - backpack 
def test_7_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Backpack" in shopping_cart_item
    driver.quit()


# shopping cart - bike light
def test_8_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bike Light" in shopping_cart_item
    driver.quit()


# shopping cart - bike light
def test_8_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bike Light" in shopping_cart_item
    driver.quit()


# shopping cart - bolt t-shirt
def test_9_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bolt T-Shirt" in shopping_cart_item
    driver.quit()


# shopping cart - bolt t-shirt
def test_9_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bolt T-Shirt" in shopping_cart_item
    driver.quit()


# shopping cart - Fleece Jacket
def test_10_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Fleece Jacket" in shopping_cart_item
    driver.quit()


# shopping cart - Fleece Jacket
def test_10_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Fleece Jacket" in shopping_cart_item
    driver.quit()


# shopping cart - Onesie
def test1_11_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Onesie" in shopping_cart_item
    driver.quit()


# shopping cart - Onesie
def test_11_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Onesie" in shopping_cart_item
    driver.quit()

# shopping cart - test.allthethings()-t-shirt-(red)
def test_12_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Test.allTheThings() T-Shirt (Red)" in shopping_cart_item
    driver.quit()


# shopping cart - test.allthethings()-t-shirt-(red)
def test_12_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Test.allTheThings() T-Shirt (Red)" in shopping_cart_item
    driver.quit()

# title
def test_login_and_title_firefox2():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    assert driver.title == "Swag Labs"
    driver.quit()


# title
def test_login_and_title_chrome2():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    assert driver.title == "Swag Labs"
    driver.quit()


# shopping cart - backpack 
def test_13_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Backpack" in shopping_cart_item
    driver.quit()


# shopping cart - backpack 
def test_13_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Backpack" in shopping_cart_item
    driver.quit()


# shopping cart - bike light
def test_14_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bike Light" in shopping_cart_item
    driver.quit()


# shopping cart - bike light
def test_14_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bike Light" in shopping_cart_item
    driver.quit()


# shopping cart - bolt t-shirt
def test_15_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bolt T-Shirt" in shopping_cart_item
    driver.quit()


# shopping cart - bolt t-shirt
def test_15_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Bolt T-Shirt" in shopping_cart_item
    driver.quit()


# shopping cart - Fleece Jacket
def test_16_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Fleece Jacket" in shopping_cart_item
    driver.quit()


# shopping cart - Fleece Jacket
def test_16_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Fleece Jacket" in shopping_cart_item
    driver.quit()


# shopping cart - Onesie
def test_17_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Onesie" in shopping_cart_item
    driver.quit()


# shopping cart - Onesie
def test_17_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Sauce Labs Onesie" in shopping_cart_item
    driver.quit()

# shopping cart - test.allthethings()-t-shirt-(red)
def test_18_firefox():
    driver = webdriver.Firefox(options=ffoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Test.allTheThings() T-Shirt (Red)" in shopping_cart_item
    driver.quit()


# shopping cart - test.allthethings()-t-shirt-(red)
def test_18_chrome():
    driver = webdriver.Chrome(options=chromeoptions)
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    username = driver.find_element(By.ID,"password")
    username.send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()
    sleep(3)
    shopping_cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
    assert "Test.allTheThings() T-Shirt (Red)" in shopping_cart_item
    driver.quit()