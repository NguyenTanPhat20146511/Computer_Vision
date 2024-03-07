import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
#Khai báo đường dẫn file hình
filehinh = r'Lena.png'
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Lena.png', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL =Image.open(filehinh)
#Tọ một ảnh có cùng kích thước và mode với ảnh impPIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang GrayScale
binary = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = binary.size[0]
height = binary.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
for x in range(width):
    for y in range(height):
        R, G, B = imgPIL.getpixel((x, y))
        #Công thức chuyển đổi ảnh màu RGB thành điểm ảnh mức xám 
        gray_binary = np.uint8(0.2126*R+0.7152*G+0.0722*B)
        if gray_binary > 100:
            gray_binary = 255
        else:
            gray_binary = 0
        #Gán giá trị mức xám vừa tinh cho ảnh xám
        binary. putpixel((x,y),(gray_binary,gray_binary,gray_binary))
# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
anhmucxam_binary = np.array(binary)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc co gai Lena', img)
cv2.imshow('Anh Nhi Phan', anhmucxam_binary)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()