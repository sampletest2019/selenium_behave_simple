from behave import Given, When, Then

expected_title = "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
base_url = "https://www.amazon.com"
search_title = "Amazon.com : nike air max"


@given(u'user is on the Amazon web site')
def step_impl(context):
    context.browser.get(base_url)
    assert context.browser.title == expected_title

@when(u'user clicks in the search field and enters "Nike Airmax"')
def step_impl(context, item):
    search_field = context.browser.find_element_by_id("twotabsearchtextbox")
    search_field.send_keys(item)

@when(u'user clicks on search icon')
def step_impl(context):
    search_button = context.browser.find_element_by_xpath("//input[@value='Go']")
    search_button.click()


@then(u'new page with "Nike Airmax" results and title is displayed')
def step_impl(context):
    assert context.browser.title == search_title
