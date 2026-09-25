import allure
from urls import *
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:
    @allure.title('Проверка увеличения счётчика «Выполнено за всё время» при создании нового заказа')
    @allure.description('Авторизуемся, запоминаем значение счётчика «за всё время», создаём заказ, снова смотрим счётчик: он должен увеличиться.')
    @allure.story('Проверка раздела «Лента заказов»')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_increases_completed_total_counter_when_new_order_created(self, driver, random_user):
        email, password = random_user
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        login_page.click_button_feed_of_orders_in_header()
        order_feed_page = OrderFeedPage(driver)
        counter_before = int(order_feed_page.get_counter_value_increases_completed_total())
        constructor_page = ConstructorPage(driver)
        constructor_page.click_button_constructor_in_header()
        constructor_page.drag_and_drop_and_verify_r2_d3()
        constructor_page.click_create_order_button()
        constructor_page.click_button_close_modal_window()
        constructor_page.click_button_feed_of_orders_in_header()
        order_feed_page.refresh_feed_of_orders_page_and_wait()
        counter_after = int(order_feed_page.get_counter_value_increases_completed_total())
        with allure.step('Сравнить значения счётчиков ДО и ПОСЛЕ: счётчик ПОСЛЕ должен быть больше'):
            assert counter_after > counter_before, (f"Счётчик не увеличился: было {counter_before}, стало {counter_after}")

    @allure.title('Проверка увеличения счётчика «Выполнено за сегодня» при создании нового заказа')
    @allure.description('Авторизуемся, запоминаем счётчик «за сегодня», создаём заказ, проверяем, что счётчик увеличился.')
    @allure.story('Проверка раздела «Лента заказов»')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_increases_completed_total_today_counter_when_new_order_created(self, driver, random_user):
        email, password = random_user
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        login_page.click_button_feed_of_orders_in_header()
        order_feed_page = OrderFeedPage(driver)
        counter_before = int(order_feed_page.get_counter_value_increases_completed_total_today())
        constructor_page = ConstructorPage(driver)
        constructor_page.click_button_constructor_in_header()
        constructor_page.drag_and_drop_and_verify_r2_d3()
        constructor_page.click_create_order_button()
        constructor_page.click_button_close_modal_window()
        constructor_page.click_button_feed_of_orders_in_header()
        order_feed_page.refresh_feed_of_orders_page_and_wait()
        counter_after = int(order_feed_page.get_counter_value_increases_completed_total_today())
        with allure.step('Сравнить значения счётчиков ДО и ПОСЛЕ: счётчик ПОСЛЕ должен быть больше'):
            assert counter_after > counter_before, (f"Счётчик «за сегодня» не увеличился: было {counter_before}, стало {counter_after}")

    @allure.title('Проверка появления номера заказа в разделе «В работе» после оформления')
    @allure.description('Создаём заказ, запоминаем его номер, переходим в «Ленту заказов», проверяем, что номер есть в секции «В работе».')
    @allure.story('Проверка раздела «Лента заказов»')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_after_placing_order_number_appears_in_progress_section(self, driver, random_user):
        email, password = random_user
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.fill_authorize_form_and_click_enter(email, password)
        constructor_page = ConstructorPage(driver)
        constructor_page.drag_and_drop_and_verify_r2_d3()
        constructor_page.click_create_order_button()
        order_identifier = constructor_page.get_number_of_order()
        constructor_page.click_button_close_modal_window()
        constructor_page.click_button_feed_of_orders_in_header()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.refresh_feed_of_orders_page_and_wait()
        with allure.step(f'Проверить, что номер заказа {order_identifier} отображается в секции «В работе»'):
            assert order_feed_page.get_order_number_in_progress_section() == order_identifier, (
                f"Номер заказа в секции «В работе» не совпадает: "
                f"ожидали '{order_identifier}', "
                f"получили '{order_feed_page.get_order_number_in_progress_section()}'"
            )
