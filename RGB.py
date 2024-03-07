import  cv2               #Sử dụng thư viện xử lý ảnh cho python
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('Lena.png', cv2.IMREAD_COLOR)

#Lấy kích thước của ảnh
width, height, channel = img.shape
print('width',height)
#Khai báo 3 biến để chứa hình 3 kênh màu RGBbit
red = np.zeros((width, height, 3), np.uint8) #Số 3 là 3 kên RGB, mỗi kênh có 8 bit
green = np.zeros((width, height, 3), np.uint8)
blue = np.zeros((width, height, 3), np.uint8)

#Ban đầu set zero cho tất cả điểm ảnh có trong 3 kênh trong mỗi hình
red[:] = [0, 0, 0] 
green[:] = [0, 0, 0] 
blue[:] = [0, 0, 0] 
#Mỗi hình là một ma trận 2 chiều nên sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh
for x in range(width):
    for y in range(height):
        #Lấy giá trị điểm ảnh tại vị trí (x,y)
        R = img[x,y,2]
        G = img[x,y,1]
        B = img[x,y,0]
        #Thiết lập màu cho các kênh
        red[x,y,2] = R
        green[x,y,1] = G
        blue[x,y,0] = B
#Hiển thị hình dùng thư viện OpenCV 
cv2.imshow('Hinh mau RGB goc co gai Lena', img)
cv2.imshow('Hinh mau RGB co gai Lena kenh Red', red)
cv2.imshow('Hinh mau RGB co gai Lena kenh Green', green)
cv2.imshow('Hinh mau RGB co gai Lena kenh Blue', blue)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()