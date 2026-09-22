from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    HEADER_FEED_OF_ORDERS = By.XPATH, "//h1[text()='Лента заказов']"            
    ORDER_IN_FEED = By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r.mb-6"     
    ORDER_FROM_THE_ORDER_FEED = By.CLASS_NAME, "OrderHistory_listItem__2x95r"   
    COUNTER_TOTAL_ORDERS_FOR_ALL_TIME = By.XPATH, "//div[p[text()='Выполнено за все время:']]/p[contains(@class, 'OrderFeed_number')]"
    COUNTER_TOTAL_ORDERS_FOR_TODAY = By.XPATH, "//div[p[text()='Выполнено за сегодня:']]/p[contains(@class, 'OrderFeed_number')]"
    ORDERS_IN_WORK = (By.XPATH,"//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
