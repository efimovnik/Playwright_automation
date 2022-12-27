class HomePage:

    def __init__(self, page):
        self.celebrating_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrating_body = page.locator("text=playwright-practice was founded by a group")