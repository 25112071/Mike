class NhanVien:
    def __init__(self, ten, luong1, hsl, luong_toi_da):
        self.ten = ten
        self.luong1 = luong1
        self.hsl = hsl
        self.luong_toi_da = luong_toi_da
        
    def tienluong(self):
        luong = self.luong1 * self.hsl
        return luong
    
    def thongtin(self):
        print(f"Ho ten: {self.ten}")
        print(f"Luong co ban: {self.luong1}")
        print(f"He so luonh: {self.hsl}")
        print(f"Luong toi da: {self.luong_toi_da}")

    def tangluong(self, tien):
        he_so_moi = self.hsl + tien
        luong_moi = self.luong1 * he_so_moi
        if luong_moi > self.luong_toi_da:
            print("Qua Han Muc Tang Luong")
            return False
        else:
            self.hsl = he_so_moi
            print(f"Da tang luong. He so luong moi: {self.hsl}")
            return True

    def get_ten(self):
        return self.ten
    
    def set_ten(self, ten):
        self.ten = ten

    def get_luong1(self):
        return self.luong1  
     
    def set_luong1(self, luong1):
        self.luong1 = luong1

    def get_hsl(self):
        return self.hsl
    
    def set_hsl(self, hsl):
         self.hsl = hsl

    def get_luong_toi_da(self):
        return self.luong_toi_da  
    
    def set_luong_toi_da(self, luong_toi_da):
         self.luong_toi_da = luong_toi_da 

nv1 = NhanVien("Giang A Duoi", 50, 4.0, 2000)
nv1.thongtin()
nv1.tangluong(5.5)
nv1.thongtin()
        
