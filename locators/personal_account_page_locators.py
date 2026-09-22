from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    LOGIN_TITLE = By.XPATH, '//h2[text()="Вход"]'                                     
    FIELDS_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'       
    FIELDS_PASSWORD = By.XPATH, '//input[@name = "Пароль"]'                           
    BUTTON_LOGIN  = By.XPATH, '//button[text()="Войти"]'                           
    REGISTER_BUTTON_LOGIN = (By.XPATH, '//a[text() = "Зарегистрироваться"]')                        
    FLAG_OF_INCORRECT_PASSWORD = (By.XPATH, '//p[text() = "Некорректный пароль"]')        
    BUTTON_SUBMIT = (By.XPATH, '//button[text() = "Зарегистрироваться"]')              
    BUTTON_EXIT_PERSONAL_ACCOUNT_PAGE_LOCATOR = By.XPATH, ".//button[text()='Выход']"  
    FIELDS_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')         
