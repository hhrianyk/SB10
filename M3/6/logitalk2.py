from socket import socket, AF_INET, SOCK_STREAM

from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.title('Logitalk')
        self.label = None

        # --- Бокове меню ---
        self.menu_frame = CTkFrame(self, width=30, height=300)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)

        self.is_show_menu = True
        self.speed_animate_menu = 5

        self.btn = CTkButton(self, text='▶️', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)

        # --- основна частина ---
        self.chat_field = CTkScrollableFrame(self, fg_color="purple")
        self.chat_field.place(x=0, y=0)

        self.message_entry = CTkEntry(self, placeholder_text="Введіть повідомлення", height=40)
        self.message_entry.place(x=0, y=0)

        self.send_button = CTkButton(self, text=">", width=50, height=40)
        self.send_button.place(x=0, y=0)

        self.adaptive_ui()
        self.username = "George"

        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(("2.tcp.ngrok.io",17704))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(-лась) до чату!!"
            self.sock.send(hello.encode())
            self.add_message("Успішне підключенння")
        except:
            self.add_message("Помилка підключення до сервера")

    # --- ЛОГІКА ПЕРЕМИКАННЯ МЕНЮ ---
    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configure(text='▶️')
            self.show_menu()

            if self.label:
                self.label.destroy()
            if getattr(self, "entry", None):
               self.entry.destroy()
            if getattr(self, "save_button", None):
                   self.save_button.destroy()
        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text="◀️")
            self.show_menu()
            # Створюємо внутрішні віджети меню
            self.label = CTkLabel(self.menu_frame, text='Імʼя')
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack()
            # Кнопка збереження
            self.save_button = CTkButton(self.menu_frame, text="Зберегти")
            self.save_button.pack()

    # --- АНІМАЦІЯ ВІДКРИТТЯ/ЗАКРИТТЯ МЕНЮ ---
    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)
        if self.menu_frame.winfo_width() <= 200 and self.is_show_menu:
            self.after(10, self.show_menu)
        elif self.menu_frame.winfo_width() >= 40 and self.is_show_menu == False:
            self.after(10,self.show_menu)

    # --- АДАПТИВНЕ КОМПОНУВАННЯ ---
    def adaptive_ui(self):
        self.menu_frame.configure(height=self.winfo_height())
        self.chat_field.place(x=self.menu_frame.winfo_width())
        self.chat_field.configure(width = self.winfo_width()-self.menu_frame.winfo_width(),
                                  height = self.winfo_height() - self.send_button.winfo_height())

        self.send_button.place(x=self.winfo_width()-self.send_button.winfo_width(), y=self.winfo_height()-self.send_button.winfo_height())
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
        self.message_entry.configure( width=self.winfo_width() - self.menu_frame.winfo_width() - self.send_button.winfo_width())

        self.after(50, self.adaptive_ui)

    def add_message(self, message, img = None):
        message_frame = CTkFrame(self.chat_field, fg_color='grey')
        message_frame.pack(pady=5, anchor='w')
        wrapleng_size = self.winfo_width() - self.menu_frame.winfo_width() - 40

        if img:
            CTkLabel(message_frame, text=message, wraplength=wrapleng_size,
                     text_color='white', image=img, compound='top', justify='left').pack(pady=5)
        else:
            CTkLabel(message_frame, text=message, wraplength=wrapleng_size,
                     text_color='white', justify='left').pack(padx=10, pady=5)

# --- ЗАПУСК ---
win = MainWindow()
win.mainloop()