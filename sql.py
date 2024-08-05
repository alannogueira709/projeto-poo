import sqlite3
import face_recognition
import cv2

def setup_database():
    conn = sqlite3.connect('faces.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, face_encoding BLOB)''')
    conn.commit()
    conn.close()

def add_user(name, face_encoding):
    conn = sqlite3.connect('faces.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name, face_encoding) VALUES (?, ?)',
              (name, face_encoding))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect('faces.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users

def update_user(user_id, name, face_encoding):
    conn = sqlite3.connect('faces.db')
    c = conn.cursor()
    c.execute('UPDATE users SET name = ?, face_encoding = ? WHERE id = ?',
              (name, face_encoding, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('faces.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

