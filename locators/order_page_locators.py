from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локатор поля ввода имени
    NAME_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
    # Локатор поля ввода фамилии
    SURNAME_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Локатор поля ввода адреса
    ADDRESS_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Локатор поля ввода станции метро
    METRO_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Локатор списка вариантов метро
    METRO_OPTIONS_LOCATOR = (By.XPATH, "//div[@class='select-search__select']//li")
    # Локатор поля ввода телефона
    PHONE_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Локатор кнопки "Далее"
    NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Далее']")

    # Локатор поля выбора даты доставки
    DELIVERY_DATE_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Локатор поля выбора периода аренды
    RENTAL_PERIOD_LOCATOR = (By.CLASS_NAME, "Dropdown-placeholder")
    # Локатор списка опций выбора аренды
    RENTAL_OPTIONS_LOCATOR = (By.XPATH, "//div[@class='Dropdown-option']")
    # Локатор поля ввода комментария для курьера
    COMMENT_INPUT_LOCATOR = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Локатор радиокнопки выбора цвета самоката (например, для выбора цвета)
    COLOR_LOCATOR = (By.XPATH, "//label[contains(@class, 'Checkbox_Label')]")
    # Локатор кнопки "Заказать"
    ORDER_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Локатор кнопки подтверждения заказа
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Да']")
    # Локатор сообщения об успешном создании заказа
    SUCCESS_MESSAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    # Локатор кнопки "Посмотреть статус"
    VIEW_STATUS_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Посмотреть статус']")
    # Локатор кнопки "Посмотреть" на странице заказа
    LOOK_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Посмотреть']")

    # Локатор логотипа «Самоката»
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    # Локатор логотипа «Яндекса»
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
