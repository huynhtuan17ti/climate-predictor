# Bài toán khí hậu
Đây là đồ án cuối kì lớp Toán Ứng dụng và Thống kê 20TN trường Đại học Khoa học Tự Nhiên.  
Nhóm gồm các sinh viên:
| Họ và tên     | MSSV      |
| --------      | -----     |
| Huỳnh Minh Tuấn | 20120024 |
| Nguyễn Văn Hưng | 20120009 |
| Trần Ngọc Đô    | 20120057 |

## Cài đặt
```shell
$user git clone https://github.com/huynhtuan17ti/climate-predictor
$user cd climate-predictor
$user pip install -r REQUIREMENTS.txt
```

## Bộ dữ liệu
Sử dụng nguồn dữ liệu từ [Cơ quan Quản lý Khí quyển và Đại dương Quốc gia (NOAA) của Mỹ](https://www.ncdc.noaa.gov/cdo-web/datasets).  
Nhóm sinh viên chọn bộ dữ liệu [khí hậu theo tháng](data/) để phân tích và thực hiện các bài toán.

## Bài toán 1
Xây dựng mô hình dự đoán nhiệt độ dựa theo bộ dữ liệu theo tháng của trạm USC.

### Cấu trúc mã nguồn
Mã nguồn của bài toán 1 nằm ở thư mục `src_1/`

```
|___ src_1/
|    |___ images/         (lưu lại các biểu đồ dùng để biểu diễn)
|    |___ tests/          (unit-test dùng để test code mỗi khi commit)
|    |___ weights/        (thư mục lưu lại trọng số của mô hình tuyến tính)
|    |___ config.yaml     (file yaml cấu hình lưu lại các tham số)
|    |___ correlation.csv (file csv lưu lại độ tương quan giữa các biến)
|    |___ metric.py       (chứa các hàm mất mát dùng để đánh giá độ hiệu quả của mô hình)
|    |___ predictor.py    (source code của mô hình tuyến tính)
|    |___ utils.py        (chứa các phép tính toán và các hàm hỗ trợ)
```

### Sử dụng
```shell
# Thay đổi config file (mặc định là src_1/config.yaml). Ví dụ chạy trên personal.yaml
$user run.py --config personal.yaml 
# Để chọn các biến phù hợp cho mô hình tuyến tính và tính toán độ tương quan giữa các biến
$user run.py --mode 1
# Để huấn luyện mô hình tuyến tính và đánh giá trên tập thử nghiệm
$user run.py --mode 0
```

## Bài toán 2
Mô tả dữ liệu về TAVG (nhiệt độ trung bình) trong vòng 10 năm từ 2010 đến 2020 của các trạm USC.