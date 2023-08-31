import pytest
from selenium import webdriver
import logging
from test_resources.test_keywords import Keywords
from test_resources.test_variables import Locators


def test_navigate_to_home_page_and_interact_with_inner_elements(setup_teardown):
    k = setup_teardown

    k.user_is_on_home_page()
    k.click_element(Locators.lets_talk_button_xpath)
    k.user_is_on_contact_page()
    k.click_element(Locators.tg_main_button_xpath)
    k.user_is_on_home_page()
    k.click_element(Locators.contact_me_button_xpath)
    k.user_is_on_contact_page()
    k.click_element(Locators.tg_secondary_button_xpath)
    k.user_is_on_home_page()
    k.click_element(Locators.main_skills_xpath)
    k.user_is_on_cv_page()
    k.click_element(Locators.contact_me_button_xpath)
    k.user_is_on_contact_page()
    k.click_element(Locators.home_upper_button_xpath)
    k.user_is_on_home_page()


def test_navigate_to_contact_page_and_check_social_media_buttons(setup_teardown):
    k = setup_teardown

    k.user_is_on_home_page()
    k.click_element(Locators.contact_me_button_xpath)
    k.user_is_on_contact_page()
    k.verify_social_media_link_opens_in_new_tab(Locators.linkedin_xpath, Locators.linkedin_url)
    k.verify_social_media_link_opens_in_new_tab(Locators.whatsapp_xpath, Locators.whatsapp_url)
    k.verify_social_media_link_opens_in_new_tab(Locators.github_xpath, Locators.github_url)
    k.verify_social_media_link_opens_in_new_tab(Locators.facebook_xpath, Locators.facebook_url)
    k.verify_social_media_link_opens_in_new_tab(Locators.instagram_xpath, Locators.instagram_url)
    k.verify_social_media_link_opens_in_new_tab(Locators.twitter_xpath, Locators.twitter_url)
    k.click_element(Locators.home_upper_button_xpath)
    k.user_is_on_home_page()


def test_navigate_to_contact_page_and_check_email_and_phone_links(setup_teardown):
    k = setup_teardown

    k.user_is_on_home_page()
    k.click_element(Locators.contact_me_button_xpath)
    k.user_is_on_contact_page()
    k.verify_email_or_phone_link(Locators.yahoo_mail_xpath, Locators.yahoo_mail_link)
    k.verify_email_or_phone_link(Locators.google_mail_xpath, Locators.google_mail_link)
    k.verify_email_or_phone_link(Locators.phone_number_xpath, Locators.phone_number_link)

