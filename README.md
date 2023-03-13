# CS114.L21 - Machine Learning
## BẢNG MỤC LỤC
* [ Giới thiệu môn học](#gioithieumonhoc)
* [ Giảng viên hướng dẫn](#giangvien)
* [ Thành viên nhóm](#thanhvien)
* [ Đồ án môn học](#doan)
## GIỚI THIỆU MÔN HỌC
<a name="gioithieumonhoc"></a>
* **Tên môn học**: Máy học - Machine Learning
* **Mã môn học**: CS114
* **Lớp học**: CS114.L21
* **Ngày bắt đầu**: 01/03/2021
* **Năm học**: 2020-2021

## GIẢNG VIÊN HƯỚNG DẪN
<a name="giangvien"></a>
* PGS.TS. **Lê Đình Duy** - *duydl@uit.edu.vn*
* ThS. **Phạm Nguyễn Trường An** - *truonganpn@uit.edu.vn*

## THÀNH VIÊN NHÓM
<a name="thanhvien"></a>
| STT | Họ tên | MSSV | GitHub | Email |
| :---: | -------------- | ----- | ----- | ----- |
| 1 | Nguyễn Thị Thúy An | 19521183 | [UIT19521183](https://github.com/UIT-19521183)   | 19521183@gm.uit.edu.vn | 
| 2 | Nguyễn Lâm Thảo Vy | 19522547 | [UIT19522547](https://github.com/UIT19522547)     | 19522547@gm.uit.edu.vn |
| 3 | Huỳnh Đỗ Tấn Thành | 19522227 | [UIT19522227](https://github.com/HuynhDoTanThanh) | 19522227@gm.uit.edu.vn |  

## ĐỒ ÁN MÔN HỌC
<a name="doan"></a>
### **1.Mô tả bài toán**
* **Bối cảnh ứng dụng:** Trong thời đại số hóa, việc đọc hình ảnh chuyển thành dữ liệu có thể xử lý thao tác được trên máy tính không còn xa lạ nữa. Ví dụ như đọc ảnh chưng minh nhân dân chẳng hạn, hay là giấy khai sinh, ... Nhóm chúng em thực hiện đồ án số hóa tủ sách này với mong muốn có thể giải quyết được việc thay vì thao tác nhập tay để lưu thông tin của quyển sách ta có thể đọc từ ảnh chụp.
* **Ưu điểm:** Giúp giảm thao tác nhập liệu khi có một kho thư viện khá lớn (vài ngàn cuốn sách) khi muốn lưu thông tin sách lên máy.
* **Nhược điểm:** Việc số hóa được một cuốn sách cũng khá là phức tạp. Độ chính xác bị giảm dần qua nhiều thao tác. Có nhìu cuốn sách không thể đọc được như chữ bị khuyết, bị che, chứ lồng vào nhau khá nhiều, chữ xiêng nhiều, chữ chìm, chữ đan xen nhau,... Nên việc số hóa chỉ nên đối với các sách đơn giản hơn.

* **INPUT:** Ảnh chụp bìa sách từ camera với chất lượng ảnh tối thiểu là Full HD (720x960).
* **OUTPUT:** File CSV chứa thông tin của sách gồm 7 trường dữ liệu:
  * tên file
  * Tên sách
  * Tên tác giả
  * Nhà xuất bản
  * Tập
  * Người dịch
  * Tái bản

* **Pipeline:**
<a align = center>
  <img src='https://drive.google.com/uc?export=view&id=1vh6oQbLgfoV850cQYrZt_IzT4tpm4XIA' align = center>
  <div style=width: 130px; align = center>Pipeline bookcase digitization</div>

### **2.Mô tả dữ liệu:**
#### **2.1 Thu thập dữ liệu:**
  * 500 ảnh bìa sách được chụp dưới nền đen.
  * 10000 ảnh bìa sách được crawl từ nhiều nguồn khác nhau như:
    * [Nhà xuất bản Trẻ](https://www.nxbtre.com.vn/)
    * [Nhà xuất bản Kim Đồng](https://nxbkimdong.com.vn/)
    * [Nhà xuất bản ĐHQG-TPHCM](https://vnuhcmpress.edu.vn/)
    * [Nhà xuất bản Hà Nội](http://www.nxbhanoi.com.vn/)
    * [Nhà xuất bản Đà Nẵng](https://nxbdanang.vn/)
    * [Nhà xuất bản Quân đội nhân dân](http://nxbqdnd.com.vn/)
    * [Nhà xuất bản khoa học xã hội](http://nxbkhxh.vass.gov.vn/)
    * [Nhà xuất bản thanh niên](https://www.nhaxuatbanthanhnien.vn/)
    * [Nhà xuất bản tư pháp](https://nxbtuphap.moj.gov.vn/)
    * [Nhà sách tiki](tiki.vn/sach-truyen-tieng-viet/c316?page=1&src=c.8322.hamburger_menu_fly_out_banner)
  * 45000 dòng text được cắt ra từ chính những sách đã thu thập được.
  * 100000 dòng text được generate từ nhiều font chữ khác nhau.

#### **2.2 Dán nhãn dữ liệu**
  * Vì thời gian thực hiện đồ án có hạn nên nhóm em đã dán nhãn được:
    * 6000 ảnh bìa sách phục vụ train model YOLO ([link dán nhãn](http://makesense.ai/))
    * 45000 dòng text để phục vụ train model VietOCR ([link dán nhãn](https://www.robots.ox.ac.uk/~vgg/software/via/via.html))

#### **2.3 Thao tác xử lý dữ liệu:**
  * Đầu tiên với ảnh thô chụp từ camera dưới nền đen ta dễ dàng contour ảnh từ một số bước xử lý dữ liệu:
    * Resize ảnh.
    * Convert ảnh thành Gray Scale.
    * Sử dụng Gaussian Blur và Candy Blur.
    * [Find contour](https://pythonexamples.org/python-opencv-cv2-find-contours-in-image/).
    * Lấy ra contour lớn nhất.
    * Lấy ra bốn điểm của countour và cắt ảnh bằng [cv2.warpPerspective](https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87)

  * Tiếp theo đến việc detect object, nhóm em sử dụng model deeplearning của [YOLOv5](https://github.com/ultralytics/yolov5)
      * Với 6 label:
        * 0: Tên sách
        * 1: Tên tác giả
        * 2: Nhà xuất bản
        * 3: Tập
        * 4: Người dịch
        * 5: Tái bản
      * Cắt ảnh ra từ những object đã được predict của phần object detection ở trên.
  * Craft:
    * Nhóm em sử dụng model deeplearning đã được train sẵn từ nhiều ngôn ngữ khác nhau: [Craft text detector](https://github.com/clovaai/CRAFT-pytorch) với:
      * text_threshold=0.7
      * link_threshold=0.4
      * low_text=0.3
      * long_size=1280
  * OCR:
    * Chuyển ảnh thành Gray Scale.
    * Nhóm em sử dụng model [VietOCR](https://github.com/pbcquoc/vietocr).
    * Sử dụng xoay ảnh để có thể đọc được cả chữ dọc.
    * Xử lý xóa các text không liên quan trong tên sách do các object khác nhau bị chồng lên nhau, ví dụ như trong việc tên sách có cả tên tác giả nếu như trong object tên sách có cả tên tác giả thì ta sẽ xóa tên tác giả có trong tên sách.
  * Lưu kết quả:
    * Thêm vào dataframe và lưu dưới dạng file csv.

#### **2.4 Phân chia (split) - train/dev/test**
 * Với model YOLOv5 
    * Training data (85%): 5951 labels (tỉ lệ train/val là 8/2)​
        * Tập train: 4745 labels​
        * Tập val: 1206 labels​
    * Testing data (15%): 1031 labels
 * Với model VietOCR thì nhóm em để chia train/val theo tỉ lệ 80/20.
 * Đối với việc đánh giá thì em dành những ảnh chụp thực tế chưa dán nhãn cả phần VietOCR và YOLO chia làm 3 phần: easy(106), medium(147), hard(71)
 ### **3.Data:**
 * Data YOLO: https://drive.google.com/file/d/1wmFvdessDGsXND22T3sdgNaizbmzvqOT/view?usp=sharing
 * Data OCR: https://drive.google.com/uc?id=1LqaWeO2qOgZIO3LdrPtntOioQJWdwA-V
 ### **4.Trainning:** Quá trình trainning chia làm hai phần:
 * Object-detection (YOLO): <a href="https://colab.research.google.com/drive/1JnxkR9EeLXjfqhK-OlJXjkeWgB1yE1xP?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
 * OCR (VietOCR): <a href="https://colab.research.google.com/drive/1DG0j27Ll73Pw0z66NKS1zl56JhCFDigO?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

