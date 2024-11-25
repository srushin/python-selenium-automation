from selenium.webdriver.common.by import By
from behave import given, when, then
@given('Open Target Page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Navigate to Cart')
def nav_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href = '/cart?prehydrateClick=true']").click()


@then('Verify Cart is Empty Message')
def verify_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1[class ='sc-fe064f5c-0 dtCtuk']").text
    assert expected_result == actual_result


@when('Click Sign In')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "span[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()



@when('Side Sign In')
def side_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[class = 'sc-ddc722c0-0 sc-f1230b39-0 jKTcnK doBYzz h-margin-t-x2 h-margin-b-default']").click()


@then('Verify Sign In Page')
def sign_page(context):
    expected_result = 'Sign in with password'
    actual_result = actual_result = context.driver.find_element(By.CSS_SELECTOR, "#login").text
    assert expected_result == actual_result