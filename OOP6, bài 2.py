from abc import ABC, abstractmethod
class Tuoikhonghople(Exception):
    def __init__(self, tuoi):
        self.tuoi = tuoi
        super().__init__(f"tuoi {tuoi} khong hop le (18-60)")
class Backhonghople(Exception):         
    def __init__(self, bac):
        self.bac = bac
        super().__init__(f"bac {bac} ko hop le (1-10)")
class Canbo(ABC):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi):
        self._ten = ten
        self._gioi_tinh = gioi_tinh     
        self._dia_chi = dia_chi
        self.tuoi = tuoi                 
    @property
    def ten(self):
        return self._ten               
    @property
    def tuoi(self):
        return self._tuoi               
    @tuoi.setter
    def tuoi(self, tuoi):
        if 18 <= tuoi <= 60:            
            self._tuoi = tuoi
        else:
            raise Tuoikhonghople(tuoi)
    @property
    def gioi_tinh(self):
        return self.gioi_tinh
    @property
    def dia_chi(self):
        return self.dia_chi
   
    @abstractmethod
    def mota(self):
        pass
    def __str__(self):
         return (f"{self._ten} | {self._tuoi} tuổi"
                f" | {self._gioi_tinh} | {self._dia_chi}"
                f" | {self.mo_ta()}")    
    
    def __repr__(self):
           return f"{self.__class__.__name__}('{self._ten}', {self._tuoi})"
    def __eq__(self, other):
        if not isinstance(other, Canbo): return NotImplemented
        return self._ten == other._ten and self._tuoi == other._tuoi
    def __lt__(self, other):
        return self._ten < other._ten
    def __hash__(self):
        return hash((self._ten, self._tuoi))
    
class Congnhan(Canbo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    @property
    def bac(self):
        return self._bac                 

    @bac.setter
    def bac(self, bac):
        if 1 <= bac <= 10:               
            self._bac = bac
        else:
            raise Backhonghople(bac)     
        
    def mota(self):
        return f"Công nhân bậc {self.bac}"
    
class KySu(Canbo):
    def __int__(self, ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh
    @property 
    def nganh(self):
        return self.nganh
    def mota(self):
        return f"Kỹ sư ngành {self.nganh}"

class NhanVien(Canbo):
    def __int__(self, ten, tuoi, gioi_tinh, dia_chi, viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.viec = viec
    @property 
    def viec(self):
        return self.viec
    def mota(self):
        return f"Công việc của nhân viên {self.viec}"
    
class QLCB:
    def __init__(self):
        self.ds_can_bo = []

    def them_can_bo(self):
        print("\n=====THEM MOI CAN BO=====")
        loai = input("CHON LOAI CAN BO (1. Cong Nhan, 2. Ky Su, 3. Nhan Vien): ").strip()
        ten = input("Nhap Ten: ")
        tuoi = int(input("Nhap Tuoi: "))
        gioi_tinh = input("Nhap Gioi Tinh (Nam/Nu): ")
        dia_chi = input("Nhap Dia Chi: ")

        try:
            if loai == "1":
                bac = int(input("Nhap Bac: "))
                cb = Congnhan(ten, tuoi, gioi_tinh, dia_chi, bac)
            elif loai == "2":
                nganh = input("Nhap Nganh: ")
                cb = KySu(ten, tuoi, gioi_tinh, dia_chi, nganh)
            elif loai == "3":
                cong_viec = input("Nhap Cong Viec: ")
                cb = NhanVien(ten, tuoi, gioi_tinh, dia_chi, cong_viec)
            else:
                print("Loai can bo khong hop le!")
                return
            self.ds_can_bo.append(cb)    
            print("Them can bo thanh cong!")
        except (Tuoikhonghople, Backhonghople) as e:
            print(f"Loi: {e}")

    def tim_kiem_can_bo(self):           
        print("\n=====TIM KIEM CAN BO=====")
        tu_khoa = input("Nhap ho ten can tim: ").strip().lower()
        ket_qua = [cb for cb in self.ds_can_bo
                   if tu_khoa in cb.ten.lower()]
        if ket_qua:
            print(f"Tim thay {len(ket_qua)} can bo:")
            for i, cb in enumerate(ket_qua, 1):
                print(f"--- #{i} ---\n{cb}\n")
        else:
            print("Khong tim thay can bo nao.")

    def hien_thi_ds(self):
        if not self.ds_can_bo:
            print("\n  Danh sach trong!")
            return
        print(f"\n══ DANH SACH CAN BO ({len(self.ds_can_bo)} nguoi) ══")
        for i, cb in enumerate(self.ds_can_bo, 1):
            print(f"\n--- #{i} ---\n{cb}")

    def chay(self):
        while True:
            print("\n╔══════════════════════════╗")
            print("║   QUAN LY CAN BO         ║")
            print("╠══════════════════════════╣")
            print("║  1. Them moi can bo      ║")
            print("║  2. Tim kiem theo ten    ║")
            print("║  3. Hien thi danh sach   ║")
            print("║  4. Thoat                ║")
            print("╚══════════════════════════╝")
            chon = input("  Lua chon: ").strip()

            if   chon == "1": self.them_can_bo()       
            elif chon == "2": self.tim_kiem_can_bo()   
            elif chon == "3": self.hien_thi_ds()
            elif chon == "4":
                print("  Goodbye!")
                break
            else:
                print("  Lua chon khong hop le, thu lai.")


if __name__ == "__main__":
    ql = QLCB()
    ql.chay()
    
    



    