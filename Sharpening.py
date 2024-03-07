import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
#Khai báo đường dẫn file hình
filehinh = "output2.jpg"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('output2.jpg', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL =Image.open(filehinh)
#Tạo một ảnh có cùng kích thước và mode với ảnh impPIL
Sharpening = Image.new(imgPIL.mode, imgPIL.size)
#Lấy kích thước của ảnh từ imgPIL
width = Sharpening.size[0]
height = Sharpening.size[1]
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
Laplace = np.array([[0,-1, 0],[-1, 4, -1],[0, -1, 0]]) #Vì sử dụng ma trận này nên hằng số c = 1
for x in range(1,width-1):
        for y in range(1,height-1):
            Rs = Gs = Bs = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                     R, G, B = imgPIL.getpixel((i, j))
                     Rs = Rs + R*Laplace[i - x + 1][j - y + 1]
                     Gs = Gs + G*Laplace[i - x + 1][j - y + 1]
                     Bs = Bs + B*Laplace[i - x + 1][j - y + 1]
            Rr, Gg, Bb = imgPIL.getpixel((x,y))
            sumR = Rs + Rr
            sumG = Gs + Gg
            sumB = Bs + Bb

            if sumR < 0:
                sumR = 0
            elif sumR > 255:
                sumR = 255
            if sumG < 0:
                sumG = 0
            elif sumG > 255:
                sumG = 255
            if sumB < 0:
                sumB = 0
            elif sumB > 255:
                sumB = 255
            Sharpening.putpixel((x,y),(sumB, sumG, sumR))

# Chuyển ảnh từ PIL sag OpenCV để hiển thị bằng OpenCV
Sharpening = np.array(Sharpening)
#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau Sharpening', Sharpening)
cv2.imshow('Anh goc',img)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hìnhd
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()