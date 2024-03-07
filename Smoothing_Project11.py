import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
import matplotlib.pyplot as plt #Thư viện dùng để vẽ biểu đồ
def ColorImageSmoothing3x3(imgPIL):
    Smoothing3x3 = Image.new(imgPIL.mode, imgPIL.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = Smoothing3x3.size[0]
    height = Smoothing3x3.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
    for a in range(1,width-1):
        for b in range(1,height-1):
            Rs = Gs = Bs = 0
            for x in range (a-1,a+2):
                for y in range (b-1,b+2):
                     R, G, B = imgPIL.getpixel((x, y))
                     Rs = Rs + R
                     Gs = Gs + G
                     Bs = Bs + B
            K = 3*3       
            Rs = int(Rs/K)
            Gs = int(Gs/K)
            Bs = int(Bs/K)
            Smoothing3x3.putpixel((a,b),(Bs, Gs, Rs))
    return Smoothing3x3
def ColorImageSmoothing5x5(imgPIL):
    Smoothing5x5 = Image.new(imgPIL.mode, imgPIL.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = Smoothing5x5.size[0]
    height = Smoothing5x5.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
    for a in range(2,width-2):
        for b in range(2,height-2):
            Rs = Gs = Bs = 0
            for x in range (a-2,a+3):
                for y in range (b-2,b+3):
                     R, G, B = imgPIL.getpixel((x, y))
                     Rs = Rs + R
                     Gs = Gs + G
                     Bs = Bs + B
            K = 5*5       
            Rs = int(Rs/K)
            Gs = int(Gs/K)
            Bs = int(Bs/K)
            Smoothing5x5.putpixel((a,b),(Bs, Gs, Rs))
    return Smoothing5x5
def ColorImageSmoothing7x7(imgPIL):
    Smoothing7x7 = Image.new(imgPIL.mode, imgPIL.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = Smoothing7x7.size[0]d    height = Smoothing7x7.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
    for a in range(3,width-3):
        for b in range(3,height-3):
            Rs = Gs = Bs = 0
            for x in range (a-3,a+4):
                for y in range (b-3,b+4):
                     R, G, B = imgPIL.getpixel((x, y))
                     Rs = Rs + R
                     Gs = Gs + G
                     Bs = Bs + B
            K = 7*7       
            Rs = int(Rs/K)
            Gs = int(Gs/K)
            Bs = int(Bs/K)
            Smoothing7x7.putpixel((a,b),(Bs, Gs, Rs))
    return Smoothing7x7
def ColorImageSmoothing9x9(imgPIL):
    Smoothing9x9 = Image.new(imgPIL.mode, imgPIL.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = Smoothing9x9.size[0]
    height = Smoothing9x9.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
    for a in range(4,width-4):
        for b in range(4,height-4):
            Rs = Gs = Bs = 0
            for x in range (a-4,a+5):
                for y in range (b-4,b+5):
                     R, G, B = imgPIL.getpixel((x, y))
                     Rs = Rs + R
                     Gs = Gs + G
                     Bs = Bs + B
            K = 9*9       
            Rs = int(Rs/K)
            Gs = int(Gs/K)
            Bs = int(Bs/K)
            Smoothing9x9.putpixel((a,b),(Bs, Gs, Rs))
    return Smoothing9x9
#Chương trình chính
#Khai báo đường dẫn file hình
filehinh = r'LenaOrg.jpg'
#Đọc ảnh dùng thư viện PIL
imgPIL = Image.open(filehinh)
Smoothing3x3 = ColorImageSmoothing3x3(imgPIL)
Smoothing5x5 = ColorImageSmoothing5x5(imgPIL)
Smoothing7x7 = ColorImageSmoothing7x7(imgPIL)
Smoothing9x9 = ColorImageSmoothing9x9(imgPIL)
a = np.array(Smoothing3x3)
b = np.array(Smoothing5x5)
c = np.array(Smoothing7x7)
d = np.array(Smoothing9x9)
cv2.imshow("Hinh anh da duoc lam muot 3x3", a)
cv2.imshow("Hinh anh da duoc lam muot 5x5", b)
cv2.imshow("Hinh anh da duoc lam muot 7x7", c )
cv2.imshow("Hinh anh da duoc lam muot 9x9", d)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()
