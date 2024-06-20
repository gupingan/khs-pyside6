import asyncio
from pyppeteer import launch
from app.lib.core import TomlBase

loop = asyncio.new_event_loop()


async def create_browser(dict_cookies):
    config = dict(
        executablePath=TomlBase.browser_path,
        headless=False,
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
        args=[
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--disable-extensions',
            '--ignore-certificate-errors',
            '--disable-blink-features=AutomationControlled',
            '--excludeSwitches=["enable-automation"]',
            '--window-size=513,820',
        ],
        defaultViewport={"width": 513, "height": 666},
    )
    browser = await launch(**config)
    try:
        pages = await browser.pages()
        page = pages[0]
        cookies = [
            {'name': key, 'value': value, 'domain': '.xiaohongshu.com'} for key, value in dict_cookies.items()
        ]
        for cookie in cookies:
            await page.setCookie(cookie)
        await page.goto('https://www.xiaohongshu.com/')
    except asyncio.CancelledError:
        pass


def startup_browser(dict_cookies: dict):
    loop.run_until_complete(create_browser(dict_cookies))
