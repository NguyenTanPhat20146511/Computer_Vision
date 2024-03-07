import  cv2               #Sử dụng thư viện xử lý ảnh cho python
from PIL import Image     #Sử dụng thư viện xử lý ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau
import numpy as np        #Thư viện toán học đặc biệt là các tính toán ma trận
import matplotlib.pyplot as plt #Thư viện dùng để ve biểu đồ
def ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL):
    luminance = Image.new(imgPIL.mode, imgPIL.size)
    #Lấy kích thước của ảnh từ imgPIL
    width = luminance.size[0]
    height = luminance.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên ta sẽ dùng 2 vòng for để đọc hết tất cả các điểm ảnh (pixel)
    for x in range(width):
        for y in range(height):
            R, G, B = imgPIL.getpixel((x, y))
            gray_luminance = np.uint8(0.2126*R+0.7152*G+0.0722*B)
            #Gán giá trị mức xám vừa tinh cho ảnh xám
            luminance. putpixel((x,y),(gray_luminance,gray_luminance,gray_luminance))
    return luminance
def TinhHistogram(HinhXamPIL):
    # Mỗi pixel có giá trị từ 0 - 255, nên phải phải khai báo một mảng có 
    #256 phần tử để chứa số đếm của các pixel có cùng giá trị'
    his = np.zeros(256)
    #Kích thước ảnh
    w = HinhXamPIL.size[0]
    h = HinhXamPIL.size[1]
    for x in range (w):
        for y in range (h):
            gR, gG, gB = HinhXamPIL.getpixel((x,y))
            # Giá trị của Gray tính ra cũng chính là phần tử thứ Gray
            # trong mảng his đã được khai báo ở trên, sẽ tăng số đếm
            # của phần tử thứ gray lên 1
            his[gR] += 1
    return his
# Vẽ biểu đồ Histogram dùng thư viện matplotlib
def VeBieuDoHistogram(his):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram của ảnh xám', figsize=((w,h)), dpi = 100)
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256)
    print(trucX)
    plt.plot(trucX, his, color = 'red')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng trị mức xám')
    plt.show()
#Chương trình chính
#Khai báo đường dẫn file hình
filehinh = r'bird_small.jpg'
#Đọc ảnh dùng thư viện PIL
imgPIL = Image.open(filehinh)
#Chuyển sang mức xám
HinhXamPIL = ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL)
#Tính Histogram
his = TinhHistogram(HinhXamPIL)
#Chuyển đổi ảnh PIL sang OpenCV để hiển thị
HinhXamCV = np.array(HinhXamPIL)
cv2.imshow("Anh Muc Xam", HinhXamCV)
#Hiển thị biểu đồ Histogram
VeBieuDoHistogram(his)
#Bấm phím bất kỳ để đống cửa sổ hiển thị hình
cv2.waitKey(0)
#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị
cv2.destroyAllWindows()

