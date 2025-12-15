class LoginPage:
    def __init__(self, page):
        self.page = page

        self.email_input = "input[placeholder='Email']"
        self.password_input = "input[placeholder='Password']"
        self.login_button = "button:has-text('Login')"

    def open(self):
        self.page.goto("https://app.beemerbenzbentley.site/auth/login")

    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
