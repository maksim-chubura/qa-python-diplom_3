from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//li[@class='undefined ml-2']//a[contains(., 'Лента Заказов')]")
    FIRST_LINK_ORDER_FEED = (By.CSS_SELECTOR, ".OrderFeed_list__OLh59 > li:first-child a")
    NUMBER_ORDER = (By.CSS_SELECTOR, "p.text_type_digits-default")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li["
                                   "@class='text text_type_digits-default mb-2']")
    MODAL_WINDOW_ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__')]")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5' and text()='Лента заказов']")
    ALL_ORDERS_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_FEED_ITEM_LOCATOR = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59 > li:first-child p.text.text_type_digits-default")