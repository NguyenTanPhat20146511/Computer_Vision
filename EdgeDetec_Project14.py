import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
print("Enter threshold: ")
z = int(input())
def ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL):
    luminance = Image.new(imgPIL.mode, imgPIL.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = luminance.size[0]
    height = luminance.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên ta10 sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
    for x in range(width):
        for y in range(height):
            R, G, B = imgPIL.getpixel((x, y))
            gray_luminance = np.uint8(0.2126*R+0.7152*G+0.0722*B)
            #Gán giá trị mức xám vừa tinh cho ảnh xám
            luminance. putpixel((x,y),(gray_luminance,gray_luminance,gray_luminance))
    return luminance
def EdgeDetection(luminance,z):
    EdgeDetec = Image.new(luminance.mode, luminance.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = EdgeDetec.size[0]
    height = EdgeDetec.size[1]
    Sx = np.array([[-1,-2, -1],[0, 0, 0],[1, 2, 1]])
    Sy= np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])   
    #Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)                 
    for x in range(1,width-1):
        for y in range(1,height-1):
            gx = gy = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    R, G, B = imgPIL.getpixel((i, j))
                    gx = gx + R*Sx[i - x + 1][j - y + 1]
                    gy = gy + R*Sy[i - x + 1][j - y + 1]
            M = abs(gx) + abs(gy)
            if M > z:
                EdgeDetec.putpixel((x,y),(255, 255, 255))
            else:
                EdgeDetec.putpixel((x,y),(0, 0, 0)) 
    return EdgeDetec 
#Khai báo đường dẫn file hình
filehinh = "D:\ComputerVision\Machine Vision Python\LenaOrg.jpg"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Lena.png', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)
luminance = ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL)
EdgeDetec = EdgeDetection(luminance, z)
EdgeDetec = np.array(EdgeDetec)
cv2.imshow('Anh sau khi EdgeDetection: ', EdgeDetec)
cv2.imshow('Anh goc',img)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()