import json

DATABASE_PATH = "../database/database.json"
LOGIN_INFO_PATH = "../database/loginInfo.json"

def database_access(database_dict, logging=False):
    if logging:
        print(database_dict['users']['ID'], database_dict['users']['PW'])
    return database_dict['users']['ID'], database_dict['users']['PW']

def login_info_access(login_info_dict, logging=False):
    if logging:
        print(login_info_dict['ID'], login_info_dict['PW'])
    return login_info_dict['ID'], login_info_dict['PW']

def login_function(login_info_data, database_dict):
    db_id, db_pw = database_access(database_dict)
    login_id, login_pw = login_info_access(login_info_data)
    if login_id == db_id:
        if login_pw == db_pw: 
            return True
        else: 
            return False
    else: 
        return False
    
def after_login_action(login_flag):
    if login_flag:  print("로그인 성공")
    else:   print("로그인 실패")

database_data, login_info_data = dict(), dict()

with open(DATABASE_PATH, 'r') as f:
    database_data = json.load(f)

with open(LOGIN_INFO_PATH, 'r') as f:
    login_info_data = json.load(f)

after_login_action(login_function(login_info_data, database_data))
