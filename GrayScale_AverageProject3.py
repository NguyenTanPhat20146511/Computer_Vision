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
average = Image.new(imgPIL.mode, imgPIL.size)
lightness = Image.new(imgPIL.mode, imgPIL.size)
luminance = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = average.size[0]
height = average.size[1]
width = lightness.size[0]
height = lightness.size[1]
width = luminance.size[0]
height = luminance.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
for x in range(width):
    for y in range(height):
        R, G, B = imgPIL.getpixel((x, y))
        #Công thức chuyển đổi ảnh màu RGB thành điểm ảnh mức xám 
        gray_average = np.uint8((R + G + B)/3)
        MIN = min(R, G, B)
        MAX = max(R, G, B)
        gray_lightness = np.uint8((MIN + MAX)/2)
        gray_luminance = np.uint8(0.2126*R+0.7152*G+0.0722*B)
        #Gán giá trị mức xám vừa tinh cho ảnh xám
        average.putpixel((x,y), (gray_average,gray_average,gray_average))
        lightness.putpixel((x,y), (gray_lightness,gray_lightness,gray_lightness))
        luminance. putpixel((x,y),(gray_luminance,gray_luminance,gray_luminance))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
anhmucxam_avergare = np.array(average)
anhmucxam_lightness = np.array(lightness)
anhmucxam_luminance = np.array(luminance)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc co gai Lena', img)
cv2.imshow('Anh muc xam dung Average', anhmucxam_avergare)
cv2.imshow('Anh muc xam dung Lightness', anhmucxam_lightness)
cv2.imshow('Anh muc xam dung Luminance', anhmucxam_luminance)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()