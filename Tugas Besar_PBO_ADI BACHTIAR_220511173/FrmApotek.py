
# filename : FrmApotek.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Apotek import Apotek
class FormApotek:   
    def __init__(self, parent, title,):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NO_INV:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO_INV
        self.txtNO_INV = Entry(mainFrame) 
        self.txtNO_INV.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNO_INV.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='NAMA_OBAT:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_OBAT
        self.txtNAMA_OBAT = Entry(mainFrame) 
        self.txtNAMA_OBAT.grid(row=1, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='JUMLAH_PEMBELIAN:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox JUMLAH_PEMBELIAN
        self.txtJUMLAH_PEMBELIAN = Entry(mainFrame) 
        self.txtJUMLAH_PEMBELIAN.grid(row=2, column=1, padx=5, pady=5)
                
         # decimal 
        Label(mainFrame, text='HARGA:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtHARGA = StringVar()
        CboHARGA = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtHARGA) 
        CboHARGA.grid(row=3, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboHARGA['values'] = ('decimal50','0')
        CboHARGA.current()
        
         # varchar 
        Label(mainFrame, text='STOK_OBAT:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox STOK_OBAT
        self.txtSTOK_OBAT = Entry(mainFrame) 
        self.txtSTOK_OBAT.grid(row=4, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','no_inv','nama_obat','jumlah_pembelian','harga','stok_obat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('no_inv', text='no_inv')
        self.tree.column('no_inv', width="30")
        self.tree.heading('nama_obat', text='nama_obat')
        self.tree.column('nama_obat', width="100")
        self.tree.heading('jumlah_pembelian', text='jumlah_pembelian')
        self.tree.column('jumlah_pembelian', width="100")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="100")
        self.tree.heading('stok_obat', text='stok_obat')
        self.tree.column('stok_obat', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNO_INV.delete(0,END)
        self.txtNO_INV.insert(END,"")
                                
        self.txtNAMA_OBAT.delete(0,END)
        self.txtNAMA_OBAT.insert(END,"")
                                
        self.txtJUMLAH_PEMBELIAN.delete(0,END)
        self.txtJUMLAH_PEMBELIAN.insert(END,"")
                                
        self.txtSTOK_OBAT.delete(0,END)
        self.txtSTOK_OBAT.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data apotek
        obj = Apotek()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        no_inv = self.txtNO_INV.get()
        obj = Apotek()
        res = obj.getByNO_INV(no_inv)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        no_inv = self.txtNO_INV.get()
        obj = Apotek()
        res = obj.getByNO_INV(no_inv)
            
        self.txtNAMA_OBAT.delete(0,END)
        self.txtNAMA_OBAT.insert(END,obj.nama_obat)
                                
        self.txtJUMLAH_PEMBELIAN.delete(0,END)
        self.txtJUMLAH_PEMBELIAN.insert(END,obj.jumlah_pembelian)
                                
        self.txtSTOK_OBAT.delete(0,END)
        self.txtSTOK_OBAT.insert(END,obj.stok_obat)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        no_inv = self.txtNO_INV.get()
        nama_obat = self.txtNAMA_OBAT.get()
        jumlah_pembelian = self.txtJUMLAH_PEMBELIAN.get()
        harga = self.txtHARGA.get()
        stok_obat = self.txtSTOK_OBAT.get()       
        obj = Apotek()
        obj.no_inv = no_inv
        obj.nama_obat = nama_obat
        obj.jumlah_pembelian = jumlah_pembelian
        obj.harga = harga
        obj.stok_obat = stok_obat
        if(self.ditemukan==True):
            res = obj.updateByNO_INV(no_inv)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        no_inv = self.txtNO_INV.get()
        obj = Apotek()
        obj.no_inv = no_inv
        if(self.ditemukan==True):
            res = obj.deleteByNO_INV(no_inv)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormApotek(root, "Aplikasi Data Apotek",)
    root.mainloop()