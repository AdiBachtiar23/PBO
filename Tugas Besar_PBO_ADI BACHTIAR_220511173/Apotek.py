# filename : Apotek.py
from db import DBConnection as mydb
class Apotek:
    def __init__(self):
        self.__id=None
        self.__no_inv=None
        self.__nama_obat=None
        self.__jumlah_pembelian=None
        self.__harga=None
        self.__stok_obat=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def no_inv(self):
        return self.__no_inv
        
    @no_inv.setter
    def no_inv(self, value):
        self.__no_inv = value
    @property
    def nama_obat(self):
        return self.__nama_obat
        
    @nama_obat.setter
    def nama_obat(self, value):
        self.__nama_obat = value
    @property
    def jumlah_pembelian(self):
        return self.__jumlah_pembelian
        
    @jumlah_pembelian.setter
    def jumlah_pembelian(self, value):
        self.__jumlah_pembelian = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    @property
    def stok_obat(self):
        return self.__stok_obat
        
    @stok_obat.setter
    def stok_obat(self, value):
        self.__stok_obat = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__no_inv,self.__nama_obat,self.__jumlah_pembelian,self.__harga,self.__stok_obat)
        sql="INSERT INTO Apotek (no_inv,nama_obat,jumlah_pembelian,harga,stok_obat) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__no_inv,self.__nama_obat,self.__jumlah_pembelian,self.__harga,self.__stok_obat, id)
        sql="UPDATE apotek SET no_inv = %s,nama_obat = %s,jumlah_pembelian = %s,harga = %s,stok_obat = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNO_INV(self, no_inv):
        self.conn = mydb()
        val = (self.__nama_obat,self.__jumlah_pembelian,self.__harga,self.__stok_obat, no_inv)
        sql="UPDATE apotek SET nama_obat = %s,jumlah_pembelian = %s,harga = %s,stok_obat = %s WHERE no_inv=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM apotek WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNO_INV(self, no_inv):
        self.conn = mydb()
        sql="DELETE FROM apotek WHERE no_inv='" + str(no_inv) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM apotek WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__no_inv = self.result[1]
        self.__nama_obat = self.result[2]
        self.__jumlah_pembelian = self.result[3]
        self.__harga = self.result[4]
        self.__stok_obat = self.result[5]
        self.conn.disconnect
        return self.result
    def getByNO_INV(self, no_inv):
        a=str(no_inv)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM apotek WHERE no_inv='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__no_inv = self.result[1]
           self.__nama_obat = self.result[2]
           self.__jumlah_pembelian = self.result[3]
           self.__harga = self.result[4]
           self.__stok_obat = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__no_inv = ''
           self.__nama_obat = ''
           self.__jumlah_pembelian = ''
           self.__harga = ''
           self.__stok_obat = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM apotek"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama_obat FROM apotek"
        self.result = self.conn.findAll(sql)
        return self.result