import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
#Khai báo đường dẫn file hình
filehinh = "D:\ComputerVision\Machine Vision Python\LenaOrg.jpg"
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('LenaOrg.jpg', cv2.IMREAD_COLOR)
#Đọc ảnh màu dùng thư viện PIL. Ảnh PIL này chúng ta sẽ dùng để tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)
#Tạo một ảnh có cùng kích thước và mode với ảnh impPIL
EdgeDetec = Image.new(imgPIL.mode, imgPIL.size)
print("Enter threshold: ")
z = int(input())
#Lấy kích thước của ảnh từ imgPIL
width = EdgeDetec.size[0]
height = EdgeDetec.size[1]
Sx = np.array([[-1,-2, -1],[0, 0, 0],[1, 2, 1]])
Sy= np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])   
#Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)                 
for x in range(1,width-1):
	for y in range(1,height-1):
		gxR = gyR = gxG = gyG = gxB = gyB = 0
		for i in range(x-1,x+2):
			for j in range(y-1,y+2):
				R, G, B = imgPIL.getpixel((i, j))
				gxR = gxR + R*Sx[i - x + 1][j - y + 1]
				gyR = gyR + R*Sy[i - x + 1][j - y + 1]
				gxG = gxG + G*Sx[i - x + 1][j - y + 1]
				gyG = gyG + G*Sy[i - x + 1][j - y + 1]
				gxB = gxB + B*Sx[i - x + 1][j - y + 1]
				gyB = gyB + B*Sy[i - x + 1][j - y + 1]
		gxx = np.square(gxR)+ np.square(gxG) + np.square(gxB)
		gyy = np.square(gyR)+ np.square(gyG) + np.square(gyB)
		gxy = gxR*gyR + gxG*gyG + gxB*gyB
		theta = 1/2 * np.arctan2(2*gxy,(gxx - gyy))
		F = np.sqrt(np.abs(1/2 * ((gxx + gyy) + (gxx - gyy) * np.cos(2*theta) + (2*gxy*np.sin(2*theta)))))
		if F > z:
			EdgeDetec.putpixel((x,y),(255, 255, 255))
		else:
			EdgeDetec.putpixel((x,y),(0, 0, 0)) 
EdgeDetec = np.array(EdgeDetec)
cv2.imshow('Anh sau khi EdgeDetection: ', EdgeDetec)
cv2.imshow('Anh goc',img)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()