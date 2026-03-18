import math
r = 5
V = 4/3 * math.pi * r ** 3
print ("The tich cua hinh cau ban kinh 5 la: ", round(V, 2))

Giabia = 24.95
Sosach = 60
Phivanchuyen = 3 + 59 * 0.75
Tong = ((Giabia * 0.6)* Sosach + Phivanchuyen )
print ("Tong chi phi nhap sach la: ", round (Tong, 2), "k")

Start = 6 * 3600 + 52 * 60
Easypace = 8 * 60 + 15
Tempopace = 7 * 60 + 12
Totaltime = Tempopace * 3 + 2 * Easypace 
Finish = Start + Totaltime
Finishhour = Finish // 3600
Finishminute = (Finish % 3600) // 60
Finishsecond = Finish % 60
print (f"Finish time is: {Finishhour:02d}:{Finishminute:02d}:{Finishsecond:02d}")