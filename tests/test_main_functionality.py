from urls import *
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from helpers import *
import allure

class TestMainFunctionality:
    @allure.title('Проверка перехода на страницу "Конструктор" по кнопке «Конструктор»')
    @allure.description('Открываем страницу авторизации, переходим в «Конструктор» по кнопке в шапке, сравниваем URL.')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_navigate_to_constructor_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_button_constructor_in_header()
        current_url = login_page.check_to_url()
        with allure.step('Сравнить текущий URL с ожидаемым'):
            assert current_url == URL_MAIN_PAGE, (
                f"Неверный URL: ожидалось '{URL_MAIN_PAGE}', "
                f"получено '{current_url}'"
            )

    @allure.title('Проверка перехода на страницу «Лента заказов» по кнопке в шапке')
    @allure.description('Открываем «Конструктор», переходим на «Ленту заказов» по кнопке, сравниваем URL.')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_navigate_to_feed_of_orders_page(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_feed_of_orders_in_header()
        current_url = constructor_page.check_to_url()
        with allure.step('Сравнить текущий URL с ожидаемым'):
            assert current_url == Urls.URL_FEED_OF_ORDERS_PAGE, (
                f"Неверный URL: ожидалось '{Urls.URL_FEED_OF_ORDERS_PAGE}', "
                f"получено '{current_url}'"
            )

    @allure.title('Проверка появления всплывающего окна с деталями выбранного ингредиента')
    @allure.description('Кликаем на ингредиент, ждём модальное окно, проверяем заголовок.')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_window_appearance_with_details_should_display_correct_info(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_ingredient_in_constructor()
        ingredient_title = constructor_page.get_name_ingredient_details()
        with allure.step('Проверить, что модальное окно открыто'):
            assert constructor_page.is_displayed_opened_modal_window(), ("Всплывающее окно не открыто")
        with allure.step('Проверить соответствие заголовка ожидаемому'):
            expected_title = "Флюоресцентная булка R2-D3"
            assert ingredient_title == expected_title, (
                f"Заголовок не совпадает: ожидалось '{expected_title}', "
                f"получено '{ingredient_title}'"
            )

    @allure.title('Проверка закрытия всплывающего окна по клику на крестик')
    @allure.description('Открываем окно, кликаем крестик, проверяем закрытие и заголовок страницы.')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_closing_window_clicking_on_cross(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        constructor_page.click_button_ingredient_in_constructor()
        constructor_page.click_button_close_modal_window()
        expected_title = "Соберите бургер"
        actual_title = constructor_page.get_title_assemble_the_burger()
        with allure.step('Проверить, что окно закрыто'):
            assert constructor_page.is_displayed_closed_modal_window(), ("Модальное окно не закрыто")
        with allure.step('Проверить заголовок страницы после закрытия окна'):
            assert actual_title == expected_title, (
                f"Заголовок страницы не совпадает: ожидалось '{expected_title}', "
                f"получено '{actual_title}'"
            )

    @allure.title('Проверка увеличения счётчика ингредиента при добавлении в заказ')
    @allure.description('Добавляем ингредиент в корзину, проверяем, что счётчик увеличился.')
    @allure.story('Проверка основного функционала')
    @allure.link(URL_MAIN_PAGE, name='Учебный сервис «Stellar Burgers»')
    def test_increasing_the_ingredient_counter_adding_order(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_constructor_page()
        expected_value = int(constructor_page.get_ingredient_counter_value())
        constructor_page.drag_and_drop_and_verify_r2_d3()
        actual_value = int(constructor_page.get_ingredient_counter_value())
        with allure.step('Проверить увеличение счётчика ингредиента'):
            assert actual_value > expected_value, (f"Счётчик не увеличился: было {expected_value}, стало {actual_value}")
