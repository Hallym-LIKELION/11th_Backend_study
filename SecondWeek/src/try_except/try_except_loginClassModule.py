import json

DATABASE_PATH = "../database/database.json"
LOGIN_INFO_PATH = "../database/loginInfo.json"

class AccessRoute:
    def __init__(self, login_path, database_path):
        self.login_path = login_path
        self.database_path = database_path
        self.database_dict = dict()
        self.login_info_dict = dict()
        self.data = dict()
        
    def access_login_data(self):
        try:
            with open(self.login_path, 'r') as f:
                self.data = json.load(f)

        except FileNotFoundError:
            print("로그인 정보에 접근이 불가능 합니다.")
            exit()
        
    def access_database(self, user_key="users", id_key="ID", pw_key="PW"):
        try:
            with open(self.database_path, 'r') as f:
                self.data = json.load(f)
            return self.data[user_key][id_key], self.data[user_key][pw_key]

        except FileNotFoundError:
            print("데이터베이스에 접근이 불가능 합니다.")
            exit()
    
    def access_login_info(self, user_key="users", id_key="ID", pw_key="PW"):
        try: 
            user_id, user_pw = self.data[user_key][id_key], self.data[user_key][pw_key]
        
        except KeyError:
            print("로그인 정보가 없습니다.")
            exit()

        return user_id, user_pw

class LoginClassModule(AccessRoute):
    def __init__(self, login_path, database_path):
        super().__init__(login_path, database_path)
        
    def after_login_action(self, login_flag):
        if login_flag:  
            print("로그인 성공")
            return True

        else:   
            print("로그인 실패")
            return False

    def login_function(self):
        db_id, db_pw = self.access_database()
        login_id, login_pw = self.access_login_info()
        if login_id == db_id:
            if login_pw == db_pw: 
                self.after_login_action(True)
            else: 
                self.after_login_action(False)
        else: 
            self.after_login_action(False)
        