import sqlite3

# try:
#     connection = sqlite3.connect('sqlite.db')
# except sqlite3.DatabaseError:
#     print('Возникла ошибка при подключении к базе данных  ')
# finally:
#     connection.close()


class User:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


def add_new_user(cur: sqlite3.Cursor, user: User):
    command = '''
    INSERT INTO users (name, surname, age, gender) VALUES (?, ?, ?, ?)
    '''
    cur.execute(command, (user.name, user.surname, user.age, user.gender)) 


def get_all_users(cur: sqlite3.Cursor):
    command = '''
    SELECT * FROM users
    '''
    result = cur.execute(command)
    return result.fetchall()


def get_user(cur: sqlite3.Cursor, user_id: int):
    command = '''
    SELECT * FROM users WHERE id = ?;
    '''
    result = cur.execute(command, (user_id,))
    return result.fetchone()


def create_user_table(cur: sqlite3.Cursor):
    command = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    age INTEGER,
    gender TEXT);
    '''
    cur.execute(command)


def clear_user_table(cur: sqlite3.Cursor):
    command = '''
    DELETE FROM users 
    '''
    cur.execute(command)


# def clear_user(cur: sqlite3.Cursor, user_id: int):
#     command = '''
#     DELETE FROM users WHERE id = ?
#     '''
#     cur.execute(command, (user_id,))


def update_user_name(cur: sqlite3, name: str, user_id: int):
    command = '''
    UPDATE users SET name = ? WHERE id = ?
    '''
    cur.execute(command, (name, user_id))


def select_user_gender(cur: sqlite3.Cursor, gender: str):
    command = '''
    SELECT * FROM users WHERE gender = ?    
    '''
    result = cur.execute(command, (gender,))
    return result.fetchall()


if __name__ == '__main__':
    with sqlite3.connect('sqlite.db') as connection:
        cursor = connection.cursor()
        create_user_table(cursor)
        # clear_user_table(cursor)
        # clear_user(cursor, 12)
        user = User(name='Алёна', surname='Иванова', age=17, gender='Ж')
        add_new_user(cursor, user=user)
        users = get_all_users(cursor)
        print(users)
        # update_user_name(cursor, 'Евгений', 1)
        user = get_user(cursor, 1)
        boys = select_user_gender(cursor, 'М')
        girls = select_user_gender(cursor, 'Ж')
        # print(user)
        print(boys)
        print(girls)






# (name='Алёна', surname='Иванова', age=17, gender='Ж')
# (name='Максим', surname='Максимов', age=16, gender='М')

