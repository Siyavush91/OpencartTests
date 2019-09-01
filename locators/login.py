from selenium.webdriver.common.by import By


class Login:

    user_name = (By.CSS_SELECTOR, "#input-username")
    password_field = (By.ID, "input-password")
    alert_error = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    login_button = (By.CSS_SELECTOR, "button.btn.btn-primary")
