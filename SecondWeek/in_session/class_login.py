import json

DATABASE_PATH = "database/database.json"
LOGIN_INFO_PATH = "database/loginInfo.json"

class AccessRoute:
    def __init__(self, login_path, database_path):
        self.login_path = login_path
        self.database_path = database_path
        self.database_data = dict()
        self.login_info_data = dict()
        self.data = dict()

    def access_login_data(self):
        with open(self.login_path, 'r') as f:
            self.login_info_data = json.load(f)
        return self.login_info_data['ID'], self.login_info_data['PW']

    def access_database(self):
        with open(self.database_path, 'r') as f:
            self.database_data = json.load(f)
        return self.database_data['users']['ID'], self.database_data['users']['PW']
    
class LoginModule(AccessRoute):
    def __init__(self, login_path, database_path):
        super().__init__(login_path, database_path)

    def login_func(self):
        db_id, db_pw = self.access_database()
        login_id, login_pw = self.access_login_data()
        if db_id == login_id and db_pw == login_pw: 
            self.after_login_action(True)
        else: 
            self.after_login_action(False)

    def after_login_action(self, login_flag):
        if login_flag:
            print("로그인 성공")
            return True
    
        else:
            print("로그인 실패")
            return False
