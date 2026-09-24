from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    BUNS_BLOCK = By.XPATH, '//span[text()="Булки"]/parent::div'                  
    SAUCES_BLOCK = By.XPATH, '//span[text()="Соусы"]/parent::div'                
    FILLINGS_BLOCK = By.XPATH, '//span[text()="Начинки"]/parent::div'            
    TITLE_ASSEMBLE_THE_BURGER = By.XPATH, ".//h1"                                
    BASKET_OF_BURGER_CONSTRUCTOR = By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    INGREDIENT_R2_D3_BUN_IN_BASKET_CONSTRUCTOR = By.XPATH, '//span[text()="Флюоресцентная булка R2-D3 (верх)"]'
    BUTTON_PLACE_AN_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"                
    INGREDIENT_R2_D3_BUN_LOCATOR = By.XPATH, './/*[text()="Флюоресцентная булка R2-D3"]'  
    INGREDIENT_COUNTER_R2_D3_BUN = By.XPATH, './/*[@class="counter_counter__num__3nue1"]' 
    PROPERTIES_OPEN_MODAL_WINDOW = By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4"
    MODAL_WINDOW_CLOSED_CONSTRUCTOR = By.CSS_SELECTOR, "section.Modal_modal__P3_V5"
    BUTTON_CLOSE_MODAL_WINDOW = By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    INGREDIENT_R2_D3_BUN_NAME_MODAL_WINDOW = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    TEXT_INDICATOR_ORDER_OF_ORDER_MODAL_WINDOW = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]"
    NUMBER_OF_ORDER_MODAL_WINDOW = (By.XPATH, "//h2[contains(@class, 'text text_type_digits-large mb-8')]")
