import pickle
import tkinter as tk
import face_recognition
import cv2
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from sql import setup_database, add_user, get_users
from reconhecimento import capture_face

class FacialRecognitionApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Sistema de Reconhecimento Facial")
		self.create_widgets()

	def create_widgets(self):
		self.label = tk.Label(self.root, text="Nome:")
		self.label.pack()
		
		self.video_label = tk.Label(self.root)
		self.video_label.pack()

		self.cap = cv2.VideoCapture(0)
		self.update_video()

		self.name_entry = tk.Entry(self.root)
		self.name_entry.pack()

		self.add_button = tk.Button(self.root, text="Adicionar Usuário", command=self.add_user_button)
		self.add_button.pack()

		self.view_button = tk.Button(self.root, text="Visualizar Usuários", command=self.view_users)
		self.view_button.pack()

	def update_video(self):
        # Captura um frame da câmera
		ret, frame = self.cap.read()
        
		if ret:
            # Converte o frame de BGR para RGB
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Converte a imagem do OpenCV para uma imagem do PIL
			image = Image.fromarray(frame)
            
            # Converte a imagem do PIL para um formato que o Tkinter pode exibir
			tk_image = ImageTk.PhotoImage(image=image)
            
            # Atualiza o Label com a nova imagem
			self.video_label.configure(image=tk_image)
			self.video_label.image = tk_image

        # Atualiza a imagem a cada 30 ms
		self.root.after(30, self.update_video)

	def __del__(self):
        # Libera a captura de vídeo ao fechar o aplicativo
		if self.cap.isOpened():
			self.cap.release()
	def add_user_button(self):
		name = self.name_entry.get()
		if name:
			self.add_user(name)
		else:
			messagebox.showwarning("Aviso", "Por favor, insira um nome.")

	def add_user(self, name):
		try:
			encoding = capture_face()
			add_user(name, encoding)
			messagebox.showinfo("Info", "Usuário adicionado com sucesso!")
		except Exception as e:
			messagebox.showerror("Erro", f"Erro ao adicionar usuário: {e}")

	def view_users(self):
		try:
			users = get_users()
			user_list = "\n".join([f"{user[0]}: {user[1]}" for user in users])
			messagebox.showinfo("Usuários", user_list)
		except Exception as e:
			messagebox.showerror("Erro", f"Erro ao visualizar usuários: {e}")

if __name__ == "__main__":
	setup_database()
	root = tk.Tk()
	app = FacialRecognitionApp(root)
	root.mainloop()   