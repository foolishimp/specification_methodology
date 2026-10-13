def login(user, pw, db):
    rec = db[user]
    return rec['password'] == pw
