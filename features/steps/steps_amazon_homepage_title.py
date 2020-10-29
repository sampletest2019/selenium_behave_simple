from behave import when, then

expected_title = "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
base_url = "https://www.amazon.com"

@given(u'user is on the Amazon home page')
def step_impl(context):
    context.browser.get(base_url)


@then(u'title of the web page is "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"')
def step_impl(context):
    assert context.browser.title == expected_title
