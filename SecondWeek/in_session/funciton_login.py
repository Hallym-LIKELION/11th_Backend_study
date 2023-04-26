import json

DATABASE_PATH = "database/database.json"
LOGIN_INFO_PATH = "database/loginInfo.json"

def database_access(database_dict):
    return database_dict['users']['ID'], database_dict['users']['PW']

def login_info_access(login_info_data):
    return login_info_data['ID'], login_info_data['PW']

def login_func(login_info_data, database_dict):
    db_id, db_pw = database_access(database_dict)
    login_id, login_pw = login_info_access(login_info_data)

    if login_id == db_id and login_pw == db_pw: return True
    else: return False

database_data = dict()
login_info_data = dict()

# Database data load
with open(DATABASE_PATH, 'r') as f:
    database_data = json.load(f)

# Login Infomation load
with open(LOGIN_INFO_PATH, 'r') as f:
    login_info_data = json.load(f)

print(login_func(login_info_data, database_data))
