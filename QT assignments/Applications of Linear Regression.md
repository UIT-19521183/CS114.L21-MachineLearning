
## Bài toán 1: Dự đoán dân số Việt Nam:
- Dataset: dân số Việt Nam từ năm 1950 đến 2020: năm (array(int)), dân số (array(int)) 
- Input: năm cần dự đoán (int)
- Output: dân số Việt Nam tại năm cần dự đoán
- Cách thu thập data: thu thập data từ các trang web về dân số Việt Nam (vd: https://danso.org/viet-nam/)
- Cách xử lý data: đưa data về 2 cột là năm (int) và dân số (int)
## Bài toán 2: Dự đoán giá cổ phiếu:
- Dataset: giá cổ phiếu của doanh nghiệp cần dự đoán theo giây trong vòng 3 giờ gần đây: giờ (array(int)), phút (array(int)), giây (array(int)), giá cổ phiếu (array(float))
- Cách thu thập data: thu thập data từ các trang web về cổ phiếu, chứng khoán,... (vd: https://iboard.ssi.com.vn/)
- Cách xử lý data: 
  - Chuyển giờ/phút/giây từ dạng văn bản về thành mảng 3 số nguyên
  - Đưa data thành 4 cột giờ (int), phút(int), giây(int), giá cổ phiếu(float) 
- Input: giờ, phút, giây cần dự đoán giá cổ phiếu (int,int,int)
- Output: giá cổ phiếu trong giờ, phút, giây cần dự đoán (float)
## 3. Dự đoán doanh thu phim:
- Dataset: dữ liệu về các bộ phim khác cùng nhà sản xuất
- Input: chi phí quảng bá phim (float), độ nổi tiếng của diễn viên (int), thể loại phim (int), độ nổi tiếng của ấn phẩm liên quan (int) của bộ phim cần dự đoán
- Output: Doanh thu của bộ phim cần dự đoán (float)
## 4. Dự đoán lưu lượng mưa trong tuần tiếp theo:
- Dataset: dữ liệu lượng mưa trong 3 năm gần đây theo từng giờ: lưu lượng mưa (array(float)), ngày/tháng/năm (array(int,int,int))
- Input: ngày/tháng/năm hiện tại (int,int,int)
- Output: dự đoán lưu lượng mưa trong 1 tuần theo từng giờ (array(float))
## 5. Dự đoán tỉ lệ mắc bệnh di truyền:
- Input: số lượng người mắc bệnh di truyền trong gia đình (int), giới tính của các thành viên trong gia đình (array(int)), khoảng cách thế hệ giữa các thành viên và người cần dự đoán (array(int))
- Output: tỉ lệ mắc bệnh di truyền của người cần dự đoán (float)
 
