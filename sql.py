import sqlite3

class Usuarios:
    def __init__(self, username, face_encoding):
        self._nome = username
        self._face_encoding = face_encoding 
    def __str__(self):
        return f'Usuário: {self._nome}'

class Sql:
    def __init__(self):
        self.usuarios = []
        self.setup_database()

    def __str__(self):
        return f'Classe para manipulação de banco de dados'

    def setup_database(self):
        with sqlite3.connect('faces.db') as bancoSQlite:
            bancoCursor = bancoSQlite.cursor()
            bancoCursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    face_encoding TEXT
                )
            ''')
            bancoSQlite.commit()

    def add_user(self, name, face_encoding):
        try:
            with sqlite3.connect('faces.db') as bancoSQlite:
                bancoCursor = bancoSQlite.cursor()
                bancoCursor.execute('INSERT INTO users (name, face_encoding) VALUES (?, ?)',
                          (name, face_encoding))
                print(f"Usuário {name} adicionado com sucesso.")
                bancoSQlite.commit()
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")

    def get_users(self):
        try:
            with sqlite3.connect('faces.db') as bancoSQlite:
                bancoCursor = bancoSQlite.cursor()
                bancoCursor.execute('SELECT * FROM users')
                users = bancoCursor.fetchall()
                print(f" Lista de usuários: {users}")
        except sqlite3.Error as e:
            print(f"Erro ao obter usuários: {e}")
            

    def update_user(self, user_id, name, face_encoding):
        try:
            with sqlite3.connect('faces.db') as bancoSQlite:
                bancoCursor = bancoSQlite.cursor()
                bancoCursor.execute('UPDATE users SET name = ?, face_encoding = ? WHERE id = ?',
                          (name, face_encoding, user_id))
                bancoSQlite.commit()
                print(f"Usuário {name} atualizado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar usuário: {e}")

    def delete_user(self, user_id):
        try:
            with sqlite3.connect('faces.db') as bancoSQlite:
                bancoCursor = bancoSQlite.cursor()
                bancoCursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
                bancoSQlite.commit()
                print(f"Usuário {user_id} deletado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao deletar usuário: {e}")