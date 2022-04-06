## Chủ đề
Xây dựng mô hình dự đoán nhiệt độ dựa theo bộ dữ liệu theo tháng của trạm USC. 

## Biểu đồ
[Correlation Score](correlation.csv)  
Lấy ngưỡng là 0.7 ta được các biểu đồ sau.  
Biểu đồ thể hiện mối quan hệ tuyến tính giữa các thuộc tính với nhiệt độ.
![CLDD](img/CLDD.png)
![DT32](img/DT32.png)
![DX70](img/DX70.png)
![EMNT](img/EMNT.png)
![EMXT](img/EMXT.png)
![HTDD](img/HTDD.png)

## Thuật toán
Sử dụng hồi quy tuyến tính để dự đoán nhiệt độ.

## Kết quả
```python
## TRAIN SET
[=] TMIN:
	[*] MAE error: 0.6780580866958524
	[*] RMSE error: 0.9529377996951054
[=] TMAX:
	[*] MAE error: 0.955749488446695
	[*] RMSE error: 1.3370741115152036
[=] TAVG:
	[*] MAE error: 0.23724220251560518
	[*] RMSE error: 0.42522936281120516

## TEST SET
[=] TMIN:
	[*] MAE error: 1.0315703635227735
	[*] RMSE error: 1.4473537530424798
[=] TMAX:
	[*] MAE error: 1.44284969016253
	[*] RMSE error: 1.8482529830560581
[=] TAVG:
	[*] MAE error: 0.48001949615866096
	[*] RMSE error: 0.801823461651462
```