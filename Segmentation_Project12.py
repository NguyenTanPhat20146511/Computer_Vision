import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
#Khai báo đường dẫn file hình
filehinh = "D:\ComputerVision\Machine Vision Python\LenaOrg.jpg"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('LenaOrg.jpg', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL =Image.open(filehinh)
#Tạo một ảnh có cùng kích thước và mode với ảnh impPIL
Segmentation = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = Segmentation.size[0]
height = Segmentation.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
aR = aG = aB = 0
print('Enter x1:')
x1 = int(input())
print('Enter x2:')
x2 = int(input())
print('Enter y1:')
y1 = int(input())
print('Enter y2:')
y2 = int(input())
print("Please enter threshold: ")
thre = int(input())
for x in range(x1,x2):
        for y in range(y1,y2):
             R, G, B = imgPIL.getpixel((x, y))
             aR = aR + R
             aG = aG + G
             aB = aB + B
aR = aR/ ((x2 - x1)*(y2 - y1))
aG = aG/ ((x2 - x1)*(y2 - y1))
aB = aB/ ((x2 - x1)*(y2 - y1))
for i in range(width):
    for j in range(height):
        zR, zG, zB = imgPIL.getpixel((i, j))
        z = np.sqrt((zR - aR)**2 +(zG - aG)**2 + (zB - aB)**2 )
        if z > thre: 
            Segmentation.putpixel((i,j),(zB, zG, zR))
        else:
            Segmentation.putpixel((i,j),(255, 255, 255))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
Segmentation = np.array(Segmentation)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau Segmentation', Segmentation)
cv2.imshow('Anh goc',img)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()