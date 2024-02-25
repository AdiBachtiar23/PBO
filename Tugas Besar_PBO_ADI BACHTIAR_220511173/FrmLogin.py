import tkinter as tk
from tkinter import Frame,Label,Entry,Button,StringVar,messagebox
from users import *
from FrmApotek import FormApotek

class FormLogin:
    
    def __init__(self, parent, title, update_main_window):
        self.parent = parent       
        self.update_main_window = update_main_window 
        self.parent.geometry("600x00")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=20, bg='light blue')
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
            

        # diatur agar tampil di tengah layar
        screen_width = mainFrame.winfo_screenwidth()
        screen_height = mainFrame.winfo_screenheight()
        x = (screen_width - 350) // 2
        y = (screen_height - 250) // 2
        width = 350
        height = 250

        self.parent.geometry(f"{width}x{height}+{x}+{y}")

        # Label
        Label(mainFrame, text='Email:').grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.txtEmail = Entry(mainFrame, bg='light blue') 
        self.txtEmail.grid(row=0, column=1, padx=10, pady=10) 
        

        Label(mainFrame, text='Password:').grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        self.txtPassword = Entry(mainFrame, bg='light blue') 
        self.txtPassword.grid(row=1, column=1, padx=10, pady=10) 

     
        
        # Button
        self.btnSubmit = Button(mainFrame, text='Login', command=self.onSubmit, width=10)
        self.btnSubmit.grid(row=2, column=0, padx=5, pady=5)
        self.btnCancel = Button(mainFrame, text='Cancel', command=self.onKeluar, width=10)
        self.btnCancel.grid(row=2, column=1, padx=5, pady=5)
      
                 
    def onSubmit(self, event=None):
        email = self.txtEmail.get()
        password = self.txtPassword.get()
                
        obj = Users()
        val = obj.Validasi(email,password)
        C = val[1]
        if(C==True):
            self.update_main_window(val)
            self.open_apotek()
            self.parent.destroy()
        else:
            messagebox.showwarning("showwarning", "Login Gagal ")
           
        return val
    
    def open_apotek(self):
        title = "FrmApotek"

        laundry = FormApotek(self.parent, title)

            
            

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = FormLogin(root, "Aplikasi Apotek",update_main_window)
    root.mainloop()
