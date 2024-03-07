import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
#Khai báo đường dẫn file hình
filehinh = "E:\ComputerVision\Machine Vision Python\Lena.png"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Lena.png', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL =Image.open(filehinh)
#Tạo một ảnh có cùng kích thước và mode với ảnh impPIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang GrayScale
X = Image.new(imgPIL.mode, imgPIL.size)
Y = Image.new(imgPIL.mode, imgPIL.size)
Z = Image.new(imgPIL.mode, imgPIL.size)
XYZ = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = XYZ.size[0]
height = XYZ.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
for a in range(width):
    for b in range(height):
        R, G, B = imgPIL.getpixel((a, b))
        x = np.uint8(0.4124564*R + 0.3535761*G +0.1804375*B)
        y = np.uint8(0.2126729*R + 0.7151522*G +0.0721750*B)
        z = np.uint8(0.0193339*R + 0.1191920*G +0.9503041*B)
        #Gán giá trị mức xám vừa tính cho ảnh XYZ
        X.putpixel((a,b), (x,x,x))
        Y.putpixel((a,b), (y,y,y))
        Z. putpixel((a,b),(z,z,z))
        XYZ. putpixel((a,b),(z,y,x))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
Ximg = np.array(X)
Yimg = np.array(Y)
Zimg = np.array(Z)
XYZimg = np.array(XYZ)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh X', Ximg)
cv2.imshow('Anh Y', Yimg)
cv2.imshow('Anh Z', Zimg)
cv2.imshow('Anh XYZ', XYZimg)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()