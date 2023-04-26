from class_login_te import LoginModule

DATABASE_PATH = "database/database.json"
LOGIN_INFO_PATH = "database/loginInfo.json"

login_check = LoginModule(LOGIN_INFO_PATH, DATABASE_PATH)
print(login_check.login_func())
