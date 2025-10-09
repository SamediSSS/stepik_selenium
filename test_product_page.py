import pytest
import time

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
        marks=pytest.mark.skip),
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
        marks=pytest.mark.skip)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    product_page.correct_product_added()
    product_page.correct_basket_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    product_page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.basket_is_empty()

@pytest.mark.new
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = 'qWeRtYuI1132'

        self.login_page = LoginPage(browser, login_link)
        self.login_page.open()
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()

        product_page.correct_product_added()
        product_page.correct_basket_price()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_not_be_success_message()