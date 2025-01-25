from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локатор поля ввода имени
    name_input_locator = (By.XPATH, "//input[@placeholder='* Имя']")
    # Локатор поля ввода фамилии
    surname_input_locator = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Локатор поля ввода адреса
    address_input_locator = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Локатор поля ввода станции метро
    metro_field_locator = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # Локатор списка вариантов метро
    metro_options_locator = (By.XPATH, "//div[@class='select-search__select']//li")
    # Локатор поля ввода телефона
    phone_input_locator = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Локатор кнопки "Далее"
    next_button_locator = (By.XPATH, "//button[text()='Далее']")

    # Локатор поля выбора даты доставки
    delivery_date_locator = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Локатор поля выбора периода аренды
    rental_period_locator = (By.CLASS_NAME, "Dropdown-placeholder")
    # Локатор списка опций выбора аренды
    rental_options_locator = (By.XPATH, "//div[@class='Dropdown-option']")
    # Локатор поля ввода комментария для курьера
    comment_input_locator = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Локатор радиокнопки выбора цвета самоката (например, для выбора цвета)
    color_locator = (By.XPATH, "//label[contains(@class, 'Checkbox_Label')]")
    # Локатор кнопки "Заказать"
    order_button_locator = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Локатор кнопки подтверждения заказа
    confirm_button_locator = (By.XPATH, "//button[text()='Да']")
    # Локатор сообщения об успешном создании заказа
    success_message_locator = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    # Локатор кнопки "Посмотреть статус"
    view_status_button_locator = (By.XPATH, "//button[text()='Посмотреть статус']")
    # Локатор кнопки "Посмотреть" на странице заказа
    look_button_locator = (By.XPATH, "//button[text()='Посмотреть']")
