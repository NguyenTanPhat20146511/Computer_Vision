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
Y = Image.new(imgPIL.mode, imgPIL.size)
Cb = Image.new(imgPIL.mode, imgPIL.size)
Cr = Image.new(imgPIL.mode, imgPIL.size)
YCbCr = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = Y.size[0]
height = Y.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
for a in range(width):
    for b in range(height):
        R, G, B = imgPIL.getpixel((a, b))
        y = np.uint8(16 + 65.738*R/256 + 129.057*G/256 +25.064*B/256)
        cr = np.uint8(128 -37.945*R/256 - 74.494*G/256 + 112.439*B/256)
        cb = np.uint8(128 + 112.439*R/256 - 94.154*G/256 - 18.285*B/256)
        #Gán giá trị mức xám vừa tính cho ảnh XYZ
        Y.putpixel((a,b), (y,y,y))
        Cb.putpixel((a,b), (cb,cb,cb))
        Cr. putpixel((a,b),(cr,cr,cr))
        YCbCr. putpixel((a,b),(cb,cr,y))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
yimg = np.array(Y)
cbimg = np.array(Cb)
crimg = np.array(Cr)
ycbcrimg = np.array(YCbCr)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh Y', yimg)
cv2.imshow('Anh Cb', cbimg)
cv2.imshow('Anh Cr', crimg)
cv2.imshow('Anh YCbCr', ycbcrimg)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()