from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner div.basket-items")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BASKET_PRICE_IN_MESSAGE = (By.XPATH, "(//*[@id='messages']//strong)[3]")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "(//*[@id='messages']//strong)[1]")
    SUCCESS_MESSAGE = (By.XPATH,"(//*[@id='messages']/div)[1]")


    