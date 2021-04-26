1. Dự đoán gia tăng dân số:
- Dataset: số lượng em bé sinh ra mỗi ngày trong 10 năm (array(int)), số lượng người chết mỗi ngày trong 10 năm (array(int))
- Input: năm cần dự đoán (int)
- Output: tổng số dân tăng trong năm (int)
2. Dự đoán biến động chứng khoán:
- Dataset: con số tăng hay giảm của cổ phiếu trong 3 tháng gần đây theo từng giờ (array(float)), giờ/ngày/tháng/năm (array(int,int,int,int))
- Input: ngày cần dự đoán (int)
- Output: giá cổ phiếu trong ngày theo từng giờ (array(float))
3. Dự đoán doanh thu phim:
- Dataset: dữ liệu về các bộ phim khác cùng nhà sản xuất
- Input: chi phí quảng bá phim (float), độ nổi tiếng của diễn viên (int), thể loại phim (int), độ nổi tiếng của ấn phẩm liên quan (int) của bộ phim cần dự đoán
- Output: Doanh thu của bộ phim cần dự đoán (float)
4. Dự đoán lưu lượng mưa trong tuần tiếp theo:
- Dataset: dữ liệu lượng mưa trong 3 năm gần đây theo từng giờ: lưu lượng mưa (array(float)), ngày/tháng/năm (array(int,int,int))
- Input: ngày/tháng/năm hiện tại (int,int,int)
- Output: dự đoán lưu lượng mưa trong 1 tuần theo từng giờ (array(float))
5. Dự đoán tỉ lệ mắc bệnh di truyền:
- Input: số lượng người mắc bệnh di truyền trong gia đình (int), giới tính của các thành viên trong gia đình (array(int)), khoảng cách thế hệ giữa các thành viên và người cần dự đoán (array(int))
- Output: tỉ lệ mắc bệnh di truyền của người cần dự đoán (float)
 
