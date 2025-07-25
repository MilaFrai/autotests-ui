from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator("//div[@data-testid='registration-form-email-input']//div/input")
    email_input.fill('user.name@gmail.com')

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div/input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div/input')
    password_input.fill('password')

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    dashboard_name = page.locator("//h6[@data-testid='dashboard-toolbar-title-text']")
    expect(dashboard_name).to_be_visible()
    expect(dashboard_name).to_have_text('Dashboard')

    page.wait_for_timeout(5000)