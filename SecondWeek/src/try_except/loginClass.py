from try_except_loginClassModule import LoginClassModule

DATABASE_PATH = "../database/database_new.json"
LOGIN_INFO_PATH = "../database/loginInfo.json"

login_check = LoginClassModule(LOGIN_INFO_PATH, DATABASE_PATH)
print(login_check.login_function())
