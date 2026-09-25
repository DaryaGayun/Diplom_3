from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from helpers import *
import allure
import re

class OrderFeedPage(BasePage):
    @allure.step('Получить значение счётчика в ленте заказов за ВСЕ ВРЕМЯ (как число)')
    def get_counter_value_increases_completed_total(self) -> int:
        counter = self.get_text_from_element(OrderFeedPageLocators.COUNTER_TOTAL_ORDERS_FOR_ALL_TIME)
        digits = re.sub(r'\D', '', counter)
        return int(digits) if digits else 0

    @allure.step('Получить значение счётчика в ленте заказов за СЕГОДНЯ (как число)')
    def get_counter_value_increases_completed_total_today(self) -> int:
        counter = self.get_text_from_element(OrderFeedPageLocators.COUNTER_TOTAL_ORDERS_FOR_TODAY)
        digits = re.sub(r'\D', '', counter)
        return int(digits) if digits else 0

    @allure.step("Обновить страницу ленты заказов и дождаться загрузки")
    def refresh_feed_of_orders_page_and_wait(self):
        self.refresh_page_and_wait(OrderFeedPageLocators.HEADER_FEED_OF_ORDERS)

    @allure.step("Получить номер заказа из раздела 'В работе' в 'Ленте заказов'")
    def get_order_number_in_progress_section(self) -> str:
        return self.get_element(OrderFeedPageLocators.ORDERS_IN_WORK).text.lstrip('0')
