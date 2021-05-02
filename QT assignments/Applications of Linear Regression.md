
## Bài toán 1: Dự đoán dân số Việt Nam:
- Dataset: dân số Việt Nam từ năm 1950 đến 2020: năm (array(int)), dân số (array(int))
- Cách thu thập data: thu thập data từ các trang web về dân số Việt Nam (vd: https://danso.org/viet-nam/)
- Cách xử lý data: đưa data về 2 cột là năm (int) và dân số (int) và lưu vào file .csv
- Input: năm cần dự đoán (int)
- Output: dân số Việt Nam tại năm cần dự đoán (int)
## Bài toán 2: Dự đoán giá cổ phiếu:
- Dataset: giá cổ phiếu của doanh nghiệp cần dự đoán theo giây trong vòng 3 giờ gần đây: giờ (array(int)), phút (array(int)), giây (array(int)), giá cổ phiếu (array(float))
- Cách thu thập data: thu thập data từ các trang web về cổ phiếu, chứng khoán,... (vd: https://iboard.ssi.com.vn/)
- Cách xử lý data: 
  - Đưa data thành 2 cột giờ/phút/giây và giá cổ phiếu vào file .csv
  - Chuyển giờ/phút/giây từ dạng văn bản về thành mảng 3 số nguyên rồi thành 3 cột giờ (int), phút (int), giây (int)
- Input: giờ, phút, giây cần dự đoán giá cổ phiếu (int, int, int)
- Output: giá cổ phiếu trong giờ, phút, giây cần dự đoán (float)
## Bài toán 3: Dự đoán doanh thu phim:
- Dataset: dữ liệu về các bộ phim khác đã được chiếu: ngân sách sản xuất phim (array(float)), doanh thu của phim (array(float)) 
- Thu thập data (vd: https://www.the-numbers.com/movie/budgets/all)
- Cách xử lý data:
  - Đưa data thành 2 cột ngân sách (float), doanh thu (float) vào file.csv
  - Loại bỏ những điểm dữ liệu bất thường (vd: doanh thu phim bằng 0 vì phim bị dời ngày phát hành,...)
- Input: ngân sách để sản xuất bộ phim cần dự đoán (float)
- Output: doanh thu của bộ phim cần dự đoán (float)
 
