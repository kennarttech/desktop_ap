from user import User

users = [User(1, 'kenneth', 'mypassword'),
         User(2, 'Kwame', 'secret')]


username_table = {u.username: u for u in users}
userid_tabel = {u.id:u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user
    

def identity(payload):
    user_id = payload['identity']
    return user_id.get(user_id, None)