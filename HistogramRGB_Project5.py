import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
import matplotlib.pyplot as plt #Thư viện dùng để ve biểu đồ
def TinhHistogram(HinhGoc):
    his = np.zeros((3,256))
    #Kích thước ảnh
    w = HinhGoc.size[0]
    h = HinhGoc.size[1]
    for x in range (w):
        for y in range (h):
            R, G, B = HinhGoc.getpixel((x,y))
            his[2,R] += 1
            his[1,G] += 1
            his[0,B] += 1
    return his
# Vẽ biểu đồ Histogram dùng thư viện matplotlib
def VeBieuDoHistogram(his):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram của ảnh xám', figsize=((w,h)), dpi = 100)
    trucX = np.zeros((3,256))
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, his[2,:], color = 'Red')
    plt.plot(trucX, his[1,:], color = 'Green')
    plt.plot(trucX, his[0,:], color = 'Blue')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng trị mức xám')
    plt.show()
#Chương trình chính
#Khai báo đường dẫn file hình
filehinh = r'bird_small.jpg'
# Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)
cv2.imshow("Anh Mau Goc Small Bird",img)
#Đọc ảnh dùng thư viện PIL
imgPIL = Image.open(filehinh)
#Tính Histogram
his = TinhHistogram(imgPIL)
#Hiển thị biểu đồ Histogram
VeBieuDoHistogram(his)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()

