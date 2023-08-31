import pytest
from selenium import webdriver
import logging
from test_resources.test_keywords import Keywords
from test_resources.test_variables import Locators


def test_submit_message_without_completing_fields(setup_teardown):
    keywords = setup_teardown
    keywords.user_is_on_home_page()
    keywords.click_element(Locators.lets_talk_button_xpath)
    keywords.user_is_on_contact_page()
    keywords.click_element(Locators.submit_button_xpath)
    assert not keywords.element_is_displayed(Locators.message_sent_xpath)
    keywords.click_element(Locators.home_upper_button_xpath)
    keywords.user_is_on_home_page()


def test_submit_message_gradually_completing_fields(setup_teardown):
    keywords = setup_teardown
    keywords.user_is_on_home_page()
    keywords.click_element(Locators.lets_talk_button_xpath)
    keywords.user_is_on_contact_page()
    i = 0
    # A loop to perform the gradual field completion steps
    for field_xpath, field_value in [
        (Locators.contact_name_xpath, Locators.name_input),
        (Locators.contact_email_xpath, Locators.email_input),
        (Locators.contact_phone_xpath, Locators.phone_input),
        (Locators.contact_message_xpath, Locators.message_input)
    ]:
        i += 1
        keywords.element_input_text(field_xpath, field_value)
        keywords.click_element(Locators.submit_button_xpath)
        if i < 4:
            assert not keywords.element_is_displayed(Locators.message_sent_xpath)
        else:
            assert keywords.element_is_displayed(Locators.message_sent_xpath)

    assert keywords.element_text(Locators.message_sent_xpath) == Locators.message_sent_text
    keywords.click_element(Locators.home_upper_button_xpath)
    keywords.user_is_on_home_page()


def test_submit_message_completing_required_fields(setup_teardown):
    keywords = setup_teardown
    keywords.user_is_on_home_page()
    keywords.click_element(Locators.lets_talk_button_xpath)
    keywords.user_is_on_contact_page()

    # Input the required fields
    keywords.element_input_text(Locators.contact_name_xpath, Locators.name_input)
    keywords.element_input_text(Locators.contact_email_xpath, Locators.email_input)
    keywords.element_input_text(Locators.contact_message_xpath, Locators.message_input)

    # Click the submit button
    keywords.click_element(Locators.submit_button_xpath)

    # Check the 'message sent' text
    assert keywords.element_text(Locators.message_sent_xpath) == Locators.message_sent_text
    keywords.click_element(Locators.home_upper_button_xpath)
    keywords.user_is_on_home_page()
