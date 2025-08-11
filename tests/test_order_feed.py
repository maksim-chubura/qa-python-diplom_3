import allure
from conftest import BaseTest

@allure.feature("Раздел «Лента заказов»")
class TestOrderFeedPage(BaseTest):

    @allure.title("Клик на заказ открывает всплывающее окно с деталями")
    def test_ckick_on_order_open_modal_window(self):
        self.order_feed.click_order_feed_button()
        self.order_feed.wait_load_order_feed_page()
        self.order_feed.click_first_order_in_order_feed()
        self.order_feed.wait_load_modal_window_order_details()
        number_order = self.order_feed.get_number_order()
        assert number_order.startswith("#0"), f"Номер заказа '{number_order}' не начинается с '#0'"
        print(f"Номер заказа: {number_order}")

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_displayed_on_order_feed(self):
        self.main_page.create_other_order()
        self.main_page.click_button_close_order_window()
        self.main_page.wait_load_page()
        self.main_page.click_profile_button()
        self.profile_page.is_profile_page()
        self.profile_page.click_order_history()
        self.profile_page.is_order_history_page()
        order_number_details = self.profile_page.scroll_to_last_order_and_get_number()
        self.order_feed.go_to_order_feed()
        order_number_feed = self.order_feed.get_order_number_from_feed()
        assert order_number_details == order_number_feed, f"Номера заказов не совпадают: {order_number_details} != {order_number_feed}"

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_counter(self):
        self.order_feed.go_to_order_feed()
        old_total, _ = self.order_feed.get_orders_count_for_all_time()
        self.main_page.go_to_constructor()
        self.main_page.create_order()
        self.main_page.make_order()
        self.main_page.is_order_accepted()
        self.main_page.click_button_close_order_window()
        self.main_page.wait_load_page()
        self.order_feed.go_to_order_feed()
        new_total, _ = self.order_feed.get_orders_count_for_all_time()
        assert old_total < new_total

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_daily_counter(self):
        self.order_feed.go_to_order_feed()
        self.order_feed.scroll_to_count_for_today()
        _, old_daily = self.order_feed.get_orders_count_for_today()
        self.main_page.go_to_constructor()
        self.main_page.create_order()
        self.main_page.make_order()
        self.main_page.is_order_accepted()
        self.main_page.click_button_close_order_window()
        self.main_page.wait_load_page()
        self.order_feed.go_to_order_feed()
        self.order_feed.scroll_to_count_for_today()
        _, new_daily = self.order_feed.get_orders_count_for_today()
        assert old_daily < new_daily

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_in_progress(self):
        self.main_page.create_order()
        self.main_page.make_order()
        self.main_page.is_order_accepted()
        self.main_page.wait_for_valid_order_id_in_modal()
        order_id = self.main_page.get_odrer_id()
        self.main_page.click_button_close_order_window()
        self.main_page.wait_load_page()
        self.order_feed.go_to_order_feed()
        last_order_number = self.order_feed.get_order_number_in_progress()
        assert order_id in last_order_number, f"Номер заказа '{order_id}' не найден в списке заказов 'В работе': {last_order_number}"