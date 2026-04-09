class CanBo:
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi):
        self._ten = ten 
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi
    def loai_cb(self):
        return "Can Bo"
    def hien_thi(self):
        print(f"Ten: {self._ten}")
        print(f"Tuoi: {self._tuoi}")
        print(f"Gioi Tinh: {self._gioi_tinh}")
        print(f"Dia Chi: {self._dia_chi}")
class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__bac = bac
class KySu(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh = nganh
class NhanVien(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
    def loai_cb(self):            #method override
        return "Nhan Vien"

    def hien_thi(self):
        super().hien_thi()
        print(f"Cong Viec: {self.__cong_viec}")
    #cn1 = CongNhan("Tran Thi B", 25, "Nu", "Hai Phong", 3)
    #ks1 = KySu("Le Van C", 28, "Nam", "Da Nang", "CNTT")
    #nv1 = NhanVien("Pham Thi D", 22, "Nu", "Hue", "Van Phong")
    #cb1.hien_thi()
    #cn1.hien_thi()
    #ks1.hien_thi()  
    #nv1.hien_thi()    



class QLCB:
    def __init__(self):
        self.ds_can_bo = []
    def them_can_bo(self):
        print("\n=====THEM MOI CAN BO=====")
        print("loai can bo: 1. Cong Nhan, 2. Ky Su, 3. Nhan Vien")
        Loai =input("CHON LOAI CAN BO:1. Cong Nhan, 2. Ky Su, 3. Nhan Vien:").strip()
        ten= input("Nhap Ten:")
        tuoi= int(input("Nhap Tuoi:"))
        gioi_tinh= input("Nhap Gioi Tinh:Nam/Nu:")
        dia_chi= input("Nhap Dia Chi:")
        if Loai == "1":
            bac= int(input("Nhap Bac:"))
            cn=CongNhan(ten, tuoi, gioi_tinh, dia_chi, bac)
        elif Loai == "2":
            nganh= input("Nhap Nganh:")
            ks=KySu(ten, tuoi, gioi_tinh, dia_chi, nganh)
        elif Loai == "3":
            cong_viec= input("Nhap Cong Viec:")
            nv=NhanVien(ten, tuoi, gioi_tinh, dia_chi, cong_viec)      
        else:
            print("Loai can bo khong hop le!")
            return
        self.ds_can_bo.append(cn)
        print("Them can bo thanh cong!")
        def tim_kiem_can_bo(self):
            print("\n=====TIM KIEM CAN BO=====")      
        tu_khoa = input("Nhập họ tên cần tìm: ").strip().lower()
        ket_qua = [cb for cb in self.danh_sach
                   if tu_khoa in cb.ho_ten.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} cán bộ:\n")
            for i, cb in enumerate(ket_qua, 1):
                print(f"--- #{i} ---")
                cb.hien_thi()
                print()
        else:
            print("Không tìm thấy cán bộ nào phù hợp.")
    def hien_thi_ds(self):
        if not self.__ds_can_bo:
            print("\n  Danh sách trống!")
            return
        print(f"\n══ DANH SÁCH CÁN BỘ ({len(self.__ds_can_bo)} người) ══")
        for i, cb in enumerate(self.__ds_can_bo, 1):
            print(f"\n--- #{i} ---")
            cb.hien_thi()        
    def chay(self):
        while True:
            print("\n╔══════════════════════════╗")
            print("║   QUẢN LÝ CÁN BỘ           ║")
            print("╠═══════════════════════════ ╣")
            print("║  1. Thêm mới cán bộ        ║")
            print("║  2. Tìm kiếm theo tên      ║")
            print("║  3. Hiển thị danh sách     ║")
            print("║  4. Thoát                  ║")
            print("╚═══════════════════════════ ╝")

            chon = input("  Lựa chọn: ").strip()

            if   chon == "1": self.them_moi()
            elif chon == "2": self.tim_kiem()
            elif chon == "3": self.hien_thi_ds()
            elif chon == "4":
                print("  Goodbye!")
                break
            else:
                print("  Invalid choice!,please try again.")
if __name__ == "__main__":
    ql = QLCB()
    ql.chay()        