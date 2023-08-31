from test_resources.test_variables import Locators


def test_navigate_to_cv_page_and_check_pdf_downloads(setup_teardown):
    k = setup_teardown

    k.user_is_on_home_page()
    k.click_element(Locators.cv_upper_button_xpath)
    k.user_is_on_cv_page()
    k.verify_pdf_cv()
