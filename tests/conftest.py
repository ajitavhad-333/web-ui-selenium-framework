import os
import pytest
from selenium import webdriver

from pages.login_page import LoginPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"

# Common Brave install locations (the first one that exists is used)
BRAVE_PATHS = [
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"),
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",  # macOS
    "/usr/bin/brave-browser",                                         # Linux
]


def find_brave(custom_path=None):
    if custom_path:
        return custom_path
    for path in BRAVE_PATHS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(
        "Brave not found. Pass the path with --brave-path "
        "(e.g. --brave-path \"C:\\...\\brave.exe\")"
    )


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="chrome, brave or firefox")
    parser.addoption("--headless", action="store_true", help="run without a visible browser")
    parser.addoption("--brave-path", default=None, help="full path to brave.exe")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        drv = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()  # Brave uses Chromium options too
        if browser == "brave":
            options.binary_location = find_brave(request.config.getoption("--brave-path"))
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        drv = webdriver.Chrome(options=options)

    drv.implicitly_wait(0)
    yield drv
    drv.quit()


@pytest.fixture
def logged_in_driver(driver):
    LoginPage(driver).open().login(VALID_USER, VALID_PASSWORD)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if drv:
            os.makedirs("screenshots", exist_ok=True)
            drv.save_screenshot(os.path.join("screenshots", f"{item.name}.png"))