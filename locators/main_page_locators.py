from selenium.webdriver.common.by import By

class MainPageLocators:
    STELLAR_BURGERS_LOGO = (By.XPATH, "//a[@aria-current='page' and @href='/']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_BUTTON = (By. XPATH, "//button[text()='Войти в аккаунт']")

    CRATER_BUN = (By.XPATH, "//a[.//p[contains(text(), 'Краторная булка')]]")
    FLUORESCENT_BUN = (By.XPATH, "//a[.//p[contains(text(), 'Флюоресцентная булка R2-D3')]]")
    SPACE_SAUCE = (By.XPATH, "//a[.//p[text()='Соус фирменный Space Sauce']]")
    ANTARIAN_FLATWALKER_SPIKED_SAUCE = (By.XPATH, "//a[.//p[text()='Соус с шипами Антарианского плоскоходца']]")
    BEEF_METEORITE = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @draggable='true']"
    "[.//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Говяжий метеорит (отбивная)']]")
    MARS_MAGNOLIA_BIOCOTELET = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @draggable='true']"
    "[.//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Биокотлета из марсианской Магнолии']]")
    CRISPY_MINERAL_RINGS = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @draggable='true']"
    "[.//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Хрустящие минеральные кольца']]")
    CHEESE_WITH_ASTEROID_MOLD = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @draggable='true']"
    "[.//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Сыр с астероидной плесенью']]")
    CRATER_BUN_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Краторная булка N-200i (верх)')]")
    FLUORESCENT_BUN_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Флюоресцентная булка R2-D3 (верх)')]")
    SPACE_SAUCE_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Соус фирменный Space Sauce')]")
    ANTARIAN_FLATWALKER_SPIKED_SAUCE_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Соус с шипами Антарианского плоскоходца')]")
    BEEF_METEORITE_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Говяжий метеорит (отбивная)')]")
    MARS_MAGNOLIA_BIOCOTELET_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Биокотлета из марсианской Магнолии')]")
    CRISPY_MINERAL_RINGS_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Хрустящие минеральные кольца')]")
    CHEESE_WITH_ASTEROID_MOLD_IN_ORDER = (By.XPATH, "//span[contains(text(), 'Сыр с астероидной плесенью')]")

    RESULT_ORDER = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
    INGREDIENT_DETAILS_TEXT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_READY = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__')]")
    CLOSE_ORDER_WINDOW_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button")
    INGREDIENT = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]')
    INGREDIENT_MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal__P3_V5')]")
    INGREDIENT_COUNTER = (By.XPATH, "((//a[starts-with(@href, '/ingredient/')])[1]//p[contains(@class, 'counter')])[1]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    COLLECT_BURGER_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")