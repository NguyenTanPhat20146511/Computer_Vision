import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
import math
#Khai báo đường dẫn file hình
filehinh = "E:\ComputerVision\Machine Vision Python\Lena.png"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Lena.png', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL =Image.open(filehinh)
#Tạo một ảnh có cùng kích thước và mode với ảnh impPIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang GrayScale
Saturation = Image.new(imgPIL.mode, imgPIL.size)
Value = Image.new(imgPIL.mode, imgPIL.size)
Hue = Image.new(imgPIL.mode, imgPIL.size)
HSV = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = HSV.size[0]
height =HSV.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
for x in range(width):
    for y in range(height):
        R, G, B = imgPIL.getpixel((x, y))
        t1 = ((R - G) + (R - B)) / 2
        t2 = math.sqrt((R - G) * (R - G) + (R - B) * (G - B))
        theta = math.acos(t1/t2)
        if (B <= G):
         H = theta
        else :
            H = 2 * math.pi - theta
        H = np.uint8(H * 180 / math.pi)
        S = 1 - 3 * min(R, G, B) / (R + G + B)
        #  Do giá trị tính ra của S nằm trong khoảng [0, 1]
        # Để hàm có thể hiển thị được thì mình phải Convert S sang khoảng
        # giá trị [0, 255]. Công thức dưới đây giúp chuyển đổi từ rank [0, 1] sang rank [0, 255]
        Sa = np.uint8(S * 255)
        V = np.uint(max(R, G, B))
        #Gán giá trị mức xám vừa tính cho ảnh HSI
        Hue.putpixel((x,y), (H,H,H))
        Saturation.putpixel((x,y), (Sa,Sa,Sa))
        Value. putpixel((x,y),(V,V,V))
        HSV. putpixel((x,y),(V,Sa,H))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
H = np.array(Hue)
S = np.array(Saturation)
V = np.array(Value)
Hsv = np.array(HSV)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Kenh mau Hue', H)
cv2.imshow('Kenh mau Saturation', S)
cv2.imshow('Kenh mau Value', V)
cv2.imshow('Kenh mau HSV', Hsv)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()