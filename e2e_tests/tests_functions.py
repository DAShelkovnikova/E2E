from selenium.webdriver.common.by import By


class TestUiE2e:
    def test_buy_product(self, driver):
        # Проверка авторизации пользователя
        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        # Проверка процесса добавления товара в корзину (например, "Sauce Labs Backpack")
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").get_attribute("Sauce Labs Backpack")
        # Проверка процесса оформления заказа
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ivan")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Ivanov")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, "#continue").click()
        driver.find_element(By.CSS_SELECTOR, "#finish").click()
        # Проверка совершения покупки
        assert (driver.find_element(By.CSS_SELECTOR, ".title").is_displayed() and
                driver.find_element(By.CSS_SELECTOR, ".complete-header").text == "Thank you for your order!"
                )