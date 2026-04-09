from abc import ABC, abstractmethod

# 1. Định nghĩa các Exception tùy chỉnh
class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass

# 2. Lớp cha HangHoa
class HangHoa(ABC):
    def __init__(self, ma_hang, ten, gia):
        # Gán trực tiếp vào biến private (có dấu gạch dưới)
        self._ma_hang = ma_hang
        self._ten = ten
        self.gia = gia  # Gọi đến setter của gia để kiểm tra điều kiện

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten(self):
        return self._ten

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe("Giá hàng hóa không được âm!")
        self._gia = value

    @abstractmethod 
    def loai_hang(self): # Thêm self
        pass
    
    @abstractmethod
    def inTTin(self): # Thêm self
        pass        
 
    def __str__(self):
        # Sửa self.ten_hang thành self.ten
        return f"[{self.loai_hang()}] Mã: {self.ma_hang}, Tên: {self.ten}, Giá: {self.gia}"
    
    def __eq__(self, other):
        if isinstance(other, HangHoa):
            return self.ma_hang == other.ma_hang
        return False
    
    def __lt__(self, other):
        return self.gia < other.gia
    
    def __hash__(self): 
        return hash(self.ma_hang)


# 3. Các lớp con (Kế thừa từ HangHoa)
class Dienmay(HangHoa):
    def loai_hang(self):
        return "Dien May"
    def inTTin(self):
        print(f"Hang Dien May: {self}")

class SanhSu(HangHoa):
    def loai_hang(self):
        return "Sanh Su"
    def inTTin(self):
        print(f"Hang Sanh Su: {self}")

class ThucPham(HangHoa):
    def loai_hang(self):
        return "Thuc Pham"
    def inTTin(self):
        print(f"Hang Thuc Pham: {self}")


# 4. Lớp Quản lý
class QuanLyHangHoa():
    def __init__(self):
       self.danh_sach = []
    
    def them_hang(self, hang):
        if any(h.ma_hang == hang.ma_hang for h in self.danh_sach):
            raise MaHangTrungLap(f"Mã {hang.ma_hang} đã tồn tại")
        self.danh_sach.append(hang)

    def hien_thi(self):
        for sp in self.danh_sach:
            sp.inTTin() # Bỏ print() bao bên ngoài vì hàm inTTin() đã tự in

    def luu_tru(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for sp in self.danh_sach:
                # Sửa sp.ten_hang thành sp.ten
                f.write(f"{sp.ma_hang},{sp.ten},{sp.gia}\n")

# --- CHẠY THỬ CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    ql = QuanLyHangHoa()
    
    # Thêm hàng hóa
    sp1 = Dienmay("DM01", "Tivi Sony", 15000000)
    sp2 = ThucPham("TP01", "Gạo ST25", 250000)
    sp3 = SanhSu("SS01", "Chén sứ Hải Dương", 50000)
    
    ql.them_hang(sp1)
    ql.them_hang(sp2)
    ql.them_hang(sp3)
    
    # Hiển thị
    print("--- Danh sách hàng hóa ---")
    ql.hien_thi()
    
    # Lưu file
    ql.luu_tru("data_hanghoa.txt")
    print("\nĐã lưu danh sách vào file data_hanghoa.txt")