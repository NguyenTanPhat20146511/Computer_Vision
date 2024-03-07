import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
#Khai báo đường dẫn file hình
filehinh = "D:\ComputerVision\Machine Vision Python\Lena.png"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Lena.png', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL =Image.open(filehinh)
#Tạo một ảnh có cùng kích thước và mode với ảnh impPIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang GrayScale
cyan = Image.new(imgPIL.mode, imgPIL.size)
magenta = Image.new(imgPIL.mode, imgPIL.size)
yellow = Image.new(imgPIL.mode, imgPIL.size)
black = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = cyan.size[0]
height = cyan.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
for x in range(width):
    for y in range(height):
        R, G, B = imgPIL.getpixel((x, y))
        MIN = min(R, G, B)
        #Gán giá trị mức xám vừa tính cho ảnh CMYK
        cyan.putpixel((x,y), (B, G, 0))
        magenta.putpixel((x,y), (B,0,R))
        yellow. putpixel((x,y),(0,G,R))
        black. putpixel((x,y),(MIN,MIN,MIN))
print(imgPIL.getpixel((30, 20)))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
C = np.array(cyan)
M = np.array(magenta)
P = np.array(yellow)
K = np.array(black)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau Cyan', C)
cv2.imshow('Anh mau Magenta', M)
cv2.imshow('Anh muc Yellow', P)
cv2.imshow('Anh muc Black', K)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()