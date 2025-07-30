1.	Thuật ngữ và viết tắt
STT	Từ viết tắt	Nghĩa đầy đủ
1	XML	eXtensible Markup Language - Ngôn ngữ Đánh dấu Mở rộng
2	VAN	Taxation Value Added Network
3	ICC	Invoice Certification Center
4	PSD	Portable Security Device
5	SGML	Standard Generalized Markup Language
6	W3C	World Wide Web Consortium, viết tắt W3C, lập ra các chuẩn cho Internet, nhất là cho World Wide Web
7	SInvoice	Dịch vụ/hệ thống hóa đơn điện tử của Viettel
8	HTTH	Hệ thống phần mềm kế toán, quản trị doanh nghiệp tích hợp với hệ thống SInvoice để phát hành hóa đơn.
2.	Mục đích và phạm vi
Mô tả chi tiết chuẩn kết nối để các hệ thống có thể kết nối vào dịch vụ Hóa đơn điện tử đại trà của Viettel nhằm đảm bảo phát hành đúng thông tin.
3.	Mô hình kết nối  
 
Hệ thống SInvoice đóng vai trò nhận dữ liệu hóa đơn từ các hệ thống bên ngoài (hệ thống tích hợp) gửi về và phát hành thành hóa đơn theo mẫu mà doanh nghiệp đã chọn. Các API của hệ thống SInvoice được cung cấp theo chuẩn Restful Webservice.
Ban đầu, doanh nghiệp thực hiện các thao tác khai báo mẫu hóa đơn trên web của hệ thống SInvoice bao gồm:
-	Khai báo tên mẫu hóa đơn
-	Chọn mẫu hóa đơn
-	Khai báo dải hóa đơn
-	Lập thông báo phát hành
-	Đăng ký thông tin chứng thư số
Chi tiết các bước hướng dẫn có thể xem thêm tại: https://sinvoice.viettel.vn/ho-tro/huong-dan-su-dung/mo-ta-tong-the-cac-buoc-dang-ky-va-su-dung-dich-vu-hoa-don-dien-tu 
4.	Một số luồng cơ bản
Sau khi các thông tin khai báo mẫu hóa đơn đã được thực hiện đầy đủ trên SInvoice, doanh nghiệp có thể thông qua các hệ thống bên ngoài để gọi các API thực hiện việc
•	Luồng đơn giản
-	Phát hành/Thay thế/điều chỉnh hóa đơn (Tương ứng API mục: 7.2 đối với loại chứng thư số HSM hoặc 7.15 và 7.16 đối với loại chứng thư số USB-TOKEN hoặc 7.31 và 7.32 đối với loại chứng thư số CLOUD CA )
-	Hủy hóa đơn (Tương ứng API mục: 7.10)
-	Tải file hóa đơn (Tương ứng API mục: 7.3)
-	Tra cứu hóa đơn (Tương ứng API mục: 7.6)
-	Lập hóa đơn nháp (Tương ứng API mục: 7.8)
-	Tra cứu hóa đơn bằng transactionUuid (Tương ứng API mục: 7.21): bắt buộc
•	Luồng hóa đơn có phát sinh các trường thông tin thêm (Các thông tin ngoài các khai báo chuẩn trong phần 5. VD: Điện nước, bệnh viện, hải hảng, xuất nhập kho ….)
-	Lấy danh sách trường động được khai báo theo mẫu hóa đơn (Tương ứng API mục: 7.7)
-	Phát hành/Thay thế/điều chỉnh hóa đơn (Tương ứng API mục: 7.2 đối với loại chứng thư số HSM hoặc 7.15 và 7.16 đối với loại chứng thư số USB-TOKEN hoặc 7.31 và 7.32 đối với loại chứng thư số CLOUD CA )
-	Hủy hóa đơn (Tương ứng API mục: 7.10)
-	Tải file hóa đơn (Tương ứng API mục: 7.3)
-	Tra cứu hóa đơn (Tương ứng API mục: 7.6)
-	Lập hóa đơn nháp (Tương ứng API mục: 7.8)
-	Tra cứu hóa đơn bằng transactionUuid (Tương ứng API mục: 7.21): bắt buộc



Lưu ý: 
- Lập hóa đơn sử dụng chữ ký số HSM, USB token và CloudCA sử dụng các hàm khác nhau. HSM sử dụng 1 hàm duy nhất, việc tương tác với chữ ký do hệ thống Hóa đơn điện tử đảm nhiệm. USB, CloudCA sử dụng 2 hàm khác nhau, việc tương tác với chữ ký do phần mềm tích hợp đảm nhiệm. Khách hàng cần được tư vấn trước khi sử dụng.
- Một doanh nghiệp có thể có nhiều mã số thuế (doanh nghiệp, chi nhánh), mẫu hóa đơn, ký hiệu hóa đơn. Vì vậy các hệ thống tích hợp phải cho phép DN cấu hình nhiều thông tin để gửi sang hệ thống SInvoice.
5.	Các tiêu chuẩn
5.1	Tiêu chuẩn thời gian
Toàn bộ trường dữ liệu chỉ định sử dụng tiêu chuẩn 5.1 này, kiểu datetime (đầy đủ giờ, phút, giây. Hiện tại hệ thống chỉ ghi nhận đến giá trị giây, không ghi nhận giá trị mili giây) đầu vào và đầu ra của 33 API theo tiêu chuẩn này chuyển hết về dạng longTime.
Ví dụ: 1587797116000.  Cách tính toán DATE như hình ảnh:
 
Tham khảo trang web: https://currentmillis.com/
5.2	Tiêu chuẩn dữ liệu
-	Hệ thống SInvoice hỗ trợ dữ liệu chuẩn Unicode (UTF-8)
-	Đối với các dữ liệu gửi sang, hệ thống SInvoice sẽ để nguyên format dữ liệu để hiển thị. Ngoại trừ với dữ liệu số (liên quan đến tiền, số lượng, đơn giá, thuế suất), tên ngân hàng, tài khoản ngân hàng. Dữ liệu số gửi sang luôn có định dạng là [0-9.]+. Ví dụ như 100000.1234. Template của SInvoice sẽ tự động format hiển thị. Đối với dữ liệu như tên ngân hàng, tài khoản có thể nhập nhiều, cách nhau bởi dấu “;”.
5.3	Các ký tự đặc biệt  
Các ký tự đặc biệt cần lưu ý và cách xử lý theo đúng chuẩn json (cần ký tự đánh dấu để nhận dạng ký tự đặc biệt)
Trong json cần thêm ký tự đánh dấu \ trước các ký tự đặc biệt.
VD:
-	Json: Muốn truyền dữ liệu là: Nguyễn Văn A "B"
Thì cần truyền trong json như sau: "buyerName": "Nguyễn Văn A \"B\""
5.4	Cơ chế kiểm trùng giao dịch
-	Phần mềm tích hợp và SInvoice giao tiếp qua môi trường mạng, vì vậy rất có thể trong quá trình giao dịch phát sinh ra lỗi về đường truyền (lỗi mạng, hệ thống cao tải v.v.v). Để tránh một giao dịch được tạo thành 2 hóa đơn, với mỗi request hóa đơn gửi sang trong các thao tác lập hóa đơn, hệ thống tích hợp tự sinh ra transactionUuid là duy nhất cho hóa đơn đó và gửi kèm trong request lập hóa đơn. Chi tiết xem mục 5.2 về định dạng dữ liệu transactionUuid.
-	Sau khi request được thực hiện, cần đợi request phản hồi xem kết quả đúng hay sai, hoặc request không phản hồi sau khoảng thời gian timeout (tối thiểu 90 giây). Sau đó mới được gửi request khác với trùng transactionUuid. Việc gửi 2 request đồng thời cùng một thời điểm với trùng transactionUuid sẽ không được hệ thống xử lý kiểm soát mà tạo thành 2 hóa đơn khác nhau.
-	Trong trường hợp chưa nhận được thông tin phản hồi. Có thể chủ động tra cứu lại thông tin hóa đơn dựa theo transactionUuid để biết hóa đơn đã được sinh ra hay chưa. Chi tiết xem mục 7.21 Tra cứu hóa đơn bằng transactionUuid
5.5	Tiêu chuẩn bảo mật kết nối
Có 2 cách để xác thực :
Cách 1:
-	API kết nối được mã hóa sử dụng giao thức https với xác thực bằng Basic Auth.
-	Để đảm bảo bảo mật, mặc định hệ thống sẽ không cho phép các tài khoản kết nối qua API. Để kết nối được API cho các tài khoản, người dùng sẽ phải đăng nhập vào web Viettel và cấu hình IP được phép truy cập. 




VD:
 
Cách 2:
-	API kết nối được mã hóa sử dụng giao thức https với xác thực bằng Token.
-	Lấy thông tin Token
o	Gọi API
API: /auth/login
Method: POST
Content-Type: application/json
Body: {"username":"0100109106-712","password":"12345678aA@"} 

o	Lấy giá trị access_token sinh ra từ API trên để sử dụng trong các lần gọi API tương đương với việc xác thực:
	Truyền vào Header của các API thông tin access_token 
•	Key: Cookie
•	Value: access_token=abc…def
Ví dụ cách sử dụng token với Postman
-	Authorization:
 
-	Headers:
 
-	Body:
 
Kết quả:
 






Sau đó sử dụng access_token tại Headers
 
5.6	Tài khoản test 
Các đơn vị sử dụng tài khoản sau để test kết nối với phần mềm
{
"username":"0100109106-509",
"password":
}
Password liên hệ đầu mối hướng dẫn tích hợp

6.	Đặc tả chi tiết đầu vào lập hóa đơn
6.1	Tổng quan
Đối với các API lập hóa đơn, điều chỉnh hóa đơn, thay thế hóa đơn, lập hóa đơn nháp, xem trước hóa đơn nháp, lập hóa đơn theo lô các trường dữ liệu truyền vào sẽ có dạng chung:
{
   "generalInvoiceInfo":{ //Thông tin chung của hóa đơn
   },
   "buyerInfo":{      //thông tin người mua
   },
   "sellerInfo":{      //thông tin người bán
   },
   "payments":[	//thông tin thanh toán      
   ],
   "itemInfo":[      //thông tin hàng hóa
   ],   
   "metadata":[	//thông tin trường động
   ],
   "meterReading": 	//thông tin đặc biệt dành cho hóa đơn điện nước
   ],
   "summarizeInfo":{	//thông tin tổng hợp tiền của hóa đơn
   },
   "taxBreakdowns":[	//thông tin gom nhóm tiền hóa đơn theo thuế suất
   ]
}
Mô tả:
Tên trường	Mô tả
generalInvoiceInfo	Đây là thông tin chung để phát hành hóa đơn, bao gồm ký hiệu mẫu số hóa đơn, ký hiệu hóa đơn, loại hóa đơn, ngày lập .v.v.v
sellerInfo	Thông tin về bên bán trên hóa đơn. Trong trường hợp bên tích hợp gửi MST sang thì hệ thống sẽ lấy toàn bộ dữ liệu do bên tích hợp gửi sang, nếu không gửi sang thì hệ thống lấy thông tin được cấu hình trên hệ thống.
buyerInfo	Thông tin về bên mua trên hóa đơn
extAttribute	Trường dữ liệu mở rộng, để tùy biến thêm trên mẫu hóa đơn. 
payments	Tên phương thức thanh toán của hóa đơn. 
itemInfo	Thông tin chi tiết hàng hóa của hóa đơn.
taxBreakdowns	Tổng hợp thông tin thuế suất của hóa đơn theo mức thuế suất, ví dụ -2, -1, 0, 5, 8, 10
summarizeInfo	Tổng hợp tiền hàng của cả hóa đơn
metadata	Thông tin trường động của hóa đơn
meterReading	Thông tin đặc biệt, dùng cho hóa đơn điện/nước.
6.2	generalInvoiceInfo
Chứa thông tin cơ bản của hóa đơn, 
Tên trường	Kiểu dữ liệu	Mô tả
invoiceType	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: 	Mã loại hóa đơn chỉ nhận các giá trị sau: 
Thông tư 32: 01GTKT, 02GTTT, 07KPTQ, 03XKNB, 04HGDL, 01BLP. Tuân thủ theo quy định ký hiệu loại hóa đơn của Thông tư hướng dẫn thi hành nghị định số 51/2010/NĐ-CP. Chi tiết xem PL1 Thông tư 39/2014/TT-BTC. 
Thông tư 78: 1, 2, 3, 4, 5, 6. Tuân thủ theo đúng Thông tư 78/2021/TT-BTC
Lưu ý: tại một thời điểm, doanh nghiệp có thể sử dụng nhiều loại hóa đơn.
templateCode	Required: true
DataType: String
Minlength: N/A
Maxlength: 20
Format: 	Ký hiệu mẫu hóa đơn, tuân thủ theo quy định ký hiệu mẫu hóa đơn của Thông tư hướng dẫn thi hành
Thông tư 32: Nghị định số 51/2010/NĐ-CP
Ví dụ 01GTKT0/001, trong đó 
01GTKT: ký hiệu loại hóa đơn
0: số liên, đối với hóa đơn điện tử luôn là 0
001: số thứ tự tăng dần theo số lượng mẫu DN đăng ký với cơ quan thuế
Chi tiết xem PL1 Thông tư 39/2014/TT-BTC
Thông tư 78: Ví dụ: 1/001 trong đó
1: Ký hiệu loại hóa đơn
001: Thứ tự tăng dần theo số lượng mẫu DN đăng ký với cơ quan thuế
Chi tiết tại khoản 1, Điều 3 Thông tư 78/2019/TT-BTC
Lưu ý: tại một thời điểm, doanh nghiệp có thể có nhiều mẫu hóa đơn.

invoiceSeries	Required : true
DataType: String
Minlength : NA
Maxlength : 25
Format : ^[a-zA-Z0-9/]*$	Là “Ký hiệu hóa đơn” tuân thủ theo quy tắc tạo ký hiệu hóa đơn của Thông tư hướng dẫn thi hành
Thông tư 32: Nghị định số 51/2010/NĐ-CP. 
Ví dụ AA/20E.
Chi tiết xem PL1 Thông tư 39/2014/TT-BTC
Thông tư 78: Ví dụ: K20TYY
Chi tiết tại khoản 1, Điều 3 Thông tư 78/2019/TT-BTC
Lưu ý: Tại một thời điểm, doanh nghiệp có thể có nhiều ký hiệu hóa đơn.
Đối với hóa đơn theo TT78, người dùng không bắt buộc phải truyền đúng hai chữ số trong ký hiệu theo đúng năm phát hành hóa đơn. Trường hợp người dùng truyền sai (năm quá khứ hoặc tương lai), hệ thống vẫn lưu ký hiệu theo năm 
Ví dụ: Người dùng lập hóa đơn với ký hiệu K18TAA, có ngày phát hành trong năm 2023, nếu truyền giá trị K50TAA, hệ thống vẫn sẽ lưu ký hiệu hóa đơn sau khi lập là K23TAA.
invoiceIssuedDate	Required: false
DataType: Datetime
Minlength: N/A
Maxlength: 50
Format: Mục 4.1  	Ngày lập hóa đơn, tuân theo nguyên tắc đảm bảo về trình tự thời gian trong 1 ký hiệu hóa đơn của một mẫu hóa đơn với một mã số thuế cụ thể: số hóa đơn sau phải được lập với thời gian lớn hơn hoặc bằng số hóa đơn trước.
Lưu ý:
-	 Thời gian chính xác đến giờ phút giây
-	Trong trường hợp không gửi ngày lập sang, hệ thống tự động lấy theo thời gian hiện tại trên hệ thống với múi giờ GMT+7.
- Dữ liệu truyền vào là thời gian dạng milliseconds kiểu long trong mục 5.1
Hệ thống ghi nhận đến chỉ số giây. Có thể tham khảo công thức tính tại: https://currentmillis.com/

DetailedListNo	Required: false
DataType: String
Minlength: 
Maxlength: 50
	Số bảng kê (Số của bảng kê các loại hàng hóa, dịch vụ đã bán kèm theo hóa đơn hoặc hóa đơn chiết khấu thương mại)

Sin thẻ SBKe
DetailedListDate	Required: false
DataType: date
Minlength: 
Maxlength: 50
	Ngày bảng kê (Ngày của bảng kê các loại hàng hóa, dịch vụ đã bán kèm theo hóa đơn hoặc hóa đơn chiết khấu thương mại) NBKe
currencyCode	Required: true
DataType: String
Minlength: 3
Maxlength: 3
Format: [A-Z]+	Mã tiền tệ dùng cho hóa đơn có chiều dài 3 ký tự theo quy định của ngân hàng nhà nước Việt Nam. Ví dụ: USD, VND, EUR…

adjustmentType 	Required: false
DataType: String
Minlength: 
Maxlength: 1
Format:	Trạng thái điều chỉnh hóa đơn: 
1: Hóa đơn gốc (hóa đơn đã phát hành, hóa đơn bị điều chỉnh, hóa đơn bị thay thế)
3: Hóa đơn thay thế 
5: Hóa đơn điều chỉnh 
7: Hóa đơn xóa bỏ
Không truyền sẽ mặc định là 1
adjustedNote	Required: false
DataType: String
Minlength: N/A
Maxlength: 255
Format:	Lý do sai sót 
Cho phép nhập chuỗi ký tự tối đa 255 ký tự. 
Không bắt buộc truyền.
Đặt trong generalInvoiceInfo
adjustmentInvoiceType	Required: false
DataType: String
Minlength: 
Maxlength: 1
Format:	Loại điều chỉnh đối với hóa đơn điều chỉnh
1: Hóa đơn điều chỉnh tiền 
2: Hóa đơn điều chỉnh thông tin 
Bắt buộc nhập nếu adjustmentType = 5
originalInvoiceId	Required: false
DataType: String
Minlength: 7
Maxlength: 15
Format: ^[a-zA-Z0-9]*$	Số hóa đơn của hóa đơn gốc trong trường hợp lập hóa đơn là: 
    Hóa đơn thay thế
    Hóa đơn điều chỉnh
Số hóa đơn có dạng AA20E00000001, trong đó
    AA20E: ký hiệu hóa đơn
    00000001: số thứ tự tăng dần
Chi tiết xem PL1 Thông tư 39/2014/TT-BTC
originalInvoiceIssueDate	Required: false
DataType: Date
Minlength: N/A
Maxlength: 50
Format: unix timestamp  	Thời gian lập hóa đơn gốc, bắt buộc trong trường hợp lập hóa đơn thay thế và hóa đơn điều chỉnh. Dùng để tìm kiếm hóa đơn gốc của hóa đơn thay thế, điều chỉnh

additionalReferenceDesc 	Required : false
DataType: String
Minlength : 
Maxlength : 225
Format :	Thông tin tham khảo nếu có kèm theo của hóa đơn: văn bản thỏa thuận giữa bên mua và bên bán về việc thay thế, điều chỉnh hóa đơn. Bắt buộc khi lập hóa đơn thay thế, hóa đơn điều chỉnh.

additionalReferenceDate	Required: false
DataType: Date
Minlength: N/A
Maxlength: 50
Format: Mục 4.1  	Thời gian phát sinh văn bản thỏa thuận giữa bên mua và bên bán, bắt buộc khi lập hóa đơn thay thế, hóa đơn điều chỉnh.
- Dữ liệu truyền vào là thời gian dạng milisecond kiểu long trong mục 5.1

paymentStatus	Required: true
DataType: Boolean
Minlength: 
Maxlength: 1
Format:	Trạng thái thanh toán của hóa đơn
True: Đã thanh toán
False: Chưa thanh toán

cusGetInvoiceRight	Required: false
DataType: Boolean
Minlength: 
Maxlength: 1
Format:	Cho phép người dùng tra cứu hóa đơn hay không.
Mặc định true.
Nếu để giá trị false thì sẽ không view được hóa đơn lên


exchangeRate	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format:	Tỷ giá ngoại tệ tại thời điểm lập hóa đơn quy đổi ra VND
Lưu ý: 
- Phần nguyên được nhập tối đa 11 chữ số, phần thập phân tối đa là 2 chữ số
- Bắt buộc truyền nếu lập hóa đơn ngoại tệ, nếu không truyền mặc định =1
Lưu ý: Trường hợp truyền giá trị 0 hoặc “0” cho trường validation thì bắt buộc truyền exchangeRate
transactionUuid	Required: true, Không được trùng
DataType: String
Minlength: 10
Maxlength: 36
Format:
	transactionUuid để kiểm trùng giao dịch lập hóa đơn, được sinh ra từ hệ thống của bên đối tác, là duy nhất với mỗi hóa đơn. Trong trường hợp gửi transactionUuid thì bên hệ thống đối tác sẽ tự quản lý để đảm bảo tính duy nhất của transactionUuid. Với mỗi transactionUuid, khi đã gửi một transactionUuid với một hóa đơn A thì mọi request lập hóa đơn với cùng transactionUuid sẽ trả về hóa đơn A chứ không lập hóa đơn khác. 
Khuyến cáo: sử dụng UUID V4 để tránh bị trùng số. 
Tham khảo: https://en.wikipedia.org/wiki/Universally_unique_identifier

certificateSerial	Required: false
DataType: String
Minlength: 
Maxlength: 100
Format:	Được sử dụng khi lập hóa đơn sử dụng USB Token.
Serial Number của chứng thư số của doanh nghiệp, chứng thư số này đã được doanh nghiệp đẩy lên trên hệ thống khi đăng ký sử dụng USB Token.
Định dạng Hex.
Ví dụ: 5404FFFEB7033FB316D672201B7BA4FE
originalInvoiceType	Required: false
DataType: String
Minlength: N/A
Maxlength: 
Format:	Loại hóa đơn gốc
Truyền giá trị số với ý nghĩa như sau 
0- Không phải hóa đơn giấy/hóa đơn không tồn tại trên hệ thống 
1-Hóa đơn TT78 
2-Hóa đơn theo QĐ 1209 
3-Hóa đơn điện tử/giấy TT32
4-Hóa đơn giấy TT 78
Không truyền thì mặc định sẽ là 0
originalTemplateCode	Required: 
DataType: String
Minlength: N/A
Maxlength: 20
Format:	Bắt buộc truyền nếu originalInvoiceType là 1, 2, 3 hoặc 4
Ví dụ mẫu TT32: 01GTKT0/001
Ví dụ mẫu TT78: 1/0224 sẽ truyền là 1
2/001 sẽ truyền là 2.... tương tự các loại hóa đơn khác ( đối với tt78 sẽ truyền theo invoiceType )
reservationCode	Required: true
DataType: String
Minlength: 
Maxlength: 100
Format:	- Mã bí mật đã được cấp cho MST 
- Yêu cầu này thực hiện thêm mới API phát hành hóa đơn có mã bí mật sử dụng chữ ký server
- Thông tin đầu ra tương tự như API createInvoice/{supplierTaxCode}, trong đó reservationCode trong response chính là reservationCode trong Input. 
- Trong trường hợp hệ thống gặp lỗi/chậm không thế trả kết quả ngay thì trả kết quả sau 10s.

adjustAmount20	Required: false
DataType: Number	Trường giảm giá 20% đối với hóa đơn bán hàng: Trường nhận giá trị “Tỷ lệ % theo doanh thu”.
Giá trị truyền vào thuộc một trong các giá trị “0, 1, 2, 3, 5”.
Ví dụ: “adjustAmount20”: “2”
Lưu ý: 
Giá trị “0” đối với trường hợp giảm trên từng hàng hóa.
Khi truyền giá trị “0” thì phải truyền tham số adjustRatio hợp lệ cho ít nhất một hàng hóa có tính chất khác ghi chú.
invoiceNote	Required: false
DataType: String
Minlength: N/A
Maxlength: 500
Format:	Được sử dụng như là 1 dòng ghi chú ở dưới danh sách hàng hóa, khi thay thế điều chỉnh hệ thống sẽ tự sinh ra dòng “ Điều chỉnh / thay thế cho hóa đơn ... ngày .... “ . Khi điều chỉnh trên web sẽ tự sinh còn api thì phải truyền vào 
Lưu ý: Không tự sinh nếu bỏ kiểm tra dữ liệu đầu vào
validation	Required: false
DataType: Number
Minlength: N/A
Maxlength: 
Format:	Được sử dụng để điều hướng bỏ qua việc kiểm tra ràng buộc và tính toán lại các trường thông tin tiền của hàng hóa và hóa đơn:
-	Trường hợp truyền giá trị 0 hoặc “0” thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
-	Các trường hợp khác thì xử lý theo nguyên tắc hiện tại.
Lưu ý: Trường hợp truyền giá trị 0 hoặc “0” cho trường validation:
-	Bắt buộc phải truyền giá trị khác null cho trường totalAmountAfterDiscount trong phần summarizeInfo nếu không trong XML hóa đơn sẽ không có thẻ TgTCThue
-	Bắt buộc phải truyền giá trị khác null cho trường itemTotalAmountAfterDiscount trong phần itemInfo nếu không trong XML hóa đơn thông tin hàng hóa tương ứng sẽ không có thẻ TTien 
-	Bắt buộc truyền exchangeRate nếu không xml sẽ bị null exchangeRate
qrCode	Required: false
DataType: String
Minlength: N/A
Maxlength: 500
Format:	Nếu truyền qrCode thì khi lập hóa đơn thành công sẽ lưu giá trị vào cột QR_CODE trong bảng invoice.
Thực hiện view hóa đơn, quét QR bằng các phần mềm quét QR  thì sẽ gen đúng chuỗi khai báo giá trị cho qrCode
otherTax	Required: false
DataType: String
Minlength: N/A
Maxlength: 
Format:	Nếu truyền otherTax = 1 là truyền thuế suất khác theo TT103/2014 thì
+ Tại bước sinh file xml, lưu thẻ <TSuat> là KHAC đối với % thuế truyền vào khác các giá trị sau: {-2, -1, 0, 5, 8, 10}
Nếu truyền otherTax khác 1 thì:
+ Tại bước sinh file xml, lưu thẻ <TSuat> là KHAC:AB.CD% đối với % thuế truyền vào khác các giá trị sau: {-2, -1, 0, 5, 8, 10}

Dữ liệu mẫu
Hóa đơn thường
    "generalInvoiceInfo": {
    "transactionUuid": "859f390a-1e59-4a05-9663-1e9ec7afdb8f",
    "invoiceType": "1",
    "templateCode": "1/001",
    "invoiceSeries": "C24AAA",
    "invoiceIssuedDate": 1605027600000,
"currencyCode": "VND",
“exchangeRate”: 1,
"adjustmentType": "1",
    "paymentStatus": true,
    "cusGetInvoiceRight": true
}
Hóa đơn điều chỉnh tiền
"generalInvoiceInfo": {
    "transactionUuid": "859f390a-1e59-4a05-9663-1e9ec7afdb8f",
    "invoiceType": "1",
    "templateCode": "1/001",
    "invoiceSeries": "C24AAA",
    "invoiceIssuedDate": 1605027600000,
"currencyCode": "VND",
    "adjustmentType": "5",
"adjustmentInvoiceType": "1",
“exchangeRate”: 1,
“adjustedNote”: “Lý do điều chỉnh để báo cáo nhận được”
    "originalInvoiceId": C24AA1",
    "originalInvoiceIssueDate": 1605027600000,
    "additionalReferenceDesc": "Văn bản",
    "additionalReferenceDate": 1605027600000,
    "paymentStatus": true,
    "cusGetInvoiceRight": true
  }

Hóa đơn điều chỉnh thông tin
"generalInvoiceInfo": {
    "transactionUuid": "859f390a-1e59-4a05-9663-1e9ec7afdb8f",
    "invoiceType": "1",
    "templateCode": "1/001",
    "invoiceSeries": "C24AAA",
    "invoiceIssuedDate": 1605027600000,
"currencyCode": "VND",
    "adjustmentType": "5",
"adjustmentInvoiceType": "2",
“exchangeRate”: 1,
“adjustedNote”: “Lý do điều chỉnh để báo cáo nhận được”
“invoiceNote”: “Nội dung ghi chú muốn hiển thị lên hóa đơn”
    "originalInvoiceId": "C24AA1",
    "originalInvoiceIssueDate": 1605027600000,
    "additionalReferenceDesc": "Văn bản",
    "additionalReferenceDate": 1605027600000,
    "paymentStatus": true,
    "cusGetInvoiceRight": true
  }
Hóa đơn thay thế
"generalInvoiceInfo": {
    "transactionUuid": "859f390a-1e59-4a05-9663-1e9ec7afdb8f",
    "invoiceType": "1",
    "templateCode": "1/001",
    "invoiceSeries": "C24AA",
    "invoiceIssuedDate": 1605027600000,
"currencyCode": "VND",
    "adjustmentType": "3",
“exchangeRate”: 1,
“adjustedNote”: “Lý do điều chỉnh để báo cáo nhận được”
“invoiceNote”: “Nội dung ghi chú muốn hiển thị lên hóa đơn” 
"originalInvoiceId": "C24AA1",
    "originalInvoiceIssueDate": 1605027600000,
    "additionalReferenceDesc": "Văn bản",
    "additionalReferenceDate": 1605027600000,
    "paymentStatus": true,
    "cusGetInvoiceRight": true
  }
Hóa đơn thay thế cho hóa đơn không tồn tại trên hệ thống
"generalInvoiceInfo": {
        "invoiceType": "1",
        "templateCode": "1/001",
        "invoiceSeries": "C24AA",
        "invoiceIssuedDate": 1605027600000,
        "currencyCode": "VND",
        "invoiceNote": "",
        "adjustmentType": "3",
    “exchangeRate”: 1,
    “adjustedNote”: “Lý do điều chỉnh để báo cáo nhận được”
        “invoiceNote”: “Thay thế hóa đơn số 1, mẫu số 1, ký hiệu C24AAA, ngày 28/03/2022”
        "paymentStatus": true,
        "cusGetInvoiceRight": true,
        "originalInvoiceId": "C24AA1",
        "originalInvoiceIssueDate": 1654861128000,
         "originalInvoiceType": "1",
         "originalTemplateCode": "1",
        "additionalReferenceDesc": "Hóa đơn thay thế số: 1, mẫu số: 1, ký hiệu: C24AA1, ngày: 10/06/2022",
        "additionalReferenceDate": 1658825818067,
        "transactionUuid": "E4B2813E5AA4E335E053380A10ACB857"
  }
Hóa đơn điều chỉnh tiền cho hóa đơn không tồn tại trên hệ thống
{
"generalInvoiceInfo": {
"invoiceType": "1",
"templateCode": "1/001",
"invoiceSeries": "C24AAA",
"currencyCode": "VND",
"adjustmentType": "5",
"adjustmentInvoiceType": "1",
"originalInvoiceId": "C24AA1",
“exchangeRate”: 1,
“adjustedNote”: “Lý do điều chỉnh để báo cáo nhận được”
“invoiceNote”: “Điều chỉnh hóa đơn số 1, mẫu số 1, ký hiệu C24AAA, ngày 28/03/2022 Điều chỉnh giảm thuế GTGT 10% thành 8%”
"originalInvoiceIssueDate": 1648454669000,
"additionalReferenceDate": 1648454669000,
"additionalReferenceDesc": "lý do điều chỉnh",
"originalInvoiceType": "1",
"originalTemplateCode": "1",
"paymentStatus": true,
"cusGetInvoiceRight": true
}

6.3	sellerInfo
Thông tin người bán trên hóa đơn, có thể được truyền sang hoặc lấy tự động trên hệ thống hóa đơn điện tử. Trong trường hợp sellerTaxCode KHÔNG ĐƯỢC truyền sang thì dữ liệu sẽ được lấy từ hệ thống hóa đơn điện tử.
Chú ý 1: Các trường dữ liệu có required = true khi có truyền sellerTaxCode, nếu không truyền sellerTaxCode thì các trường khác được lấy từ hệ thống HDDT, không lấy từ thông tin truyền vào, với trường storeCode và storeName nếu truyền vào thì vinvocie sẽ lấy theo dữ liệu truyền vào
Chú ý 2: sellerTaxCode phải trùng khớp với taxCode của user đăng nhập
Tên trường	Kiểu dữ liệu	Mô tả
sellerLegalName	Required: true
DataType: String
Minlength: 
Maxlength: 400
Format: N/A	Tên (đăng ký kinh doanh trong trường hợp là doanh nghiệp) của người bán

sellerTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format:	Mã số thuế người bán được cấp bởi TCT Việt Nam. Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
Mã số này được dùng để kiểm tra xem dữ liệu sẽ lấy từ hệ thống SInvoice hay do phần mềm tích hợp truyền sang. Nếu có dữ liệu thì sẽ lấy toàn bộ thông tin người bán từ phần mềm tích hợp. Nếu không có sẽ lấy thông tin được cấu hình trên SInvoice. Mã số này không được dùng để phát hành lên hóa đơn. 
sellerAddressLine	Required: true
DataType: String
Minlength: 
Maxlength: 255
Format: N/A	Địa chỉ của bên bán được thể hiện trên hóa đơn.

sellerPhoneNumber	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format: \s*[0-9]*\s*	Số điện thoại người bán

sellerFaxNumber	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format: \s*[0-9]*\s*	Số fax người bán

sellerEmail	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format: \s{0,}(([a-zA-Z0-9][a-zA-Z0-9_*$&+,:;=?#|'<>.^*()%!-]{2,}@[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,}){1,})+)\s{0,}	Địa chỉ thư điện tử người bán

sellerBankName	Required: false
DataType: String
Minlength: 
Maxlength: 400
Format:	Tên ngân hàng nơi người bán mở tài khoản giao dịch

sellerBankAccount	Required: false
DataType: String
Minlength: 
Maxlength: 30
Format: \s*[0-9]*\s*	Tài khoản ngân hàng của người bán

sellerDistrictName	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Tên Quận Huyện

sellerCityName	Required: false
DataType: String
Minlength: 
Maxlength: 600
Format:	Tên Tỉnh/Thành phố

sellerCountryCode	Required: false
DataType: String
Minlength: 
Maxlength: 15
Format:	Mã quốc gia 

sellerWebsite	Required: false
DataType: String
Minlength: 
Maxlength: 200
Format:	Website của người bán

storeCode	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Mã cửa hàng
storeName	Required: false
DataType: String
Minlength: 
Maxlength: 400
Format:	Tên cửa hàng
merchantCode	Required: true
DataType: String
Minlength: 
Maxlength: 4
Format:	Mã danh mục đơn vị chấp nhận thanh toán
Chỉ cho phép truyền ký tự số
Lưu ý: các trường này phục vụ cho việc sinh qrcode78, các mẫu khác không bắt buộc
merchantName	Required: true
DataType: String
Minlength: 
Maxlength: 25
Format:	Tên đơn vị chấp nhận thanh toán
Chỉ cho phép truyền 96 ký tự theo EMV Book 
Lưu ý: các trường này phục vụ cho việc sinh qrcode78, các mẫu khác không bắt buộc

merchantCity	Required: true
DataType: String
Minlength: 
Maxlength: 15
Format:	Thành phố đơn vị chấp nhận thanh toán 
Chỉ cho phép truyền 96 ký tự theo EMV Book 
Lưu ý: các trường này phục vụ cho việc sinh qrcode78, các mẫu khác không bắt buộc
Dữ liệu mẫu
"sellerInfo": {
    "sellerLegalName": "Người bán hàng",
    "sellerTaxCode": "0100109106",
    "sellerAddressLine": "Thành Phố Hà Nội - Việt Nam",
    "sellerPhoneNumber": "0123456789",
	"sellerFaxNumber": "0123456789",
    "sellerEmail": "email@gmail.com",
    "sellerBankName": "Ngân hàng ",
    "sellerBankAccount": "012345678901",
	"sellerDistrictName": "",
    "sellerCityName": "Thành Phố Hà Nội",
    "sellerCountryCode": "84”,
    "sellerWebsite": "sinvoice.viettel.vn"
  }
6.4	buyerInfo
Thông tin người mua trên hóa đơn.
Tên trường	Kiểu dữ liệu	Mô tả
buyerName	Required: false
DataType: String
Minlength: 
Maxlength: 800
Format:	Tên người mua trong trường hợp là người mua lẻ, cá nhân. Tên người mua hoặc tên đơn vị là bắt buộc khi buyerNotGetInvoice = 0.


buyerCode	Required: false
DataType: String
Minlength: 
Maxlength: 400
Format:	Mã khách hàng, chỉ cho phép các ký tự 


buyerLegalName	Required: false
DataType: String
Minlength: 
Maxlength: 1200
Format:	Tên đơn vị (đăng ký kinh doanh trong trường hợp là doanh nghiệp) của người mua. Tên người mua hoặc tên đơn vị là bắt buộc khi buyerNotGetInvoice = 0.
Bắt buộc nếu truyền buyerTaxCode

buyerTaxCode	Required: false
DataType: String
Minlength: 
Maxlength: 20
Format: 	Mã số thuế người mua, có thể là mã số thuế Việt Nam hoặc mã số thuế nước ngoài
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

buyerBudgetCode	Required: false
DataType: String
Minlength: 
Maxlength: 7
Format: 	Mã quan hệ ngân sách của tổ chức, đơn vị mua hàng

buyerAddressLine	Required: false
DataType: String
Minlength: 
Maxlength: 1200
Format:	Địa chỉ xuất hóa đơn của người mua 
Bắt buộc khi buyerNotGetInvoice = 0


buyerPhoneNumber	Required: false
DataType: String
Minlength: 
Maxlength: 15
Format: \s*[0-9]*\s*	Số điện thoại người mua, số điện thoại sẽ được dùng để gửi tin nhắn trong trường hợp bên bán đăng ký dịch vụ SMS Brandname. 

buyerFaxNumber	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: 	Số fax người mua
(Hiện tại nếu truyền thì Sinvoice cũng không lấy)

buyerEmail	Required: false
DataType: String
Minlength: 
Maxlength: 2000
Format: ^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$  (áp dụng cho từng email đơn lẻ)	Email người mua, sử dụng để gửi hóa đơn cho người mua
Nếu có nhiều email thì cách nhau bởi dấu chấm phẩy (;). Khi tài khoản email của bên bán được cấu hình trên hệ thống thì hệ thống tự động gửi nếu có email của người mua. Chi tiết cấu hình email xem ở đây: https://sinvoice.viettel.vn/ho-tro/huong-dan-su-dung/5-huong-dan-cau-hinh-doanh-nghiep--cau-hinh-chung 


buyerBankName	Required: false
DataType: String
Minlength: 
Maxlength: 200
Format:	Tên trụ sở chính ngân hàng nơi người mua mở tài khoản giao dịch. 


buyerBankAccount	Required: false
DataType: String
Minlength: 
Maxlength: 30
Format:	Tài khoản ngân hàng của người mua. 


buyerDistrictName	Required: false
DataType: String
Minlength: 
Maxlength: 
Format:	Tên Quận Huyện
(Hiện tại nếu truyền thì Sinvoice cũng không lấy)

buyerCityName	Required: false
DataType: String
Minlength: 
Maxlength: 
Format:	Tên Tỉnh/Thành phố
(Hiện tại nếu truyền thì Sinvoice cũng không lấy)

buyerCountryCode	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: 	Mã quốc gia người mua
(Hiện tại nếu truyền thì Sinvoice cũng không lấy)

buyerIdType	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: [123]*	Loại giấy tờ của người mua,
-	1: CCCD
-	2: Hộ chiếu
buyerIdNo	Required: false
DataType: String
Minlength: 
Maxlength: 200
Format: [a-zA-Z0-9-_ ]*	Chú ý: Khi buyerIdType có giá trị thì buyerIdNo bắt buộc phải có giá trị.
Số giấy tờ của người mua, có thể là chứng minh thư/căn cước công dân, giấy phép kinh doanh, hộ chiếu

buyerBirthDay	Required: false
DataType: Date
Minlength: 
Maxlength: 
Format: 	Ngày sinh của người mua
(Hiện tại nếu truyền thì Sinvoice cũng không lấy)

buyerNotGetInvoice	Required: false
DataType: Integer
Minlength: 0
Maxlength: 1
Format:	Người mua không lấy hóa đơn
0-Người mua có lấy hóa đơn 
1-Người mua không lấy hóa đơn
Nếu không truyền, mặc định là 0
Dữ liệu mẫu
"buyerInfo": {
    "buyerName": "Tên khách hàng",
    "buyerLegalName": "Tên đơn vị",
    "buyerTaxCode": "0100109106",
    "buyerAddressLine": "An Khánh Hoài Đức Hà Nội",
    "buyerDistrictName": "Số 9, đường 11, VSIP Bắc Ninh, Thị xã Từ Sơn, Tỉnh",
    "buyerCityName": "Thành Phố Hà Nội",
    "buyerCountryCode": "84",
    "buyerPhoneNumber": "987999999",
    "buyerFaxNumber": "0458954",
    "buyerEmail": "minhltt@viettel.com.vn",
    "buyerBankName": "Ngân hàng Quân đội MB",
    "buyerBankAccount": "01578987871236547",
    "buyerIdType": "3",
    "buyerIdNo": "8888899999",
    "buyerCode": "832472343b_b",
    "buyerBirthDay": ""
  }
6.5	payments 

Tên trường	Kiểu dữ liệu	Mô tả
paymentMethod	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Hình thức thanh toán. Có thể không cần truyền giá trị, chỉ cần truyền paymentMethodName
- Gồm các giá trị sau:
1: khi hình thức thanh toán là TM
2: khi hình thức thanh toán là CK
3: khi hình thức thanh toán là TM/CK
4: khi hình thức thanh toán là DTCN
5: khi hình thức thanh toán là KHAC
6: Khi hình thức thanh toán là Tiền mặt
7: Khi hình thức thanh toán là Chuyển khoản
8: Khi hình thức thanh toán là Tiền mặt/Chuyển khoản
- Không truyền dữ liệu thì sẽ được hiểu là 5
paymentMethodName	Required: true
DataType: String
Minlength: 
Maxlength: 50
Format:	Hình thức thanh toán chi tiết phải mapping theo paymentMethod.
- Gồm các giá trị sau:
TM
CK
TM/CK
DTCN
KHAC
Tiền mặt
Chuyển khoản
Tiền mặt/Chuyển khoản
- Không truyền dữ liệu thì trả về thông báo lỗi 
- Được nhập free text khi paymentMethod = 5, được hiểu là hình thức thanh toán khác
Dữ liệu mẫu
"payments": [
    {
	  "paymentMethod": "2",
      "paymentMethodName": "CK"
    }
  ]

Hoặc

"payments": [
    {
      "paymentMethodName": "Truyền trực tiếp giá trị mong muốn vào đây"
    }
  ]


6.6	itemInfo
Là một danh sách các hàng hóa/dịch vụ được hiển thị trên hóa đơn. 
Tên trường	Kiểu dữ liệu	Mô tả
lineNumber	Required: false
DataType: Integer
Minlength: 
Maxlength: 
Format: 	Thứ tự dòng hóa đơn, bắt đầu từ 1
Không cần nhập, hệ thống tự động sinh
selection	Required: false
DataType: Integer
Min: 1
Max: 6
Format: 	Đánh dấu loại hàng hóa/dịch vụ
Đối với Thông tư 32:
Null hoặc 1- Hàng Hóa (Sinh STT, bắt buộc phải nhập số lượng, đơn giá)
2: Ghi chú (Không sinh STT và không cộng tiền vào tổng tiền thanh toán)
3: Chiết khấu (Không sinh STT, không cần nhập số lượng, đơn giá và thêm isIncreaseItem = false để xác định giảm tiền)
4: Bảng kê (Sinh STT, không cần nhập số lượng, đơn giá, chỉ cần nhập thành tiền)
5: Phí khác (Không sinh STT, không bắt buộc nhập số lượng, đơn giá)
Đối với Thông tư 78:
Null hoặc 1- Hàng Hóa (Sinh STT, bắt buộc phải nhập số lượng, đơn giá)
2: Ghi chú (Không sinh STT và không cộng tiền vào tổng tiền thanh toán) 
3: Chiết khấu (Không sinh STT, không cần nhập số lượng, đơn giá và thêm isIncreaseItem = false để xác định giảm tiền)
4: Phí khác (Không sinh STT, không nhập số lượng, đơn giá)
      5: Khuyến mại (Sinh STT, bắt buộc phải nhập số           lượng, đơn giá)
6: Hàng hóa đặc trưng, nếu truyền hàng hóa đặc trưng (ND 70) thì các trường thông tin bắt buộc xem danh sách bên dưới 

itemType	Required: false
DataType: Integer
Min: 1
Max: 6
Format:	Trường hợp nếu truyền selection là 6 thì trường này bắt buộc
Loại hàng hóa đặc thù
1.	Hàng hóa là xe ô tô, xe mô tô
2.	Dịch vụ vận chuyển
3.	Dịch vụ vận chuyển trên nền tảng số, TMĐT
itemCode	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format: 	Mã hàng hóa, dịch vụ
itemName	Required: false
DataType: String
Minlength: 
Maxlength: 500
Format:	Tên hàng hóa, dịch vụ
Bắt buộc nhập với tính chất hàng hóa là Hàng hóa, Khuyến mãi và Phí khác
Đối với hóa đơn điều chỉnh, Hệ thống sẽ dựa vào giá trị của isIncreaseItem xác định điều chỉnh tăng, giảm để tự sinh câu mô tả: 
"Điều chỉnh tăng/giảm tiền hàng, tiền thuế của hàng hóa dịch vụ" + itemName
-	Đối vói biên lai thì đây là Tên loại phí 
unitCode	Required: false
DataType: String
Minlength: 
Maxlength: 100
Format:	Mã đơn vị tính

unitName	Required: false
DataType: String
Minlength: 
Maxlength: 300
Format:	Tên đơn vị tính hàng hóa, dịch vụ

unitPrice	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Đơn giá của hàng hóa
Bắt buộc nhập với tính chất hàng hóa là Hàng hóa, Khuyến mãi
Cho phép truyền giá trị âm


quantity	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Số lượng của hàng hóa
Bắt buộc nhập với tính chất hàng hóa là Hàng hóa, Khuyến mãi
Cho phép truyền giá trị âm

itemTotalAmountWithoutTax	Required: true
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format: [0-9.]+	Là tổng tiền chưa bao gồm VAT của hàng hóa/dịch vụ. Tổng tiền không có số âm. itemTotalAmountWithoutTax = quantity * unitPrice
Hệ thống sẽ kiểm tra dữ liệu nhận được vế bên trái với dữ liệu tính toán vế bên phải để kiểm tra tính chính xác của dữ liệu. 
Hóa đơn thường: Là tổng tiền hàng hóa dịch vụ chưa có VAT. 
Hóa đơn điều chỉnh: Là tổng tiền phần điều chỉnh của hàng hóa dịch vụ chưa có VAT
Lưu ý: Cho phép sai số 5 đơn vị
taxPercentage	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Trong trường hợp thuế tổng/hóa đơn bán hàng (theo chuẩn hóa đơn xác thực là phải có)
-	Thuế tổng: để theo con số chung
-	Hóa đơn bán hàng/hóa đơn không thuế: -2 
Thuế suất của hàng hóa, dịch vụ. Thuế suất bao gồm các loại:
-2: không thuế
-1: không kê khai tính/nộp thuế (Chỗ này hơi ngược với hóa đơn có mã xác thực của TCT)
0: 0%
5: 5%
8: 8%
10: 10%
Nếu truyền loại thuế suất khác thì truyền giá trị % thuế suất.
VD: Khác 12.34% thì truyền “taxPercentage”: 12.34
taxAmount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength
Format: [0-9.]+	Tổng tiền thuế
Trong trường hợp thuế tổng/hóa đơn bán hàng: (theo chuẩn hóa đơn xác thực là phải có)
-	Thuế tổng: tổng tiền hàng * thuế chung
-	Hóa đơn bán hàng/hóa đơn không thuế: 0
Nếu không truyền, được hiểu là = 0
isIncreaseItem	Required: false
DataType: Boolean
Minlength: 
Maxlength: 
Format:	Hóa đơn bình thường: có giá trị là null.
Hóa đơn điều chỉnh:
- false: dòng hàng hóa/dịch vụ bị điều chỉnh giảm 
- true: dòng hàng hóa/dịch vụ bị điều chỉnh tăng

itemNote	Required: false
DataType: String
Minlength: 
Maxlength: 300
Format:	Ghi chú cho từng dòng hàng hóa
Để đồng bộ nội dung ghi chú của từng dòng hàng hóa đọc tự động trên web và nội dung ghi chú từ API tích hợp khi lập hóa đơn điều chỉnh tiền, người dùng API tích hợp truyền nội dung ghi chú chi tiết cho từng dòng hàng hóa vào trường itemNote trong itemInfo. Hệ thống sẽ tự đọc phần thông tin “của hàng hóa dịch vụ” và ghép với tên hàng hóa dịch vụ
Ví dụ: Hệ thống tự động sinh ghi chú: Điều chỉnh tăng số lượng, giảm đơn giá của hàng hóa dịch vụ: Máy tính
batchNo	Required: false
DataType: String
Minlength: 
Maxlength: 300
Format:	Số lô, thường dùng cho các hàng hóa là thuốc, có thể sử dụng để hiển thị thêm thông tin trong trường hợp cần thiết.

expDate	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Hạn sử dụng của hàng hóa, thường dùng cho các hàng hóa là thuốc, có thể sử dụng để hiển thị thêm thông tin trong trường hợp cần thiết.

discount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	% chiết khấu trên dòng sản phẩm, tính trên đơn giá của sản phẩm. Trong trường hợp không có thì truyền 0


discount2	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	% chiết khấu thứ 2 trên dòng sản phẩm, tính trên đơn giá của sản phẩm. Trong trường hợp không có thì truyền 0.

itemDiscount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Giá trị chiết khấu trên dòng sản phẩm, sau khi nhân với số lượng và % chiết khấu
Hệ thống tự tính, không cần truyền dữ liệu

itemTotalAmountAfterDiscount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Là tổng tiền sau khi trừ chiết khấu, giảm giá.
Hệ thống tự tính, không cần truyền dữ liệu
Lưu ý: Trường hợp truyền giá trị 0 hoặc “0” cho trường validation: bắt buộc phải truyền giá trị khác null
itemTotalAmountWithTax	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Là tổng tiền đã bao gồm VAT của hàng hóa/dịch vụ. 
Hệ thống tự tính, không cần truyền dữ liệu

adjustRatio	Required: false
DataType: Integer
Minlength: 
Maxlength: 
Format: [0-9.]+	Trường giảm giá 20% đối với hàng hóa áp dụng với hóa đơn bán hàng: Trường nhận giá trị “Tỷ lệ % theo doanh thu”.
Giá trị truyền vào thuộc một trong các giá trị “1, 2, 3, 5”.
Ví dụ: “adjustRatio”: “1”
Lưu ý: Giá trị của trường này chỉ có ảnh hưởng đến giá trị hóa đơn khi trường adjustAmount20 trong phần generalInvoiceInfo có giá trị là “0”, các trường hợp truyền giá trị khác cho adjustAmount20 thì hệ thống sẽ bỏ qua. Khi truyền adjustAmount20 = “0” thì phải truyền giá trị adjustRatio hợp lệ cho ít nhất một hàng hóa có tính chất không phải ghi chú.
unitPriceWithTax	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Đơn giá của hàng hóa bao gồm thuế. 
Được sử dụng trong API lập hóa đơn nháp cho xăng dầu
unitPriceWithTax	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Đơn giá của hàng hóa bao gồm thuế. 
Được sử dụng trong API lập hóa đơn nháp cho xăng dầu
specialInfo
	Required: false
DataType: List objet

"specialInfo": [
 {
    "name": "SKhung",
    "value": "137462734"
                },
 {
    "name": "SMay",
    "value": "13746dd2734"
                }
            ] 
	Nếu truyền itemType thì trường specialInfo
Tùy theo yêu cầu của Nghị định 70 theo từng hàng hóa đặc thù, name và value ,validate theo yêu cầu từ TCT .
Danh sách các trường đặc thù được trình bày bên dưới 




DANH MỤC LOẠI HÀNG HÓA ĐẶC THÙ
STT	Mô tả	Giá trị bắt buộc	Loại hóa đơn áp dụng
1	Hàng hóa là xe ô tô, xe mô tô	SKhung: Số khung, string, bắt buộc, max 200 kí tự
SMay: Số máy, string, bắt buộc , max 200 kí tự
	
Hóa đơn bán hàng, hóa đơn giá trị gia tăng, hóa đơn khác, hóa đơn máy tính tiền, hóa đơn tài sản công, hóa đơn giá trị gia tăng tich hợp biên lại
2	Dịch vụ vận chuyển	BKSPTVChuyen: Biển kiểm soát phương tiện vận chuyển , string,, bắt buộc, 200 kí tự  	Hóa đơn bán hàng, hóa đơn giá trị gia tăng, hóa đơn khác, hóa đơn máy tính tiền, hóa đơn tài sản công, hóa đơn giá trị gia tăng tich hợp biên lại
3	Dịch vụ vận chuyển trên nền tảng số, TMĐT	 TNGHang: Tên người gửi hang, string,, bắt buộc, 200 kí tự  
 DCNGHang: Địa chỉ người gửi hang, string,, bắt buộc, 200 kí tự  
MSTNGHang: MST người gửi, string,, bắt buộc, 200 kí tự  
MDDNGHang; Số định danh người gửi hang, string,, bắt buộc, 200 kí tự  	Hóa đơn bán hàng, hóa đơn giá trị gia tăng, hóa đơn khác, hóa đơn máy tính tiền, hóa đơn giá trị gia tăng tich hợp biên lại




Lưu ý 1: Đối với từng dòng hàng hóa, trong trường hợp các trường thông tin như quantity, unitPrice, itemTotalAmountWithoutTax, taxPercentage, taxAmount, discount, itemDiscount, itemTotalAmountWithTax có dữ liệu (dữ liệu khác null), hệ thống sẽ tính toán và kiểm tra các dữ liệu
Hệ thống so sánh quantity x unitPrice lệch không quá 5 đồng so với itemTotalAmountWithoutTax
Hệ thống so sánh itemTotalAmountWithoutTax khi bị lệch quá hệ thống báo lỗi. 
Dòng ghi chú cho hóa đơn điều chỉnh, thay thế tổng hợp hệ thống sẽ tự động thêm.
VD Điều chỉnh tăng tiền hàng, tiền thuế của hàng hóa dịch vụ: Hàng hóa 01, hệ thống sẽ tự tổng hợp lại và sinh 1 item dạng selection =2 với nội dung tổng hợp như sau, hệ thống phần mềm không cần thêm, tránh trùng lặp: 
Hóa đơn điều chỉnh tăng tiền hàng, tiền thuế cho hóa đơn điện tử mẫu số01GTKT0/002, kí hiệu AA/20E, số hóa đơn AA/20E0000162, ngày lập09:22:25 19/11/2020: số tiền: 165,495 VN
Hóa đơn thay thế cho hóa đơn điện tử mẫu số 01GTKT0/002, kí hiệuAA/20E, số hóa đơn AA/20E0000156, ngày lập 14:01:00 18/11/2020

- Trường hợp trong itemInfo người dùng có truyền thông tin gì thì lưu theo đúng giá trị người dùng truyền.
- Lưu ý 2: cho phép người dùng điều chỉnh thông tin hàng hóa khi lập hóa đơn điều chỉnh thông tin qua API tích hợp: 
+ Trường hợp hàng hóa trong itemInfo chỉ truyền thông tin selection hoặc lineNumber thì không lưu dữ liệu hàng hóa này
+ Trường hợp hàng hóa có ít nhất một thông tin khác (ngoài lineNumber hay selection bao gồm: itemCode, itemName, unitCode, unitName, batchNo, itemNote, expDate) thì lưu hàng hóa theo giá trị người dùng truyền vào list_product trong invoice. Trường thông tin nào không truyền/truyền rỗng thì lưu giá trị null.
+ Các trường thông tin khác lineNumber, selection , itemCode, itemName, unitCode, unitName, batchNo, itemNote, expDate thì truyền hay không truyền giá trị đều lưu là NULL
Dữ liệu mẫu
"itemInfo": [
    { hàng_hóa_1},      { hàng_hóa_1}
  ]
Hàng hóa thông thường
"itemInfo": [
    {
      "lineNumber": 1,
      "itemCode": "PCDELLV3653_i56400_R4H10DVDRW",
      "itemName": "Máy tính để bàn DELL VOSTRO 3653 Desktop Core i5-6400 upto3.30Ghz/ 4GB/ 1TB HDD/DVDRW/NVIDIA Geforce 705 2Gb/ Wireless-Bluetooth/ K/ M/1Yr Pro",
      "unitName": "Cái",
      "itemNote": "",
      "unitPrice": 10300000,
      "quantity": 1,
      "itemTotalAmountWithoutTax": 10300000,
      "itemTotalAmountWithTax": 11330000,
      "itemTotalAmountAfterDiscount": 10300000,
      "taxPercentage": 10,
      "taxAmount": 1030000,
      "customTaxAmount": "0",
      "discount": 0,
      "itemDiscount": 0,
      "batchNo": "",
      "expDate": ""
    }
  ]
Hàng hóa kèm ghi chú:
"itemInfo": [
    {
      "lineNumber": 2,
      "selection": 2,
      "itemName": "Ghi chú cho hóa đơn",
    }
  ]
Hàng hóa có chiết khấu trên dòng sản phẩm
"itemInfo": [
    {
      "lineNumber": 1,
      "itemCode": "LCDLI2215S_LNV",
      "itemName": "Màn hình vi tính LENOVO LCD LI2215S 21.5\" Led (65CCAACC6VN)",
      "unitName": "Cái",
      "itemNote": "",
      "unitPrice": 1750000,
      "quantity": 2,
      "itemTotalAmountWithoutTax": 3500000,
      "itemTotalAmountWithTax": 3696000,
      "itemTotalAmountAfterDiscount": 3360000,
      "taxPercentage": 10,
      "taxAmount": 336000,
      "customTaxAmount": "0",
      "discount": 4,
      "itemDiscount": 140000,
      "batchNo": "",
      "expDate": ""
    }
  ]
Hàng hóa có dòng chiết khấu
"itemInfo": [
    {
      "lineNumber": 2,
      "itemCode": "chieu_khau_hang_hoa",
      "selection": 3,
      "itemName": "Chiếu khấu hàng hóa",
      "unitName": "",
      "itemNote": "",
      "itemTotalAmountWithoutTax": 50000,
      "itemTotalAmountWithTax": 50000,
      "itemTotalAmountAfterDiscount": 50000,
      "taxPercentage": 0,
      "taxAmount": 0,
      "customTaxAmount": "0",
      "discount": 0,
      "itemDiscount": 0,
      "isIncreaseItem": false,
      "batchNo": "",
      "expDate": ""
    }
  ]
Hàng hóa dạng bảng kê
"itemInfo": [
    {
      "lineNumber": 1,
      "itemCode": "bang_ke_hang_hoa",
      "selection": 4,
      "itemName": "Bảng kê hàng hóa",
      "unitName": "",
      "itemNote": "",
      "itemTotalAmountWithoutTax": 97770000,
      "itemTotalAmountWithTax": 107547000,
      "itemTotalAmountAfterDiscount": 97770000,
      "taxPercentage": 10,
      "taxAmount": 9777000,
      "customTaxAmount": "0",
      "discount": 0,
      "itemDiscount": 0,
      "batchNo": "",
      "expDate": ""
    }
  ]
Hàng hóa có kèm phí khác
"itemInfo": [
    {
      "lineNumber": 2,
      "itemCode": "phi_bao_tri",
      "selection": 5,
      "itemName": "Phí bảo trì",
      "unitName": "",
      "itemNote": "",
      "unitPrice": 20000,
      "quantity": 1,
      "itemTotalAmountWithoutTax": 20000,
      "itemTotalAmountWithTax": 20000,
      "itemTotalAmountAfterDiscount": 20000,
      "taxPercentage": 0,
      "taxAmount": 0,
      "customTaxAmount": "0",
      "discount": 0,
      "itemDiscount": 0,
      "batchNo": "",
      "expDate": ""
    }
  ]
Hàng hóa là điều chỉnh giảm
"itemInfo": [
    {
      "lineNumber": 1,
      "itemCode": "DELL_LJ2350D",
      "itemName": "Máy in Dell LJ 2350D 1Y Wty",
      "unitName": "Cái",
      "itemNote": "",
      "unitPrice": 6281000,
      "quantity": 3,
      "itemTotalAmountWithoutTax": 18843000,
      "itemTotalAmountWithTax": 20727300,
      "itemTotalAmountAfterDiscount": 18843000,
      "taxPercentage": 10,
      "taxAmount": 1884300,
      "customTaxAmount": "0",
      "adjustmentTaxAmount": 1,
      "discount": 0,
      "itemDiscount": 0,
      "isIncreaseItem": false,
      "batchNo": "",
      "expDate": ""
    }
    }
  ]
Hàng hóa là điều chỉnh tăng
"itemInfo": [
    {
      "lineNumber": 1,
      "itemCode": "DELL_LJ2350D",
      "itemName": " Máy in Dell LJ 2350D 1Y Wty",
      "unitName": "Cái",
      "itemNote": "",
      "unitPrice": 6281000,
      "quantity": 5,
      "itemTotalAmountWithoutTax": 31405000,
      "itemTotalAmountWithTax": 34545500,
      "itemTotalAmountAfterDiscount": 31405000,
      "taxPercentage": 10,
      "taxAmount": 3140500,
      "customTaxAmount": "0",
      "adjustmentTaxAmount": 1,
      "discount": 0,
      "itemDiscount": 0,
      "isIncreaseItem": true,
      "batchNo": "",
      "expDate": ""
    }
]
Ghi chú của hóa đơn điều chỉnh tiền, điều chỉnh thông tin, hóa đơn thay thế sẽ được chuyển vào invoiceNote trong generalInvoiceInfo
Hàng hoá truyền itemNote 
Ví dụ hoá đơn điều chỉnh tăng số lượng, giảm đơn giá cho hàng hoá là Máy tính
{
  "lineNumber": 1,
  "itemCode": "",
  "itemName": "Máy tính",
  "unitName": "Chiếc",
  "unitPrice": 1500000,
  "quantity": 20,
  "selection": 1,
  "itemTotalAmountWithoutTax": 30000000,
  "taxPercentage": 10,
  "taxAmount": 3000000,
  "discount": null,
  "discount2": null,
  "itemDiscount": 0,
  "itemNote": "Điều chỉnh tăng số lượng, giảm đơn giá",
  "batchNo": null,
  "expDate": null,
  "isIncreaseItem": true
  "adjustRatio": “1”
}
Hệ thống tự động sinh ghi chú: Điều chỉnh tăng số lượng, giảm đơn giá của hàng hóa dịch vụ: Máy tính
Hàng hoá truyền adjustRatio 
Ví dụ áp dụng Giảm 20% mức tỷ lệ % tính thuế cho hàng hoá là Máy tính, mức tỷ lệ % tính thuế là 1%.
{
  "lineNumber": 1,
  "itemCode": "",
  "itemName": "Máy tính",
  "unitName": "Chiếc",
  "unitPrice": 1500000,
  "quantity": 20,
  "selection": 1,
  "itemTotalAmountWithoutTax": 30000000,
  "taxPercentage": null,
  "taxAmount": null,
  "discount": null,
  "discount2": null,
  "itemDiscount": 0,
  "itemNote": null,
  "batchNo": null,
  "expDate": null,
  "adjustRatio": “1”
}
Hàng hoá truyền vào API lập hóa đơn nháp xăng dầu 
{
            "lineNumber": 1,
            "selection": 1,
            "itemCode": "Ron92",
            "itemName": "Xăng Ron 92",
            "unitName": "lít",
            "itemNote": "",
            "unitPrice": null,
	"unitPriceWithTax": 22000,
            "quantity": 10,
            "itemTotalAmountWithoutTax": null,
            "taxPercentage": null,
            "taxAmount": null,
            "discount": null,
            "itemDiscount": null,
            "batchNo": "",
            "itemTotalAmountWithTax": 220000,
            "itemTotalAmountAfterDiscount": null,
            "expDate": ""
}

6.7	taxBreakdowns
Dùng để tổng hợp thuế suất theo mức cho hóa đơn.
Tên trường	Kiểu dữ liệu	Mô tả
taxPercentage	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Mức thuế: khai báo giá trị như sau 
-2: không thuế
-1: không kê khai tính/nộp thuế 
0: 0%
5: 5%
8: 8%
10: 10%

Note: Mỗi một giá trị thuế chỉ xuất hiện 1 lần (lưu giá trị tổng hợp các hàng hóa cùng loại thuế đó)

Bắt buộc nhập với mẫu thuế Tổng

Trường hợp người dùng không truyền thông tin thì lưu giá trị null vào list_product trong bảng invoice. 
khác
Lưu ý: trường hợp đối với hóa đơn thuế tổng, hàng hóa có tính chất ghi chú không truyền giá trị vatPercentage thì lưu giá trị thuế suất của hàng hóa là NULL, không lấy theo vatPercentage trong taxBreakDowns như hiện tại.
Nếu truyền loại thuế suất khác thì truyền giá trị % thuế suất.
VD: Khác 12.34% thì truyền “taxPercentage”: 12.34
taxableAmount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Tổng tiền chịu thuế của mức thuế tương ứng, tổng tiền chịu thuế không có số âm. Bằng tổng của itemTotalAmountWithoutTax của tất cả các itemInfo có mức thuế suất giống với mức thuế suất tổng hợp. Trong trường hợp dòng hàng hóa là chiết khấu thì trừ đi.
Không cần nhập liệu, hệ thống tự tính dựa vào các itemTotalAmountWithoutTax
taxAmount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Tổng tiền thuế của mức thuế tương ứng, tổng tiền thuế không có số âm. Bằng tổng của taxAmount của tất cả các itemInfo có mức thuế suất giống với mức thuế suất tổng hợp. Trong trường hợp dòng hàng hóa là chiết khấu thì trừ đi.
Không cần nhập dữ liệu, nếu không truyền dữ liệu, hệ thống sẽ tự tính dựa vào taxPercentag và các itemTotalAmountWithoutTax.
Nếu nhập dữ liệu cho phép chênh lệch 20,000 so với giá trị hệ thống tự tính
taxableAmountPos	Required: false
DataType: Boolean
Minlength: 
Maxlength: 
Format:	Dùng để biểu thị tổng tiền chịu thuế của mức thuế là âm hay dương. 
- null/true: Tổng tiền đánh thuế dương. Được sử dụng đối với các hàng hóa thông thường. 
- false: Tổng tiền đánh thuế âm, được sử dụng với hóa đơn điều chỉnh giảm hoặc hóa đơn có hàng hóa là chiết khấu mà tổng tiền của hàng hóa và chiết khấu của mức thuế là âm.
taxAmountPos	Required: false
DataType: Boolean
Minlength: 
Maxlength: 20
Format:	Dùng để biểu thị tổng tiền thuế của mức thuế là âm hay dương. Giá trị của taxAmountPos luôn giống với giá trị của taxableAmountPos. 
- null/true: Tổng tiền thuế dương 
- false: Tổng tiền thuế âm
taxExemptionReason	Required: false
DataType: String
Minlength: 
Maxlength: 255
Format:	Lý do miễn giảm thuế


Lưu ý: Hệ thống so sánh tổng của itemTotalAmountWithoutTax của tất cả các itemInfo trong cùng mức thuế suất với taxableAmount trong taxBreakDowns. Trong trường hợp bị lệch hệ thống sẽ báo lỗi.
Hệ thống so sánh tổng của taxAmount của tất cả các itemInfo trong cùng mức thuế suất với taxAmount trong taxBreakDowns. Trong trường hợp bị lệch hệ thống sẽ báo lỗi.
Cho phép chênh lệch tiền thuế 20,000 so với giá trị thực tính
Dữ liệu mẫu
Thuế có %
"taxBreakdowns": [
    {
      "taxPercentage": 5,
      "taxableAmount": 400000,
      "taxAmount": 20000
    },
    {
      "taxPercentage": 10,
      "taxableAmount": 400000,
      "taxAmount": 40000
    }
  ]
Không thuế
"taxBreakdowns": [
    {
      "taxPercentage": -2,
      "taxableAmount": 400000,
      "taxAmount": 0
    }
  ]
Không kê khai, tính nộp thuế
"taxBreakdowns": [
    {
      "taxPercentage": -1,
      "taxableAmount": 400000,
      "taxAmount": 0
    }
  ]
Hóa đơn có tiền thuế âm
"taxBreakdowns": [
    {
      "taxPercentage": 10,
      "taxableAmount": 100000,//tổng tiền âm 100000
      "taxAmount": 10000,//thuế âm 10000
      "taxableAmountPos": false,
      "taxAmountPos": false
    }
  ]
6.8	summarizeInfo
Dùng để tổng hợp tiền hàng cho toàn bộ hóa đơn. Không sử dụng, hệ thống tự tính tổng tiền hóa đơn, đốiv ới biên lai điện tử summarizeInfo là bắt buộc trường totalAmountWithTax
Tên trường	Kiểu dữ liệu	Mô tả
totalAmountWithoutTax	Required: true
DataType: BigDecimal
Minlength: 
Maxlength: 15
Format: [0-9.]+	Tổng tiền hóa đơn chưa bao gồm VAT (đã tính hàng hóa chiết khấu (nếu có)). Tổng tiền hóa đơn không có số âm.
- Hóa đơn thường: Tổng tiền HHDV trên các dòng HĐ và các khoản tăng/giảm khác trên toàn HĐ. 
- Hóa đơn điều chỉnh: Tổng tiền điều chỉnh của các dòng HĐ và các khoản tăng/giảm khác trên toàn HĐ.
totalTaxAmount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format: [0-9.]+	Tổng tiền thuế trên toàn hóa đơn. Tổng tiền thuế không có số âm.
- Hóa đơn thường: Tổng tiền VAT trên các dòng HĐ và các khoản thuế khác trên toàn HĐ.
- Hóa đơn điều chỉnh: Tổng tiền VAT điều chỉnh của các dòng HĐ và các khoản tăng/giảm VAT khác trên toàn HĐ.

totalAmountWithTax	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format: [0-9.]+	Tổng tiền trên hóa đơn đã bao gồm VAT. Tổng tiền sau thuế không có số âm.
- Hóa đơn thường: Tổng tiền HHDV trên các dòng HĐ và các khoản tăng/giảm khác trên toàn HĐ đã bao gồm cả VAT.
- Hóa đơn điều chỉnh: Tổng tiền điều chỉnh của các dòng HĐ và các khoản tăng/giảm khác trên toàn HĐ đã bao gồm cả VAT
- Đối với biên lại điện tủ phần tiền thì thông tin này là bắt buộc 



totalAmountWithTaxFrn	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format: [0-9.]+	Tổng tiền ngoại tệ của hóa đơn đã bao gồm VAT. Dùng trong trường hợp hóa đơn không chọn loại tiền là VND
- Hóa đơn thường: Tổng tiền HHDV trên các dòng HĐ và các khoản tăng/giảm khác trên toàn HĐ đã bao gồm cả VAT.
- Hóa đơn điều chỉnh: Tổng tiền điều chỉnh của các dòng HĐ và các khoản tăng/giảm khác trên toàn HĐ đã bao gồm cả VAT
totalAmountWithTaxInWords	Required: false
DataType: String
Minlength: 
Maxlength: 255
Format:	Số tiền hóa đơn bao gồm VAT viết bằng chữ. Hệ thống hóa đơn điện tử sẽ tự động sinh lại dữ liệu này để đảm bảo đúng theo dữ liệu hệ thống.


isTotalAmountPos	Required: false
DataType: Boolean
Minlength: 
Maxlength: 20
Format:	Để đánh dấu tổng tiền sau thuế là âm hay dương
- null/True: Tổng tiền là số dương, sử dụng đối với các hóa đơn thông thường hoặc hóa đơn có chiết khấu nhưng tổng tiền vẫn là dương sau khi trừ chiết khấu.
- False: Tổng tiền âm, sử dụng đối với hóa đơn điều chỉnh giảm hoặc có chiết khấu mà tiền chiết khấu lớn hơn tiền hàng hóa thông thường.
isTotalTaxAmountPos	Required: false
DataType: Boolean
Minlength: 
Maxlength: 20
Format:	Để đánh dấu tổng tiền thuế là âm hay dương
- null/true: tổng tiền thuế là dương
- false: tổng tiền thuế là âm


isTotalAmtWithoutTaxPos	Required: false
DataType: Boolean
Minlength: 
Maxlength: 20
Format:	Để đánh dấu tổng tiền trước thuế là âm hay dương
- null/true: tổng tiền trước thuế là dương
- false: tổng tiền trước thuế là âm
discountAmount	Required: true
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format: [0-9.]+	Tổng tiền chiết khấu thương mại trên toàn hóa đơn trước khi tính thuế. Chú ý: Khi tính chiết khấu, toàn hóa đơn chỉ sử dụng một mức thuế. 
Lưu ý: Đối với hóa đơn thuế tổng, chiết khấu trước thuế có 2 cách nước thuế có 2 cách nhập liệu
1.	Nhập tỷ lệ % chiết khấu và tiền chiết khấu trên từng dòng hàng hóa (itemInfo.discount, itemInfo.itemDiscount)
2.	Nhập thêm 1 hàng hóa dạng chiết khấu (selection = 3)
Trường hợp nhập theo cả 2 cách thì discountAmount bằng tổng của 2 giá trị
settlementDiscountAmount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 13
Format: [0-9.]+	Tổng tiền chiết khấu thanh toán trên toàn hóa đơn sau khi tính thuế. Chú ý: Khi tính chiết khấu, toàn hóa đơn chỉ sử dụng một mức thuế.

isDiscountAmtPos	Required: false
DataType: Boolean
Minlength: 
Maxlength: 20
Format:	Trường nhận biết tổng tiền chiết khấu là số dương hay âm
- null/true: tổng tiền chiết khấu là dương
- false: tổng tiền chiết khấu là âm

extraName	Required: false
DataType: String
Minlength: 
Maxlength: 500
Format: {}	Tên bổ sung
Có thể truyền nhiều giá trị được phân cách nhau bằng dấu “,”
Ví dụ: {Phụ phí, Phí thu thêm} 
extraValue	Required: false
DataType: String
Minlength: 
Maxlength: 500
Format: {}	Giá trị của trường bổ sung
Có thể truyền nhiều giá trị được phân cách nhau bằng dấu “,”
Ví dụ: {10000, 100}
totalAmountAfterDiscount	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Là tổng tiền hóa đơn sau khi trừ chiết khấu, giảm giá, chưa bao gồm VAT. Tổng tiền hóa đơn không có số âm.
Lưu ý: Trường hợp truyền giá trị 0 hoặc “0” cho trường validation: bắt buộc phải truyền giá trị khác null

Dữ liệu mẫu
Hóa đơn thường
"summarizeInfo": {
    "sumOfTotalLineAmountWithoutTax": 100000,
    "totalAmountWithoutTax": 100000,
    "totalTaxAmount": 10000,
    "totalAmountWithTax": 110000,
    "totalAmountAfterDiscount": 0,
    "totalAmountWithTaxInWords": "Một trăm mười nghìn đồng",
    "discountAmount": 0,
    "taxPercentage": 10,
    "extraName": "{ Tiền phí đặc biệt, Tiền phí,  } ",
    "extraValue": "{ 00 ,00,}"
  }
Hóa đơn có tổng tiền âm
"summarizeInfo": {
    "sumOfTotalLineAmountWithoutTax": 100000,
    "totalAmountWithoutTax": 100000,
    "totalTaxAmount": 10000,
    "totalAmountWithTax": 110000,
    "totalAmountAfterDiscount": 0,
    "totalAmountWithTaxInWords": "Một trăm mười nghìn đồng",
    "discountAmount": 0,
    "taxPercentage": 10,
    "isTotalAmountPos": false,
    "isTotalTaxAmountPos": false,
    "isTotalAmtWithoutTaxPos": false	
    "extraName": "{ Tiền phí đặc biệt, Tiền phí,  } ",
    "extraValue": "{ 00 ,00,}"	
  }
6.9	metadata
Dữ liệu các trường thông tin động (Thông tin trường bổ sung), ngoài các trường thông tin được mô tả ở trong mục 6 này. Nếu như trường thông tin chưa tồn tại trong mục 5, sẽ phải khai thêm. Trường động này sẽ gắn riêng cho từng mẫu hóa đơn của từng khách hàng. Danh sách các trường động của một mẫu cụ thể sẽ được lấy bằng hàm 7.7
Tên trường	Kiểu dữ liệu	Mô tả
keyTag	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: 	Tên dữ liệu
Text: 
Number:
Date: Duedate

valueType	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: 	Kiểu dữ liệu gồm: text, number, date

dateValue	Required: false
DataType: Date
Minlength: 
Maxlength: 
Format: 	Giá trị dữ liệu khi kiểu là date.

stringValue	Required: false
DataType: String
Minlength: 
Maxlength: 500
Format:	Giá trị dữ liệu khi kiểu là text

numberValue	Required: false
DataType: Integer
Minlength: 
Maxlength: 6
Format:	Giá trị dữ liệu khi kiểu là number

keyLabel	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Nhãn hiển thị của dữ liệu

isRequired	Required: false
DataType: Boolean
Minlength: 
Maxlength: 
Format:	Giá trị có bắt buộc hay không

isSeller	Required: false
DataType: Boolean
Minlength: 
Maxlength: 
Format:	Giá trị của người bán hay mua
False: Người mua
True: Người bán

Dữ liệu mẫu
"metadata": [
    {
      "keyTag": "dueDate",
      "valueType": "date",
      "dateValue": 1544115600000,
      "keyLabel": "Hạn thanh toán",
      "isRequired": false,
      "isSeller": false
    },
    {
      "keyTag": "contractNo",
      "stringValue": "555",
      "valueType": "text",
      "keyLabel": "Hợp dong số",
      "isRequired": false,
      "isSeller": false
    }
  	]

Một số metadata đặc biệt (được sử dụng làm trường chuẩn của XML thông tư 78)
Tên trường	Kiểu dữ liệu	Mô tả
PHIẾU XUẤT KHO KIÊM VẬN CHUYỂN NỘI BỘ
economicContractNo	Required: true
DataType: String
Minlength: 
Maxlength:  
Format:	-	Lệnh điều động nội bộ
-	Tên thẻ trong XML: “LDDNBo”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/LDDNBo”
transformer	Required: false
DataType: String
Minlength: 
Maxlength:  
Format:	-	Tên người vận chuyển
-	Tên thẻ trong XML: “TNVChuyen”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/TNVChuyen”
vehicle	Required: true
DataType: String
Minlength: 
Maxlength:  
Format:	-	Phương tiện vận chuyển
-	Tên thẻ trong XML: “PTVChuyen”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/PTVChuyen”
contractNo	Required: false
DataType: String
Minlength: 
Maxlength:  
Format:	-	Hợp đồng số
-	Tên thẻ trong XML: “HDSo”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/HDSo”
exporterName	Required: false
DataType: String
Minlength: 
Maxlength:  
Format:	-	Họ và tên người xuất hàng
-	Tên thẻ trong XML: “HVTNXHang”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/HVTNXHang”

Một số metadata đặc biệt (được sử dụng làm trường chuẩn của XML thông tư 78)
Tên trường	Kiểu dữ liệu	Mô tả
PHIẾU XUẤT KHO HÀNG GỬI ĐẠI LÝ
economicContractNo	Required: true
DataType: String
Minlength: 
Maxlength:  
Format:	-	Hợp đồng kinh tế số
-	Tên thẻ trong XML: “HDKTSo”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/HDKTSo”
commandDate	Required: true
DataType: Date
Minlength: 
Maxlength:  
Format:	-	Hợp đồng kinh tế ngày 
-	Tên thẻ trong XML: “HDKTNgay”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/HDKTNgay”
transformer	Required: true
DataType: String
Minlength: 
Maxlength:  
Format:	-	Tên người vận chuyển 
-	Tên thẻ trong XML: “TNVChuyen”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/TNVChuyen”
vehicle	Required: true
DataType: String
Minlength: 
Maxlength:  
Format:	-	Phương tiện vận chuyển 
-	Tên thẻ trong XML: “PTVChuyen”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/PTVChuyen”
contractNo	Required: false
DataType: String
Minlength: 
Maxlength:  
Format:	-	Hợp đồng số (Hợp đồng vận chuyển)
-	Tên thẻ trong XML: “HDSo”
-	Vị trí thẻ trong XML:
-	“DLHDon/NDHDon/NBan/HDSo”
HVTNXHang	Required: false
DataType: String
Minlength: 
Maxlength:  
Format:	-	Họ và tên người xuất hàng
-	Tên thẻ trong XML: “HVTNXHang”
-	Vị trí thẻ trong XML:
“DLHDon/NDHDon/NBan/HVTNXHang”

Một số metadata đặc biệt (được sử dụng làm trường chuẩn của XML thông tư 78)
Tên trường	Kiểu dữ liệu	Mô tả
PHIẾU BÁN HÀNG PHI THUẾ QUAN
KPTQuan	Required: true
DataType: String
Minlength: 
Maxlength:  
Format:	-	thể hiện mẫu phi thuế quan
-  truyền giá trị bằng 1 để hiện thỉ mẫu phi thuế quan bên thuế
- Lưu ý định dạng bắt buộc phải là text chứ không được khai báo dạng number hay date.






Một số metadata đặc biệt (được sử dụng làm trường chuẩn của XML thông tư 78)
Tên trường	Kiểu dữ liệu	Mô tả
HÓA ĐƠN GTGT KIÊM TỜ KHAI HOÀN THUẾ
SHChieu	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format:	-	Số hộ chiếu
-	Tên thẻ trong XML: “SHChieu”
-	Vị trí thẻ trong XML:
“HDon\DLHDon\NDHDon\NMua\SHChieu”
NCHChieu	Required: true
DataType: Date
Minlength: 
Maxlength:  
Format:	-	Ngày cấp hộ chiếu
-	Tên thẻ trong XML: “NCHChieu”
-	Vị trí thẻ trong XML:
“HDon\DLHDon\NDHDon\NMua\NCHChieu”
NHHHChieu	Required: true
DataType: Date
Minlength: 
Maxlength:  
Format:	-	Ngày hết hạn hộ chiếu
-	Tên thẻ trong XML: “NHHHChieu”
-	Vị trí thẻ trong XML:
“HDon\DLHDon\NDHDon\NMua\NHHHChieu”
QTich	Required: true
DataType: String
Minlength: 
Maxlength: 50
Format:	-	Quốc tịch
-	Tên thẻ trong XML: “QTich”
-	Vị trí thẻ trong XML:
“HDon\DLHDon\NDHDon\NMua\QTich”

6.10	meterReading
Dữ liệu đặc thù cho riêng hóa đơn điện/nước.
Tên trường	Kiểu dữ liệu	Mô tả
meterName	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Tên chỉ số
previousIndex	Required: false
DataType: Number
Minlength: 
Maxlength: 
Format: 	Chỉ số cũ của hóa đơn điện nước.

currentIndex	Required: false
DataType: Number
Minlength: 
Maxlength: 
Format: 	Chỉ số mới của hóa đơn điện nước.

factor	Required: false
DataType: Number
Minlength: 
Maxlength: 
Format: 	Hệ số nhân của hóa đơn điện nước. Vị dụ như nước sinh hoạt sẽ có hệ số nhân khác với nước kinh doanh. Nội dung này sẽ tùy theo công ty điện/ nước quy định và hiển thị.

amount	Required: false
DataType: Number
Minlength: 
Maxlength: 
Format:	Tổng số của hóa đơn 
Hệ thống không validate công thức tính toán ra giá trị

Dữ liệu mẫu
"meterReading": [{
	            "previousIndex": "110",
	            "currentIndex": "150",
	            "factor": "1",
	            "amount": "40"
	          },
	          {
	            "previousIndex": "44",
	            "currentIndex": "50",
	            "factor": "1",
	            "amount": "6"
	          }]
6.11	invoiceFile
Các file đính kèm khi lập hóa đơn
Tên trường	Kiểu dữ liệu	Mô tả
fileContent	Required: false
DataType: String	Nội dung file dạng chuỗi base64 
fileType	Required: false
DataType: Double
	Loại file
-	1: bảng kê (Cho phép định dạng xlsx)
-	2: biên bản thỏa thuận (Cho phép định dạng .doc, .docx, .pdf, .png, .jpg)
fileExtension	Required: false
DataType: String	Định dạng file theo từng loại tương ứng fileType
Dữ liệu mẫu
"invoiceFile": {
      "fileType": 1,
      "fileExtension": "xlsx",
      "fileContent": "RmlsZSBi4bqjbmcga8OqIMSRxrDhu6NjIGFkZCBsw6puIHThuqFpIHBo4bqnbiBs4bqtcCBow7NhIMSRxqFu"
   }
6.12	qrcode
-	API cho phép người dùng hệ thống tích hợp lập hóa đơn điện tử trên hệ thống hóa đơn điện tử sử dụng chữ ký server.
-	Mô tả chung: Bổ sung thêm thông tin về QRCODE khi lập hóa đơn bằng API tích hợp sử dụng chữ ký server.
-	Input: 
-	Bổ sung thêm 05 trường thông tin trong tham số đầu vào đặt trong qrCodeInfo như sau: 
Tên trường	Kiểu dữ liệu	Mô tả
totalQrcode	Required: false
DataType: int(3)
Minlength: 
Maxlength: 
Format: 	Tổng số lần được quét QRCODE
remainQrcode	Required: false
DataType: int(3)
Minlength: 
Maxlength: 
Format: 	Số lần quét QRCODE còn lại
startDateQrcode	Required: false
DataType: timestamp
Minlength: 
Maxlength: 
Format: 	Thời gian bắt đầu hiệu lực của QRCODE
endDateQrcode	Required: false
DataType: timestamp
Minlength: 
Maxlength: 
Format: 	Thời gian kết thúc hiệu lực của QRCODE
6.13	fuelReading
Dữ liệu đặc thù cho riêng hóa đơn xăng dầu có ghi nhận log bơm.
Tên trường	Kiểu dữ liệu	Mô tả
idLog	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format:	Mã log bơm
noteLog	Required: false
DataType: String
Minlength: 
Maxlength: 100
Format: 	Ghi chú 
pumpCode	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format: 	Mã vòi bơm 
pumpName	Required: false
DataType: String
Minlength: 
Maxlength: 50
Format: 	Tên vòi bơm 
qtyLog	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 20
Format: [0-9.]+	Số lượng log bơm 
Số lượng của hàng hóa, luôn là số dương

priceLog	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 20
Format: [0-9.]+	Đơn giá áp theo cột bơm.
Đơn giá của hàng hóa, không có số âm. 

productCode	Required: false
DataType: string
Minlength: 
Maxlength: 50
Format:	Mã hàng hóa 
productName	Required: false
DataType: string
Minlength: 
Maxlength: 50
Format:	Tên hàng hóa 
startDate	Required: false
DataType: Datetime
Minlength: N/A
Maxlength: 
Format: mục 5.1	Thời gian bắt đầu bơm 
endDate	Required: false
DataType: Datetime
Minlength: N/A
Maxlength: 
Format: mục 5.1	Thời gian kết thúc bơm 
batch	Required: false
DataType: string
Minlength: 
Maxlength: 50
Format:	Mã chứng từ 
thanhTienLog	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 20
Format: [0-9.]+	Thành tiền được tính bằng công thức số lượng * Đơn giá trên cột bơm 



Dữ liệu mẫu
    "fuelReading": [
        {
            "idLog": 1,
            "noteLog": "Ghi chu 1",
            "pumpCode": "code1",
            "pumpName": "name1",
            "qtyLog": 1,
            "priceLog": 20000,
            "productCode": "pCode1",
            "productName": "pName1",
            "startDate": 1700594681000,
            "endDate": 1700594681000,
            "batch": "Ma01",
            "thanhTienLog": 20000
        },
        {
            "idLog": 2,
            "noteLog": "Ghi chu 2",
            "pumpCode": "code2",
            "pumpName": "name2",
            "qtyLog": 1,
            "priceLog": 200000,
            "productCode": "pCode2",
            "productName": "pName2",
            "startDate": 1700594681000,
            "endDate": 1700594681000,
            "batch": "Ma01",
            "thanhTienLog": 200000
        }
    ]

7.	Các API kết nối
7.1	 Các khái niệm chung  
Giải thích 1 request bao gồm
-	Action: Phương thức và hàm thực thi (Vị dụ: “/InvoiceAPI/InvoiceWS” phương thức POST).
-	Content-Type: Kiểu thông tin request
-	Data: định dạng dữ liệu truyền vào.
-	Đầu ra webservice: Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về 
-	Thông tin hệ thống test (Thực hiện test kết nối trên hệ thống test không test kết nối trên hệ thống thật)
-	Thông tin hệ thống tích hợp 
Link web: https://vinvoice.viettel.vn
Link API: https://api-vinvoice.viettel.vn/services/einvoiceapplication/api/
-	Header xác thực: Header xác thực được gửi đi cùng mỗi request trong quá trình sử dụng. Xác thực bằng token sinh ra sau khi thực hiện gọi API login trong mục 5.5. Header cần truyền thêm thông tin Cookie có access_token dạng access_token=abc_def (Xem Vị dụ tại 5.5.	Tiêu chuẩn bảo mật kết nối)
C#: 
WebRequest request = WebRequest.Create(pzUrl);
request.Headers.Add("Cookie","access_token=abc_def");
Java: 
String path = "url";
HttpPost post = new HttpPost(path);
post.setHeader("Cookie", "access_token=abc_def");
-	Header định dạng dữ liệu: Dữ liệu gửi lên Web service có thể là JSON, FormParam hay QueryParam
o	Với JSON: Thêm header: Content-Type: application/json
o	Với FormParam: Thêm header: Content-Type: application/x-www-form-urlencoded
o	Với QueryParam: Không cần header, tham số truyền vào qua URL
-	Dữ liệu trả về từ Web service là JSON
o	Để nhận về JSON: Thêm header: Accept: application/json
Lưu ý: Do cần thời gian kết nối và thời gian xử lý yêu cầu nên kết quả trả về có thể phải chờ 1 khoảng thời gian (khuyến nghị để thời gian timeout khi gửi yêu cầu khoảng 60-90 giây)
7.2	 Phát hành/thay thế/điều chỉnh hóa đơn cho CTS SERVER
* Quy tắc kiểm tra ngày lập hóa đơn:
Hệ thống Hóa đơn điện tử SInvoice V2, phần Cấu hình chung liên quan ngày lập hóa đơn có 2 checkbox: Cho phép ngày lập hóa đơn khác ngày hiện tại, Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất.
Khi phát hành hóa đơn qua API, ngày lập hóa đơn sẽ bị ảnh hưởng khi người dùng tích chọn các checkbox này, xảy ra 4 trường hợp như mô tả sau:
TH1: Không tích cả 2
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: ngày lập không hợp lệ
- Ngày lập > ngày hiện tại: lấy ngày truyền vào (không kiểm tra giờ)
TH2: Tích “Cấu hình ngày ký là thời điểm hiện tại”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH3: Tích “Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH4: Tích cả 2 
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại:  lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
	Đầu vào:
Webservice dùng chung trong các trường hợp lập hóa đơn gốc, lập hóa đơn điều chỉnh tiền, lập hóa đơn điều chỉnh thông tin, lập hóa đơn thay thế
-	Action (POST): InvoiceAPI/InvoiceWS/createInvoice/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 


Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format : 	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
Hệ thống sẽ dùng trường thông tin này để kiểm tra và lấy thông tin về mã số thuế của chi nhánh/doanh nghiệp.
https://vi.wikipedia.org/wiki/Thu%E1%BA%BF_Vi%E1%BB%87t_Nam 
Trong quá trình tích hợp nếu đơn vị sử dụng nhiều tài khoản của nhiều phòng ban để phát hành hóa đơn cùng lúc thì nên tách mỗi phòng ban 1 ký hiệu hóa đơn để sử dụng. 
Vị dụ:
+ Phòng kế toán dùng ký hiệu: C22TKT
+ Phòng tổng hợp dùng ký hiệu: C22TTH
Ngoài ra có thể áp dụng phân tách ký hiệu hóa đơn theo user sử dụng
Vị dụ:
+ Tài khoản A dùng ký hiệu C22TAA
+ Tài khoản B dùng ký hiệu C22TBB
originalInvoiceType	Required: True
DataType: String
Minlength: N/A
Maxlength: 
Format:	Loại hóa đơn gốc
Truyền giá trị số với ý nghĩa như sau 
0- Không phải hóa đơn giấy/hóa đơn không tồn tại trên hệ thống 
1-Hóa đơn TT78 
2-Hóa đơn theo QĐ 1209 
3-Hóa đơn điện tử/giấy TT32
4-Hóa đơn giấy TT 78
Chú ý: 
- Trường hợp thẻ originalInvoiceType không truyền hoặc truyền giá trị rỗng/0 thì không bắt buộc truyền thẻ originalTemplateCode, hệ thống xác thực thông tin khi lập hóa đơn như hiện trạng. 
- Trường hợp thẻ originalInvoiceType truyền giá trị 1, 2, 3 hoặc 4 thì 
+ Bắt buộc phải truyền thẻ originalTemplateCode, quy tắc xác thực thẻ này tương tự như thẻ templateCode hiện tại. 
 + Khi lập hóa đơn, hệ thống không kiểm tra tính tồn tại của hóa đơn gốc trên hệ thống, các quy tắc xác thực khác giữ nguyên hiện trạng
originalTemplateCode	Required: 
DataType: String
Minlength: N/A
Maxlength: 20
Format:	Bắt buộc truyền nếu originalInvoiceType là 1, 2, 3 hoặc 4
Ví dụ mẫu TT32: 01GTKT0/001
Ví dụ mẫu TT78: 1/0224
-	Data: Dữ liệu mẫu lập hóa đơn (Chi tiết các đối tượng xem từng mục nhỏ trong phần 6)
{
   "generalInvoiceInfo":{ //Thông tin chung của hóa đơn
   },
   "buyerInfo":{      //thông tin người bán
   },
   "sellerInfo":{      //thông tin người mua
   },
   "payments":[	//thông tin thanh toán      
   ],
   "itemInfo":[      //thông tin hàng hóa
   ],   
   "metadata":[	//thông tin trường động
   ],
   "meterReading": 	//thông tin đặc biệt dành cho hóa đơn điện nước
   ],
   "summarizeInfo":{	//thông tin tổng hợp tiền của hóa đơn
   },
   "taxBreakdowns":[	//thông tin gom nhóm tiền hóa đơn theo thuế suất
   ]
}

Lưu ý: 
1.	Các dữ liệu này bao gồm tất cả các trường dữ liệu có thể có khi lập hóa đơn. Không phải tất cả các trường thông tin đều bắt buộc, người dùng có thể bỏ bớt cho phù hợp với nhu cầu của khách hàng. Chi tiết các trường thông tin bắt buộc hoặc không bắt buộc xem ở mục 6.
2.	Nếu là lập hóa đơn máy tính tiền thì respond trả về có cả thông tin Mã CQT cấp: "codeOfTax", nếu không phải hóa đơn máy tính tiền thì trả về “codeOfTax” = null
VD mẫu output
{
    "errorCode": null,
    "description": null,
    "result": {
        "supplierTaxCode": "0100109106-710",
        "invoiceNo": "C23MHY3",
        "transactionID": "168378907853232661",
        "reservationCode": "2QTBFEMAXFWZO5B",
        "codeOfTax": "M1-23-34567-00000000201"
    }
}
3.	Nếu cấu hình Không ký hóa đơn có mã khởi tạo từ máy tính tiền và hóa đơn thuộc loại máy tính tiền thì cho phép doanh nghiệp dùng chữ ký USB Token và CloudCA lập hóa đơn Phát hành bằng API Server.
4.	Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
5.	Do cơ chế xử lý bất đồng bộ nên nếu response trả về không có số hóa đơn: "invoiceNo":""
	Sau 30s-90s Gọi thêm 1 bước lấy lại số hóa đơn bẳng hàm tra cứu hóa đơn bẳng transactionUid: (tài liệu 7.21	Tra cứu hóa đơn bằng transactionUuid) (Đề xuất viết 1 luồng offline quét những hóa đơn phát hành thành công nhưng chưa có số để lấy lại số hóa đơn)
Dữ liệu mẫu	JSON	Lưu ý
Hóa đơn gốc	        

Hóa đơn thay thế	 

Hóa đơn điều chỉnh thông tin 	 
Không ghi nhận các giá trị trong itemInfo
Hóa đơn điều chỉnh tiền 	 
Không ghi nhận các giá trị trong buyerInfo
Phiếu xuất kho nội bộ	   
Lưu ý 2 giá trị economicContractNo, vehicle là bắt buộc phải truyền với thông tư 78
Phiếu xuất kho đại lý	 
Lưu ý 4 giá trị economicContractNo, vehicle, commandDate, transformer là bắt buộc phải truyền với thông tư 78
Hóa đơn xăng dầu	 


	Đầu ra:
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về:
	Dữ liệu về thông tin về hóa đơn đã lập
{
  "errorCode": "",
  "description": "",
  "result": {
    "supplierTaxCode": 1258694363,
    "invoiceNo": AA/20E0000001,
    "transactionID": 12523522245,
    "reservationCode": AXHBNK8I0H
  }
}

Ví dụ response trường hợp truyền sai giá trị originalInvoiceType
{
    "code": 400,
    "message": "BAD_REQUEST_ORIGINAL_INVOICE_TYPE_INVALID",
    "data": "BAD_REQUEST_ORIGINAL_INVOICE_TYPE_INVALID"
}

Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lập hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lập hóa đơn thành công)
supplierTaxCode	Mã số thuế người bán (doanh nghiệp phát hành hóa đơn)
invoiceNo	Số hóa đơn Vị dụ: AA/20E0000001 
transactionID	Id của giao dịch
reservationCode	Mã số bí mật dùng để khách hàng tra cứu
	Vị dụ: 
 

 
7.3	 Lấy file hóa đơn
Webservice dùng cho hệ thống tích hợp có thể lấy các file hóa đơn sau khi được phát hành thành công. 
Lưu ý: 
	Hệ thống hóa đơn điện tử chạy theo cơ chế bất đồng bộ, vì vậy hệ thống đẩy hóa đơn lên cơ sở dữ liệu sau khi nhận request phát hành hóa đơn khoảng 1s. Vì vậy, khi tích hợp, request lấy file hóa đơn nên được thực hiện sau từ 2-5 giây sau khi phát hành hóa đơn.
	Hệ thống chỉ lấy lên những hóa đơn có trạng thái khả dụng (state = 1).
	Đầu vào:
-	Action (POST): /InvoiceAPI/InvoiceUtilsWS/getInvoiceRepresentationFile
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json
Các tham số của đối tượng CommonDataInput
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
https://vi.wikipedia.org/wiki/Thu%E1%BA%BF_Vi%E1%BB%87t_Nam

invoiceNo	Required : true
DataType: String
Minlength: 7
Maxlength: 35
Format : [a-zA-Z0-9]*$	Số hóa đơn, bao gồm ký hiệu hóa đơn và số thứ tự hóa đơn

templateCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : 	Mã mẫu hóa đơn
VD: 
01GTKT0/001
1/001
transactionUuid	Required : false
DataType: String
Minlength : 10
Maxlength : 36
Format : N/A	Chuỗi kiểm tra dữ liệu (fkey) được truyền vào khi lập hóa đơn. Chi tiết xem mục 6.2

fileType	Required : false
DataType: String
Minlength : 3
Maxlength : 3
Format : N/A	Loại file muốn tải về, các định dạng được phép 
ZIP, PDF

paid	Required : false
DataType: boolean
Minlength : 
Maxlength : 
Format : N/A	true – Đã thanh toán
false – Chưa thanh toán

startDate	Required : false
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required : false
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập đến ngày
Định dạng "2019-05-12"
Lưu ý: Khoảng thời gian lập tối đa 3 tháng
(endDate – startDate) <= 3 tháng
Vị dụ mẫu và các trường dữ liệu:
-	JSON:
{
"supplierTaxCode":"0100109106-712",
"invoiceNo":"AA/20E0000166",
"templateCode":"01GTKT0/002",
"transactionUuid":"testuuid9999999",
"fileType":"ZIP"
}
	Đầu ra:
Đối tượng Response với HTTPStatus và output Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null không có lỗi gì xảy ra)
description	Mô tả lỗi (giá trị là null không có lỗi gì xảy ra)
fileName	Tên file tải về
fileToBytes	Nội dung file được chuyển thành kiểu byte
Mảng bytes file hóa đơn, chuyển mảng bytes này ra file sẽ được file chứa các thông tin của hóa đơn, Vị dụ file .zip bao gồm file .xml, .xsl, ảnh logo, watermark, qrcode
Code chuyển ra file Java
FileUtils.writeByteArrayToFile(newFile("D:/viettel/fileName.zip"), output.getFileToBytes());

7.4	 Lấy file hóa đơn có mã số bí mật
Cho phép lấy file hóa đơn được phát hành thành công có kiểm tra mã số bí mật.
Lưu ý: 
	Hệ thống hóa đơn điện tử chạy theo cơ chế bất đồng bộ, vì vậy hệ thống đẩy hóa đơn lên cơ sở dữ liệu sau khi nhận request phát hành hóa đơn khoảng 1s. Vì vậy, khi tích hợp, request lấy file hóa đơn nên được thực hiện sau từ 2-5 giây sau khi phát hành hóa đơn.
	Hệ thống chỉ lấy lên những hóa đơn có trạng thái khả dụng (state = 1).
	Đầu vào:
-	Action (POST): InvoiceAPI/InvoiceUtilsWS/getInvoiceFilePortal
-	Headers:
 + Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
 + Content-Type : application/x-www-form-urlencoded

Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

templateCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : 	Mã mẫu hóa đơn
VD: 
01GTKT0/001
1/001
invoiceNo	Required: true
DataType: String
Minlength: 7
Maxlength: 35
Format:  [a-zA-Z0-9]*$	Là số hóa đơn = ký hiệu hóa đơn + số thứ tự hóa đơn vd: AA/20E0000001, tuân theo chuẩn của cục thuế

buyerIdNo	Required: false
DataType: String
Minlength: 
Maxlength: 100
Format:	Số giấy tờ của người mua

reservationCode	Required: true
DataType: String
Minlength: 
Maxlength: 100
Format:	Mã số bí mật

fileType	Required: true
DataType: String
Minlength: 
Maxlength: 100
Format: 	Loại file: zip

strIssueDate	Required: true
DataType: milisecond since epoch
Minlength: 
Maxlength: 
Format: Tiêu chuẩn 5.1	Ngày phát hành hóa đơn

startDate	Required : false
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required : false
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập đến ngày
Định dạng "2019-05-12"
Lưu ý: Khoảng thời gian lập tối đa 3 tháng
(endDate – startDate) <= 3 tháng
VD:
 

Đầu ra:
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về:
-	Ví dụ: kết quả trả về với dạng FormParam
 
Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lấy hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lấy hóa đơn thành công)
fileToBytes	Mảng bytes file hóa đơn, chuyển mảng bytes này ra file sẽ được file chứa các thông tin của hóa đơn, Vị dụ file .zip bao gồm file .xml, .xsl, ảnh logo, watermark, qrcode
Code chuyển ra file Java
FileUtils.writeByteArrayToFile(newFile("D:/viettel/fileName.zip"), output.getFileToBytes());
paymentStatus	Trạng thái thanh toán 
fileName	Tên file
   
7.5	 Lấy file hóa đơn chuyển đổi (pdf)
Cho phép hệ thống tích hợp lấy file hóa đơn chuyển đổi của hóa đơn điện tử. Trong trường hợp hóa đơn đã được chuyển đổi trước đó, SInvoice sẽ cho tải lại file cũ mà không tạo ra file mới (Điều kiện phải cùng exchangeUser như lần chuyển đổi đầu tiên)

Lưu ý: 
	Hệ thống hóa đơn điện tử chạy theo cơ chế bất đồng bộ, vì vậy hệ thống đẩy hóa đơn lên cơ sở dữ liệu sau khi nhận request phát hành hóa đơn khoảng 1s. Vì vậy, khi tích hợp, request lấy file hóa đơn nên được thực hiện sau từ 2-5 giây sau khi phát hành hóa đơn.
	Hệ thống chỉ lấy lên những hóa đơn có trạng thái khả dụng (state = 1).
	Đầu vào:
-	Action (POST): InvoiceAPI/InvoiceWS/createExchangeInvoiceFile
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/x-www-form-urlencoded

Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế bên bán
Mã mẫu hóa đơn, tuân thủ theo quy định ký hiệu mẫu hóa đơn của Thông tư hướng dẫn thi hành nghị định số 51/2010/NĐ-CP

invoiceNo	Required : true
DataType: String
Minlength : 7
Maxlength : 35
Format :  [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + số hóa đơn vd : AA/20E0000001

strIssueDate	Required : true
DataType: milisecond
Minlength : 
Maxlength : 
Format: Tiêu chuẩn 5.1	Ngày phát hành hóa đơn

exchangeUser	Required : true
DataType: String
Minlength : 
Maxlength : 100	Tên người chuyển đổi (Cần thực hiện encode giá trị: Tham khảo: https://www.urlencoder.org/)

startDate	Required : false
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required : false
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập đến ngày
Định dạng "2019-05-12"
Lưu ý: Khoảng thời gian lập tối đa 3 tháng
(endDate – startDate) <= 3 tháng

-	Data: định dạng FormParam của các tham số truyền vào.
 
	Đầu ra:
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về:
Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lấy hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lấy hóa đơn thành công)
fileToBytes	Mảng bytes file hóa đơn, chuyển mảng bytes này ra file sẽ được file pdf hóa đơn chuyển đổi 
Code chuyển ra file Java
FileUtils.writeByteArrayToFile(newFile("D:/viettel/fileName.pdf"), output.getFileToBytes());
fileName	Tên của file hóa đơn










Hình ảnh Response trả về
 
7.6	Tra cứu hóa đơn
Trường hợp doanh nghiệp có trang webportal để tra cứu hóa đơn thì có thể kết nối đến webservice Hóa đơn điện tử của Viettel để tra cứu hóa đơn theo các điều kiện.
Vị dụ khách hàng của doanh nghiệp có thể tra cứu được các hóa đơn của mình theo khoảng thời gian. 
	Đầu vào:
-	Action (POST): InvoiceAPI/InvoiceUtilsWS/getInvoices/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : false
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
GetInvoiceInput	Object	Đối tượng gồm các trường dữ liệu tham số

-	Data: JSON
o	Các tham số của đối tượng GetInvoiceInput
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
invoiceNo	Required : false
DataType: String
Minlength : 7
Maxlength : 35
Format :  [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + số hóa đơn vd : AA/20E0000001

startDate	Required : true
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required : true
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập đến ngày
Định dạng "2019-05-12"

invoiceType	Required : false
DataType: String
Minlength : 
Maxlength : 
Format : 	Loại hóa đơn, là một trong các giá trị
Thông tư 32: 01GTKT, 02GTTT, 03XKNB,  04HGDL, 07KPTQ
Thông tư 78: 1, 2, 3, 4, 5, 6
rowPerPage	Required : true
DataType: Number
Min : 1
Max: 	Số dòng trên một trang 
pageNum	Required : true
DataType: Number
Min : 0
Max	Chỉ số trang
buyerTaxCode	Required : false
DataType: String
Minlength : 
Maxlength : 20	Mã số thuế của khách hàng

buyerIdNo	Required : false
DataType: String	Số giấy tờ của khách hang

templateCode	Required : false
DataType: String
Minlength : 
Maxlength : 	Mã mẫu hóa đơn.

invoiceSeri	Required : false
DataType: String
Minlength : 
Maxlength : 25
Format : [a-zA-Z0-9]*$	Ký hiệu hóa đơn

getAll	Required : false
DataType: Boolean
Minlength: 
Maxlength: 
Format : true/false	Cho phép tra cứu thông tin hóa đơn của toàn doanh nghiệp đối với user của công ty mẹ.
Các giá trị là true/false
issueStartDate	Required: false
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày phát hành từ ngày
Định dạng "2019-05-12"

issueEndDate	Required: false
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày phát hành đến ngày
Định dạng "2019-05-12"

adjustmentType	Required: false
DataType: String
Minlength: 
Maxlength: 1
Format:	Trạng thái điều chỉnh hóa đơn: 
1: Hóa đơn gốc (hóa đơn đã phát hành, hóa đơn bị điều chỉnh, hóa đơn bị thay thế)
3: Hóa đơn thay thế 
5: Hóa đơn điều chỉnh thông tin
7: Hóa đơn xóa bỏ
9: Hóa đơn điều chỉnh tiền
Không truyền sẽ trả tất cả
Vị dụ gửi dữ liệu với JSON:
{
  "startDate" : "2020-05-12" ,
  "endDate" : "2020-05-12",
  "invoiceType" : "02GTTT",
  "rowPerPage" : 20,
  "pageNum" : 1,
  "templateCode" : null
}



	Đầu ra:
{
    "errorCode": null,
    "description": null,
    "totalRow": 286,
    "invoices": [
        {
            "invoiceId": 213469,
            "invoiceType": "02GTTT",
            "adjustmentType": "1",
            "templateCode": "02GTTT0/089",
            "invoiceSeri": "QT/17E",
            "invoiceNumber": "0000003",
            "invoiceNo": "QT/17E0000003",
            "currency": "VND",
            "total": 3800000,
            "issueDate": 1587797116843,
            "issueDateStr": null,
            "state": null,
            "requestDate": null,
            "description": null,
            "buyerIdNo": null,
            "stateCode": null,
            "subscriberNumber": null,
            "paymentStatus": 1,
            "viewStatus": 1,
            "downloadStatus": null,
            "exchangeStatus": null,
            "numOfExchange": null,
            "createTime": 1587797116843,
            "contractId": null,
            "contractNo": null,
            "supplierTaxCode": "0100109106",
            "buyerTaxCode": "6200000230",
            "totalBeforeTax": 3800000,
            "taxAmount": 0,
            "taxRate": null,
            "paymentMethod": null,
            "paymentTime": null,
            "customerId": null,
            "buyerName": "Trần Trung Dũng",
            "no": null,
            "paymentStatusName": null
             "originalInvoiceId": "K22THY32"
        }
}
Đối tượng Response với HTTPStatus và output  Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null lấy hóa đơn thành công)
description	Mô tả lỗi (giá trị là null lấy hóa đơn thành công)
List<InvoiceBean>	Danh sách các bản ghi hóa đơn thỏa mãn điều kiện  

7.7	 Lấy thông tin trường động
Với mỗi mẫu hóa đơn, có thể có những thông tin trường động khác nhau (các trường thông tin ngoài các trường tĩnh được mô tả ở mục 6). SInvoice cho phép các hệ thống tích hợp có thể lấy thông tin trường động của một mẫu hóa đơn cụ thể mà khách hàng sử dụng.
	Đầu vào:
-	Action (GET): /InvoiceAPI/InvoiceWS/getCustomFields?taxCode=&templateCode=
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
Vị dụ : /InvoiceAPI/InvoiceWS/getCustomFields?taxCode=0100109106&templateCode=01GTKT0%2f001
-	Data: dữ liệu truyền vào dạng Query Param gồm các tham số:
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
taxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế
templateCode	Required : false
DataType: String
Minlength : 
Maxlength : 20
Format : [a-zA-Z0-9/]+	Mã mẫu hóa đơn, tuân thủ theo quy định ký hiệu mẫu hóa đơn của Thông tư hướng dẫn thi hành nghị định số 51/2010/NĐ-CP

Chú ý: Mẫu hóa đơn có ít nhất 1 thông báo phát hành ở trạng thái dự thảo mới có thể lấy danh sách trường động qua API
	Đầu ra:
Đối tượng Response là danh sách trường động tương ứng với mẫu hóa đơn của doanh nghiệp:
	Vị dụ:
 
Kết quả:
"errorCode": null,
    "description": null,
    "customFields": [
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "commandDes",
            "valueType": "text",
            "keyLabel": "về việc",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "contractNo",
            "valueType": "text",
            "keyLabel": "Hợp đồng số",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "vehicle",
            "valueType": "text",
            "keyLabel": "Phương tiện vận chuyển",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "exportAt",
            "valueType": "text",
            "keyLabel": "Xuất tại kho",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "exportAtNo",
            "valueType": "text",
            "keyLabel": "Mã kho",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "importAt",
            "valueType": "text",
            "keyLabel": "Nhập tại kho",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "importAtNo",
            "valueType": "text",
            "keyLabel": "Mã kho",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "vehicleNo",
            "valueType": "text",
            "keyLabel": "Số xe",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "economicContractNo",
            "valueType": "text",
            "keyLabel": "Căn cứ hợp đồng kinh tế số",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "commandDate",
            "valueType": "date",
            "keyLabel": "Ngày điều động",
            "isRequired": false,
            "isSeller": false
        },
        {
            "id": null,
            "invoiceTemplatePrototypeId": 2503,
            "keyTag": "commandOf",
            "valueType": "text",
            "keyLabel": "của",
            "isRequired": false,
            "isSeller": false
        }
    ]
}

Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
id	DataType: Number	ID của trường động
keyLabel	DataType: String	Tên hiển thị của trường động, 
Hiển thị trên giao diện nhập liệu khi lập hóa đơn
keyTag	DataType: String	Tên của trường động khi lưu vào dữ liệu
valueType	DataType: String
	Kiểu dữ liệu của trường động. Chỉ bao gồm các giá trị: “text”,  “date”, “number”
isRequired	DataType: Boolean	Trường có bắt buộc hay không
isSeller	DataType: Boolean	isSeller = true: Trường dữ liệu thuộc bên bán
isSeller = false: Trường dữ liệu thuộc bên mua
Gửi dữ liệu lập hóa đơn với trường động: Thêm vào mảng metadata, mỗi phần tử bao gồm các giá trị được mapping dựa vào customFields nhận từ response như sau
Trường trong
(customFields)	Tên trường
(metadata)	Kiểu dữ liệu, ràng buộc	Mô tả
id	invoiceCustomFieldId	Required : false
DataType: Number
Minlength : 
Maxlength : 10
Format : 	ID của trường động

keyTag	keyTag	Required : true
DataType: String	Tên của trường động khi lưu vào dữ liệu
valueType	valueType	Required : true
DataType: String
	Kiểu dữ liệu của trường động. Chỉ bao gồm các giá trị: “text”,  “date”, “number”
keyLabel	keyLabel	Required : true
DataType: String
	Tên hiển thị của trường động, 
Hiển thị trên giao diện nhập liệu khi lập hóa đơn
valueType = date	dateValue	Required : false
DataType: Date	Giá trị của trường dữ liệu trong trường hợp valueType = date
valueType = number	numberValue	Required : false
DataType: Number	Giá trị của trường dữ liệu trong trường hợp valueType = number
valueType = text	stringValue	Required : false
DataType: String	Giá trị của trường dữ liệu trong trường hợp valueType = text

{
   "generalInvoiceInfo": {
      "invoiceType": "03XKNB",
      "templateCode": "03XKNB0/003",
      "invoiceSeries": "AA/20E",
      "currencyCode": "VND",
      "adjustmentType": "1",
      "paymentStatus": true,
      "cusGetInvoiceRight": true
   },
   "sellerInfo": {
      "sellerLegalName": "Người bán hàng",
      "sellerTaxCode": "0100109106-712",
      "sellerAddressLine": "Thành Phố Hà Nội - Việt Nam",
      "sellerPhoneNumber": "0123456789",
      "sellerFaxNumber": "0123456789",
      "sellerEmail": "email@gmail.com",
      "sellerBankName": "Ngân hàng ",
      "sellerBankAccount": "012345678901",
      "sellerDistrictName": "",
      "sellerCityName": "Thành Phố Hà Nội",
      "sellerCountryCode": "84",
      "sellerWebsite": "sinvoice.viettel.vn"
   },
   "buyerInfo": {
      "buyerName": "Tên khách hàng",
      "buyerLegalName": "Tên đơn vị",
      "buyerTaxCode": "0100109106",
      "buyerAddressLine": "An Khánh Hoài Đức Hà Nội",
      "buyerDistrictName": "Số 9, đường 11, VSIP Bắc Ninh, Thị xã Từ Sơn, Tỉnh",
      "buyerCityName": "Thành Phố Hà Nội",
      "buyerCountryCode": "84",
      "buyerPhoneNumber": "987999999",
      "buyerFaxNumber": "0458954",
      "buyerEmail": "abc@gmail.com",
      "buyerBankName": "Ngân hàng Quân đội MB",
      "buyerBankAccount": "01578987871236547",
      "buyerIdType": "3",
      "buyerIdNo": "8888899999",
      "buyerCode": "832472343b_b",
      "buyerBirthDay": ""
   },
   "payments": [
      {
         "paymentMethodName": "Truyền trực tiếp giá trị mong muốn vào đây"
      }
   ],
     "taxBreakdowns": [
    {
      "taxPercentage": -1,
      "taxableAmount": 27286150,
      "taxAmount": 0
    }
  ],
  "itemInfo": [
    {
      "lineNumber": 1,
      "itemCode": "HH0001",
      "itemName": "Hàng hóa 01",
      "unitCode": null,
      "unitName": "Chiếc",
      "unitPrice": 150450,
      "quantity": 100,
      "selection": 1,
      "itemTotalAmountWithoutTax": 15045000,
      "taxPercentage": -1,
      "taxAmount": 0,
      "discount": null,
      "discount2": null,
      "itemDiscount": 0,
      "itemNote": null,
      "batchNo": null,
      "expDate": null,
      "isIncreaseItem": null
    },
    {
      "lineNumber": 2,
      "itemCode": "HH00002",
      "itemName": "Hàng hóa 02",
      "unitCode": null,
      "unitName": "Cái",
      "unitPrice": 244823,
      "quantity": 50,
      "selection": 1,
      "itemTotalAmountWithoutTax": 12241150,
      "taxPercentage": -1,
      "taxAmount": 0,
      "discount": null,
      "discount2": null,
      "itemDiscount": 0,
      "itemNote": null,
      "batchNo": null,
      "expDate": null,
      "isIncreaseItem": null
    }
  ],
  "metadata": [
  {
    "keyTag": "commandDes",
    "keyLabel": "về việc",
    "dateValue": null,
    "stringValue": "điều chuyển nội bộ",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "contractNo",
    "keyLabel": "Hợp đồng số",
    "dateValue": null,
    "stringValue": "Hợp đồng số",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "vehicle",
    "keyLabel": "Phương tiện vận chuyển",
    "dateValue": null,
    "stringValue": "xe tải",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "exportAt",
    "keyLabel": "Xuất tại kho",
    "dateValue": null,
    "stringValue": "Kho 1",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "importAtNo",
    "keyLabel": "Mã kho",
    "dateValue": null,
    "stringValue": "KH2",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "importAt",
    "keyLabel": "Nhập tại kho",
    "dateValue": null,
    "stringValue": "Kho 2",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "importAtNo",
    "keyLabel": "Mã kho",
    "dateValue": null,
    "stringValue": "KH0",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "vehicleNo",
    "keyLabel": "Số xe",
    "dateValue": null,
    "stringValue": "1524-jhh",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "economicContractNo",
    "keyLabel": "Căn cứ hợp đồng kinh tế số",
    "dateValue": null,
    "stringValue": "123456",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "commandDate",
    "keyLabel": "Ngày điều động",
    "dateValue": "1605752798000",
    "stringValue": null,
    "numberValue": null,
    "valueType": "date",
    "isRequired": false,
    "isSeller": false,
    "required": false
  },
  {
    "keyTag": "commandOf",
    "keyLabel": "của",
    "dateValue": null,
    "stringValue": "Công ty ABC",
    "numberValue": null,
    "valueType": "text",
    "isRequired": false,
    "isSeller": false,
    "required": false
  }
]
}


7.8	 Lập hóa đơn nháp
	Đầu vào:
Webservice dùng để lưu dữ liệu hóa đơn nháp lên hệ thống SInvoice. Các hóa đơn nháp này không có số hóa đơn hay kí số, chỉ có thể xem/phát hành trên website của SInvoice. Khi phát hành thì các số hóa đơn sẽ không được cập nhật lại phần mềm tích hợp.
-	Action (POST): InvoiceAPI/InvoiceWS/createOrUpdateInvoiceDraft/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
-	Data: Định dạng JSON
-	Thông số dữ liệu truyền vào tương tự phần Lập hóa đơn. Tham khảo json tại phần 6.2
Lưu ý:
Trong trường hợp lập hóa đơn điều chỉnh/thay thế cho hóa đơn giấy thì bổ sung thêm trong generalInvoiceInfo hai thẻ như sau: 

Tên trường	Kiểu dữ liệu	Mô tả
originalInvoiceType	Required: false
DataType: String
Minlength: N/A
Maxlength: 
Format:	Loại hóa đơn gốc
Truyền giá trị số với ý nghĩa như sau 
0- Không phải hóa đơn giấy/hóa đơn không tồn tại trên hệ thống 
1-Hóa đơn TT78 
2-Hóa đơn theo QĐ 1209 
3-Hóa đơn điện tử/giấy TT32
4-Hóa đơn giấy TT 78
originalTemplateCode	Required: 
DataType: String
Minlength: N/A
Maxlength: 20
Format:	Bắt buộc truyền nếu originalInvoiceType là 1, 2, 3 hoặc 4
Ví dụ mẫu TT32: 01GTKT0/001
Ví dụ mẫu TT78: 1/0224
Khi lập hóa đơn, hệ thống không kiểm tra tính tồn tại của hóa đơn gốc trên hệ thống, các quy tắc xác thực khác giữ nguyên hiện trạng
	Đầu ra:
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về:
	Dữ liệu về thông tin về hóa đơn nháp lập thành công
{
  "errorCode": "",
  "description": "",
  "result": {    
  }
}

Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lập hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lập hóa đơn thành công)

Lưu ý:
Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
7.9	Hủy hóa đơn
Cho phép xóa bỏ hóa đơn (chuyển hóa đơn sang trạng thái xóa bỏ) từ hệ thống tích hợp.
	Đầu vào:
-	Action (POST): InvoiceAPI/InvoiceWS/cancelTransactionInvoice
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/x-www-form-urlencoded

Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

templateCode	Required : false
DataType: String
Minlength : 
Maxlength : 20
Format : 	Mã mẫu hóa đơn
VD: 
01GTKT0/001
1/001
invoiceNo	Required : true
DataType: String
Minlength : 7
Maxlength : 35
Format :  [a-zA-Z0-9/]+	Là số hóa đơn = ký hiệu hóa đơn + số hóa đơn.
 vd : AA/20E0000001

strIssueDate	Required : true
DataType: milisecond since epoch
Minlength : 
Maxlength : 
Format: Tiêu chuẩn 5.1	Ngày phát hành hóa đơn 
(không vượt quá ngày hiện tại)

additionalReferenceDesc	Required : true
DataType: String
Minlength : 1
Maxlength : 400	Tên văn bản thỏa thuận hủy hóa đơn

additionalReferenceDate	Required : true
DataType: milisecond since epoch
Minlength : 
Maxlength :
Format: Tiêu chuẩn 5.1	Ngày thỏa thuận (không vượt quá ngày hiện tại)

reasonDelete	Required: False
DataType: String
Minlength: N/A
Maxlength: 255
Format:	Lý do hủy hóa đơn 
Cho phép nhập tối đa 255 ký tự

Form Data Vị dụ:
	Đầu ra:
 
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về:
Vị dụ trả về thành công:

{
    "errorCode": null,
    "description": "CANCEL TRANSACTION INVOICE SUCCESS"
}
	Bảng mã lỗi :
Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lấy hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lấy hóa đơn thành công),
Kiểm tra hóa đơn có phải là các hóa đơn gốc, chưa kê khai thuế, trạng thái đã thanh toán, không phải hóa đơn điều chỉnh, hóa đơn thay thế và hóa đơn điều chỉnh hủy hay không? Nếu phải trả lại thông tin hóa đơn không hợp lệ

7.10	Cập nhật kê khai thuế
Cho phép hệ thống tích hợp gửi thông tin cập nhật kê khai thuế sang, để tránh cho khách hàng bị sai sót trong quá trình sử dụng (hóa đơn đã kê khai thực tế vẫn có thể xóa bỏ, thay thế).
	Đầu vào:
-	Action (POST):  InvoiceAPI/InvoiceUtilsWS/updateTaxDeclaration/
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type: application/json
Các tham số:
Tên trường	Kiểu dữ liệu, ràng buộc	Dữ liệu/mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
strIssueDate	Required: true
DataType: String
Minlength: 
Maxlength: 
Format: dd/mm/yyyy	Ngày lập hóa đơn  

-	Vị dụ với định dạng json:
  {
		"supplierTaxCode":"0100109106",
		"strIssueDate":"14/03/2018"
		}

	Đầu ra:
Hình ảnh Response trả về thành công
 

7.11	Cung cấp tình hình sử dụng hóa đơn theo dải
Trả về thông tin chi tiết số lượng hóa đơn đã dùng, số lượng còn lại của một dải hóa đơn để từ đó đối tác tích hợp có thể chủ động cảnh báo khách hàng trong trường hợp không đủ hóa đơn.
	Đầu vào:
-	Action (POST): /InvoiceAPI/InvoiceUtilsWS/getProvidesStatusUsingInvoice
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Các tham số của đối tượng CommonDataInput
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
templateCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : 	Mã mẫu hóa đơn
Mã mẫu hóa đơn, tuân thủ theo quy định ký hiệu mẫu hóa đơn của Thông tư hướng dẫn thi hành nghị định số 51/2010/NĐ-CP
Chi tiết xem PL1 Thông tư 39/2014/TT-BTC
serial	Required : true
DataType: String
Minlength : 
Maxlength : 7
Format : [a-zA-Z0-9]*$	Seri hóa đơn


Vị dụ mẫu và các trường dữ liệu:
-	JSON:
{
	"supplierTaxCode":"0100109106-712",
	"templateCode":"01GTKT0/003",
	"serial":"AA/20E"
}
	Đầu ra:
Đối tượng Response với HTTPStatus và output  Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null không có lỗi gì xảy ra)
description	Mô tả lỗi (giá trị là null không có lỗi gì xảy ra)
statuss	Trạng thái (giá trị là 200 lấy thông tin sử dụng hóa đơn thành công)
numOfpublishInv	Tổng số hóa đơn đã phát hành
totalInv	Tổng số hóa đơn có thể lập với mẫu hóa đơn + dải truyển vào

7.12	Lập hóa đơn theo lô
*Quy tắc kiểm tra ngày lập hóa đơn:
Hệ thống Hóa đơn điện tử SInvoice V2, phần Cấu hình chung liên quan ngày lập hóa đơn có 2 checkbox: Cho phép ngày lập hóa đơn khác ngày hiện tại, Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất.
Khi phát hành hóa đơn qua API, ngày lập hóa đơn sẽ bị ảnh hưởng khi người dùng tích chọn các checkbox này, xảy ra 4 trường hợp như mô tả sau:
TH1: Không tick cả 2
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: ngày lập không hợp lệ
- Ngày lập > ngày hiện tại: lấy ngày truyền vào (không kiểm tra giờ)
TH2: Tick “Cấu hình ngày ký là thời điểm hiện tại”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH3: Tick “Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH4: Tích cả 2 
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại:  lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ 
- Trường hợp khách hàng muốn lập hóa đơn theo lô sẽ sử dụng hàm sau. Lưu ý chỉ sử dụng cho loại chứng thư số server (HSM)
Lưu ý: 
-	Hệ thống đang cho phép tối đa 50 hóa đơn/1 lô do thời gian xử lý đơn lẻ từng hóa đơn lâu, nếu như để lô nhiều quá có thể bị timeout. Trong trường hợp dữ liệu từ hệ thống tích hợp nhiều hơn, có thể tự động chia nhỏ số lượng hóa đơn và gửi sang.
-	Chỉ lập các hóa đơn gốc theo lô
-	Nếu là lập hóa đơn máy tính tiền thì respond trả về có cả thông tin Mã CQT cấp: "codeOfTax", nếu không phải hóa đơn máy tính tiền thì trả về “codeOfTax” = null
-	Nếu cấu hình Không ký hóa đơn có mã khởi tạo từ máy tính tiền và hóa đơn thuộc loại máy tính tiền thì cho phép doanh nghiệp dùng chữ ký USB Token và CloudCA lập hóa đơn theo lô bằng API Server.
-	Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
	Đầu vào:
-	Action (POST): InvoiceAPI/InvoiceWS/createBatchInvoice/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

-	Data: Dữ liệu mẫu lập hóa đơn theo lô
	JSON
Lập hóa đơn theo lô	 

Kết quả khi lập hóa đơn theo lô thành công sẽ trả kết quả về theo transactionUuid để xác định được hóa đơn nào thành công, sinh ra số hóa đơn nào.
	Đầu ra:
Tên trường	Mô tả
createInvoiceOutputs	Kết quả trả về khi hóa đơn được lập thành công ( trả số hóa đơn )
lstMapError	Mô tả lỗi (các lỗi gặp phải của ds hóa đơn)
totalSuccess	Tổng số dòng tạo hóa đơn thành công
totalFail	Tổng số hóa đơn bị lỗi chưa phát hành thành công

Ví dụ về kết quả trả về:
 
Lỗi về sai, thiếu  thông tin 
 




Các lỗi về định dạng json và token sẽ trả về theo định dạng
 
7.13	Cung cấp danh sách hóa đơn theo khoảng thời gian
Trả về chi tiết thông tin các hóa đơn để có thể đối soát xem sai đúng của hóa đơn trong một khoảng thời gian.

	Đầu vào:
-	Action (POST): /InvoiceAPI/InvoiceUtilsWS/getListInvoiceDataControl
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json
Các tham số của đối tượng CommonDataInput
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
 
fromDate	Required : true
DataType: String
Format : dd/MM/yyyy	Ngày bắt đầu muốn tìm kiếm 

toDate	Required : true
DataType: String
Format : dd/MM/yyyy	Ngày kết thúc muốn tìm kiếm

originalInvoiceID	DataType: String
	-	Là ký hiệu hóa đơn + số hóa đơn vd : AA/20E0000001
-	Chỉ lấy khi hoá đơn có adjustmentType:
3: Hóa đơn thay thế 
      5: Hóa đơn điều chỉnh 
adjustmentType	Required: false
DataType: String
Minlength: 
Maxlength: 1
Format:	Trạng thái điều chỉnh hóa đơn: 
1: Hóa đơn gốc (hóa đơn đã phát hành, hóa đơn bị điều chỉnh, hóa đơn bị thay thế)
3: Hóa đơn thay thế 
5: Hóa đơn điều chỉnh thông tin
7: Hóa đơn xóa bỏ
9: Hóa đơn điều chỉnh tiền
Không truyền sẽ trả tất cả
Vị dụ mẫu và các trường dữ liệu:
-	JSON:
{	"supplierTaxCode":"0100109106",
	"fromDate":"10/03/2018",
	"toDate":"16/03/2018"
       "adjustmentType":3
}
	Đầu ra:
Đối tượng Response với HTTPStatus và output  Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null không có lỗi gì xảy ra)
description	Mô tả lỗi (giá trị là null không có lỗi gì xảy ra)
lstInvoiceBO	Danh sách hóa đơn được tạo theo thời gian được truyền vào
Lưu ý adjustmentTyp của hóa đơn trả về :
Tên trường	Mô tả
adjustmentType	Loại hóa đơn: 
1: Hóa đơn gốc 
3: Hóa đơn thay thế 
5: Hóa đơn điều chỉnh thông tin
7: Hóa đơn xóa bỏ
9: Hóa đơn điều chỉnh tiền
{
    "errorCode": null,
    "description": null,
    "totalRows": 8162,
    "invoices": [
        {
            "invoiceId": 16376495,
            "invoiceType": "1",
            "adjustmentType": "1",
            "templateCode": "1/011",
            "invoiceSeri": "K22TXK",
            "invoiceNumber": "0037294",
            "invoiceNo": "K22TXK37294",
            "currency": "VND",
            "total": 13627273.000000000,
            "issueDate": 1663204962000,
            "issueDateStr": null,
            "state": 1,
            "requestDate": null,
            "description": null,
            "buyerIdNo": "",
            "stateCode": 1,
            "subscriberNumber": null,
            "paymentStatus": 1,
            "viewStatus": null,
            "downloadStatus": null,
            "exchangeStatus": 0,
            "numOfExchange": null,
            "createTime": 1663204962000,
            "contractId": null,
            "contractNo": null,
            "supplierTaxCode": "0100109106-509",
            "buyerTaxCode": "",
            "totalBeforeTax": 13627273.000000000,
            "taxAmount": 0E-9,
            "taxRate": null,
            "paymentMethod": "5",
            "paymentTime": null,
            "customerId": null,
            "no": null,
            "paymentStatusName": "Đã thanh toán",
            "buyerName": "Nguyễn văn A",
            "transactionUuid": "E8AE136CEF1272AAE05324011E0A9838"
             "originalInvoiceId": "K22THY32"
        }
    ]
}

7.14	Gửi email hoá đơn cho khách hàng
- Trong trường hợp khách hàng đã cấu hình email server và biểu mẫu email trên hệ thống SInvoice, hệ thống sẽ tự động thực hiện gửi email cho người mua khi trong thông tin hóa đơn có email. API này cho phép phần mềm tích hợp chủ động việc gửi email cho khách hàng, trong trường hợp cấu hình của email là không hoạt động hoặc muốn gửi lại email cho khách hàng khi có yêu cầu.
- API này có kiểm tra cấu hình gửi email các loại hóa đơn
- Chú ý: 
+ Bổ sung đường link tra cứu hóa đơn theo mã bí mật trong email hóa đơn gửi cho người mua.
+ Trường hợp dữ liệu hợp lệ, hệ thống gửi email hóa đơn cho người mua theo biểu mẫu đã cấu hình, thay thế các thông tin trong dấu {} bằng thông tin của hóa đơn/người bán như hiện tại, bổ sung thêm đường link tra cứu hóa đơn theo mã bí mật tại tham số {link-invoice-search}.
	Đầu vào:
-	Action (POST): /InvoiceAPI/InvoiceUtilsWS/sendHtmlMailProcess
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
•	Các tham số sendHtmlMailProcess
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

lstTransactionUuid	Required : true
DataType: String	Danh sách key request, mỗi transactionUuid tương ứng với 1 hoá đơn (Validate độ dài transactionUuid trong khoảng 10 – 36 ký tự). Các transactionUuid cách nhau bởi dấu “,”

Vị dụ mẫu và các trường dữ liệu:
-	JSON:
{
	"supplierTaxCode":"0100109106-712s",
	"lstTransactionUuid":"idtest9999999999,testuuid8888888,transactionUuid123"
}

	Đầu ra:
Đối tượng Response với HTTPStatus và output Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null không có lỗi gì xảy ra)
description	Mô tả lỗi (giá trị là null không có lỗi gì xảy ra)

7.15	Phát hành/thay thế/điều chỉnh cho USB-TOKEN (Bước 1: Lấy chuỗi hash)
*Quy tắc kiểm tra ngày lập hóa đơn:
Hệ thống Hóa đơn điện tử SInvoice V2, phần Cấu hình chung liên quan ngày lập hóa đơn có 2 checkbox: Cho phép ngày lập hóa đơn khác ngày hiện tại, Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất.
Khi phát hành hóa đơn qua API, ngày lập hóa đơn sẽ bị ảnh hưởng khi người dùng tích chọn các checkbox này, xảy ra 4 trường hợp như mô tả sau:
TH1: Không tick cả 2
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: ngày lập không hợp lệ
- Ngày lập > ngày hiện tại: lấy ngày truyền vào (không kiểm tra giờ)
TH2: Tick “Cấu hình ngày ký là thời điểm hiện tại”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH3: Tick “Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH4: Tích cả 2 
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại:  lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
- Sinh ra file xml và chuỗi hash của file XML của hóa đơn ký bởi USB Token.
	Đầuvào:
-	Action (POST):  InvoiceAPI/InvoiceWS/createInvoiceUsbTokenGetHash/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Đầu vào tương tư như lập hóa đơn, bổ sung thêm thông tin chứng thư gửi kèm.
Bổ sung trường Lý do sai sót hoá đơn. Điều chỉnh cho phép truyền dấu âm số lượng/ đơn giá
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
certificateSerial	Required : true
DataType: String
Minlength :  
Maxlength : 100
Format : 	Serial Number của chứng thư số của doanh nghiệp, chứng thư số này đã được doanh nghiệp đẩy lên trên hệ thống khi đăng ký sử dụng USB Token.
Định dạng Hex.
Vị dụ: 5404FFFEB7033FB316D672201B7BA4FE
adjustedNote	Required: False
DataType: String
Minlength: N/A
Maxlength: 255
Format:	Lý do sai sót 
Cho phép nhập chuỗi ký tự tối đa 255 ký tự. 
Không bắt buộc truyền.
Đặt trong generalInvoiceInfo
unitPrice	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+-	Đơn giá của hàng hóa. 
Các quy tắc ràng buộc giữ nguyên hiện trạng. 
Bổ sung cho phép truyền giá trị âm


quantity	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+-	Số lượng của hàng hóa 
Các quy tắc ràng buộc giữ nguyên hiện trạng. 
Bổ sung cho phép truyền giá trị âm



originalInvoiceType	Required: True
DataType: String
Minlength: N/A
Maxlength: 
Format:	Loại hóa đơn gốc
Truyền giá trị số với ý nghĩa như sau 
0- Không phải hóa đơn giấy/hóa đơn không tồn tại trên hệ thống 
1-Hóa đơn TT78 
2-Hóa đơn theo QĐ 1209 
3-Hóa đơn điện tử/giấy TT32
4-Hóa đơn giấy TT 78
Chú ý: 
- Trường hợp thẻ originalInvoiceType không truyền hoặc truyền giá trị rỗng/0 thì không bắt buộc truyền thẻ originalTemplateCode, hệ thống xác thực thông tin khi lập hóa đơn như hiện trạng. 
- Trường hợp thẻ originalInvoiceType truyền giá trị 1, 2, 3 hoặc 4 thì 
+ Bắt buộc phải truyền thẻ originalTemplateCode, quy tắc xác thực thẻ này tương tự như thẻ templateCode hiện tại. 
+ Khi lập hóa đơn, hệ thống không kiểm tra tính tồn tại của hóa đơn gốc trên hệ thống, các quy tắc xác thực khác giữ nguyên hiện trạng
originalTemplateCode	Required: 
DataType: String
Minlength: N/A
Maxlength: 20
Format:	Bắt buộc truyền nếu originalInvoiceType là 1, 2, 3 hoặc 4
Ví dụ mẫu TT32: 01GTKT0/001
Ví dụ mẫu TT78: 1/0224

{
   "generalInvoiceInfo":{
      "invoiceType":"01GTKT",
      "templateCode":"01GTKT0/170",
	"invoiceSeries":"AA/17E",
      "transactionUuid": "123e4567-e89b-12d3-a456-426655440000",
      "invoiceIssuedDate":1587797116843,
      "currencyCode":"VND",
      "adjustmentType":"1",
      "adjustedNote":"",
      "originalInvoiceType": "1",
      "originalTemolateCode": "1/0224",
      "paymentStatus":true,
      "paymentType":"TM",
      "paymentTypeName":"TM",
      "cusGetInvoiceRight":true,
      "userName":"user 1",
      “certificateSerial”:”5404FFFEB7033FB316D672201B7BA4FE”
   },
   "buyerInfo":{
      "buyerName":"Đặng thị thanh tâm",
      "buyerLegalName":"",
      "buyerTaxCode":"",
      "buyerAddressLine":"HN VN",
      "buyerPhoneNumber":"11111",
      "buyerEmail":"",
      "buyerIdNo":"123456789",
      "buyerIdType":"1"
   },
   "sellerInfo":{
      "sellerLegalName":"Đặng thị thanh tâm",
      "sellerTaxCode":"0100109106-501",
      "sellerAddressLine":"test",
      "sellerPhoneNumber":"0123456789",
      "sellerEmail":"PerformanceTest1@viettel.com.vn",
      "sellerBankName":"vtbank",
      "sellerBankAccount":"23423424"
   },
   "extAttribute":[

   ],
   "payments":[
      {
         "paymentMethodName":"TM"
      }
   ],
   "deliveryInfo":{

   },
   "itemInfo":[
      {
         "lineNumber":1,
         "itemCode":"ENGLISH_COURSE",
         "itemName":"Khóa học tiếng anh",
         "unitName":"khóa học",
         "unitPrice":"-3500000.0",
         "quantity":"-10.0",
         "itemTotalAmountWithoutTax":35000000,
         "taxPercentage":10.0,
         "taxAmount":0.0,
         "discount":0.0,
         "itemDiscount":150000.0
      }
   ],
   "discountItemInfo":[

   ],
"metadata":[

   ],

  "meterReading": [{
            "previousIndex": "5454",
            "currentIndex": "244",
            "factor": "22",
            "amount": "2"
          },
          {
            "previousIndex": "44",
            "currentIndex": "44",
            "factor": "33",
            "amount": "3"
          }],
   "summarizeInfo":{
      "sumOfTotalLineAmountWithoutTax":35000000,
      "totalAmountWithoutTax":35000000,
      "totalTaxAmount":3500000.0,
      "totalAmountWithTax":38500000,
      "totalAmountWithTaxInWords":"Ba mươi tám triệu năm trăm nghìn đồng chẵn",
      "discountAmount":0.0,
      "settlementDiscountAmount":0.0,
      "taxPercentage":10.0,
      "extraName": "{ Tiền phí đặc biệt, Tiền phí,  } ",
      "extraValue": "{ 00 ,00,}"
   },
   "taxBreakdowns":[
      {
         "taxPercentage":10.0,
         "taxableAmount":35000000,
         "taxAmount":3500000.0
      }
   ]
}
	Dữ liệu chuỗi Hash trả về
{
  "errorCode": "",
  "description": "",
  "result": {
    "hashString": 0HFm34vX525V3Syg5EwdTnfO21s=,  }
}

Ví dụ response trường hợp truyền sai giá trị originalInvoiceType
{
    "code": 400,
    "message": "BAD_REQUEST_ORIGINAL_INVOICE_TYPE_INVALID",
    "data": "BAD_REQUEST_ORIGINAL_INVOICE_TYPE_INVALID"
}
Lưu ý: 
1.	Dữ liệu hóa đơn gốc lưu vào cột instance_file_name trong bảng invoice như sau: 
Loại hóa đơn | Mẫu hóa đơn | Ký hiệu hóa đơn | Số hóa đơn
trong đó:
- Loại hóa đơn là giá trị thẻ originalInvoiceType 
- Mẫu hóa đơn là giá trị thẻ originalTemplateCode 
2.	Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
Output:
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
errorCode	DataType: String	Mã lỗi nếu có, không có lỗi thì trả về null
description	DataType: String	Mô tả chi tiết lỗi
hashString	DataType: String	Chuỗi Hash trả về của hóa đơn, dạng Base64

7.16	Phát hành/thay thế/điều chỉnh cho USB-TOKEN (Bước 2: Ký USB token và sinh hóa đơn)
- Thực hiện sử dụng USB-TOKEN để ký chuỗi hashString nhận được từ API trong bước 7.15. Lấy chuỗi ký để sinh hóa đơn.
	Đầuvào:
-	Action (POST):  InvoiceAPI/InvoiceWS/createInvoiceUsbTokenInsertSignature
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength :  
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

templateCode	Required : true
DataType: String
Minlength : 
Maxlength : 20	Mã mẫu hóa đơn. 

hashString	Required : true
DataType: String	Chuỗi Hash mà dữ liệu trả về ở trong request getHash phía bên trên
= out put của API : 7.15 Lập hóa đơn ký USB Token (Bước 1: Lấy chuỗi hash)
signature	Required : true
DataType: String	Chữ ký sau khi hashString đã được ký bởi USB token. dạng Base64
Vị dụ Json
{
  "supplierTaxCode": "0100109106-712",
  "templateCode": "01GTKT0/002",
  "hashString": "0HFm34vX525V3Syg5EwdTnfO21s=",
  "signature": "U0WpJk2Q/rDsnZDz8hiWKvs6QEf5DHTG8JyXjjNMtggZ/MIDP0hn9Mutc2uPZEOxqk2YnMjuRSxU8ST/T+C5i46Vb/0+7uIfzKpPm2yrsOSivCdzr6FrY6nJPkfkOWEdEs/hqDzcf4Vn8ZCVkNfovYR4prPGc7kNpO21sNb9BAI="
}
Kết quả trả về
	Dữ liệu về thông tin về hóa đơn đã lập0
{
  "errorCode": "",
  "description": "",
  "result": {
    "supplierTaxCode": 0100109106-712,
    "invoiceNo": AA/20E0000018,
    "transactionID": 12523522245,
    "reservationCode": AXHBNK8I0H
  }
}


Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lập hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lập hóa đơn thành công)
supplierTaxCode	Mã số thuế người bán (doanh nghiệp phát hành hóa đơn)
invoiceNo	Số hóa đơn vd: AA\20E0000001 
transactionID	Id của giao dịch
reservationCode	Mã số bí mật dùng để khách hàng tra cứu
Tham khảo thêm tại https://sinvoice.viettel.vn/download/soft/signhash.rar
Lưu ý: Nếu là lập hóa đơn máy tính tiền thì respond trả về có cả thông tin Mã CQT cấp: "codeOfTax", nếu không phải hóa đơn máy tính tiền thì trả về codeOfTax = null
VD mẫu output
{
    "errorCode": null,
    "description": null,
    "result": {
        "supplierTaxCode": "0100109106-710",
        "invoiceNo": "C23MHY3",
        "transactionID": "168378907853232661",
        "reservationCode": "2QTBFEMAXFWZO5B",
        "codeOfTax": "M1-23-34567-00000000201"
    }
}
7.17	Chuyển font
Hỗ trợ convert từ các font chữ sang unicode (KH sử dụng API) này kết hợp với API tạo hóa đơn để convert dữ liệu
	Đầuvào:
-	Action (POST):  InvoiceAPI/InvoiceUtilsWS/convertFont
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
font	Required : true
DataType: String	Font dữ liệu, các dữ liệu hỗ trợ bao gồm:
VNI
TCVN3
TCVN1
data	Required : true
DataType: String	Dữ liệu cần chuyển 
Vị dụ json:
{
  "font": "TCVN3",
  "data": "D÷ liÖu kh«ng ®óng chuÈn Unicode cÇn convert"
}
Kết quả trả về
{
    "errorCode": null,
    "description": null,
    "result": "Dữ liệu không đúng chuẩn Unicode cần convert"
}

 


Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu chuyển font thành công)
description	Mô tả lỗi (giá trị là null nếu chuyển font thành công)
result	Dữ liệu sau khi được chuyển về chuẩn Unicode
7.18	Cập nhật trạng thái thanh toán
Cho phép hệ thống tích hợp cập nhật trạng thái thanh toán của hóa đơn sang là đã thanh toán.
	Đầu vào:
-	Action (POST):  InvoiceAPI/InvoiceWS/updatePaymentStatus
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/x-www-form-urlencoded
-	Data: dữ liệu truyền vào dạng Form Param gồm các tham số:

Tên trường	
Kiểu dữ liệu, ràng buộc	
Dữ liệu/mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

templateCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format:  	Mẫu số hóa đơn


invoiceNo	Required: true
DataType: String
Minlength: 7
Maxlength: 35
Format:  [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + số hóa đơn vd: AA/20E0000001



buyerEmailAddress	Required: false
DataType: String
Minlength: 
Maxlength: 2000
Format: ^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$	Email người mua





strIssueDate	Required: false
DataType: milisecond
Minlength: 
Maxlength: 
Format: Tiêu chuẩn 5.1	Ngày lập hóa đơn  



paymentType	Required: false
DataType: String
Minlength: 
Maxlength: 
Format: 	Loại hình thức thanh toán 

 

paymentTypeName	Required: false
DataType: String
Minlength: 
Maxlength: 
Format:	Tên phương thức thanh toán


 
cusGetInvoiceRight	Required: false
DataType: Boolean
Minlength: 
Maxlength: 
Format: true/false	Cho khách hàng xem hóa đơn trong Quản lý hóa đơn





	Vị dụ định dạng FormParam
 
Dữ liệu trả về
{"errorCode":null,"description":null,"result":true,"paymentTime":null,"paymentMethod":null}
Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu cập nhật trạng thái thanh toán thành công)
description	Mô tả lỗi (giá trị là null nếu cập nhật trạng thái thanh toán thành công)
result	Kết quả cập nhật trạng thái thanh toán 
Thành công: true
Không thành công: false
paymentTime	Thời gian cập nhật trạng thái thanh toán
paymentMethod	Phương thức thanh toán
7.19	Hủy trạng thái thanh toán
Cho phép chuyển trạng thái thanh toán của hóa đơn sang chưa thanh toán.
	Đầu vào:
-	Action (POST):  InvoiceAPI/InvoiceWS/cancelPaymentStatus
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/x-www-form-urlencoded

Tên trường	Kiểu dữ liệu, ràng buộc	Dữ liệu/mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
invoiceNo	Required : true
DataType: String
Minlength : 7
Maxlength : 35
Format :  [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + số hóa đơn vd : AA/20E0000001
strIssueDate	Required : true
DataType: 
Minlength : 
Maxlength : 
Format:Tiêu chuẩn 5.1	Ngày lập hóa đơn 

	Vị dụ định dạng FormParam
supplierTaxCode=0100109106-712&invoiceNo=AA%2F20E0000002&strIssueDate=1600154781000
	Dữ liệu trả về
{
    "errorCode": null,
    "description": "Success"
}

 
7.20	Xem trước hóa đơn nháp
	Đầu vào:
Webservice dùng để lấy file PDF của dữ liệu để xem. Hệ thống tích hợp đẩy dữ liệu lập hóa đơn sang và SInvoice trả về file PDF của dữ liệu đó, các dữ liệu sẽ không được lưu vào trong SInvoice.
-	Action (POST):  InvoiceAPI/InvoiceUtilsWS/createInvoiceDraftPreview/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 

Tên trường	
Kiểu dữ liệu, ràng buộc	
Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001

-	Data: Định dạng JSON
-	Thông số dữ liệu truyền vào tương tự phần Lập hóa đơn. Tham khảo json tại phần 6.2


Lưu ý:
Trong trường hợp lập hóa đơn điều chỉnh/thay thế cho hóa đơn giấy thì bổ sung thêm trong generalInvoiceInfo hai thẻ như sau: 
Tên trường	Kiểu dữ liệu	Mô tả
originalInvoiceType	Required: false
DataType: String
Minlength: N/A
Maxlength: 
Format:	Loại hóa đơn gốc
Truyền giá trị số với ý nghĩa như sau 
0- Không phải hóa đơn giấy/hóa đơn không tồn tại trên hệ thống 
1-Hóa đơn TT78 
2-Hóa đơn theo QĐ 1209 
3-Hóa đơn điện tử/giấy TT32
4-Hóa đơn giấy TT 78
originalTemplateCode	Required: 
DataType: String
Minlength: N/A
Maxlength: 20
Format:	Bắt buộc truyền nếu originalInvoiceType là 1, 2, 3 hoặc 4
Ví dụ mẫu TT32: 01GTKT0/001
Ví dụ mẫu TT78: 1/0224
Khi lập hóa đơn, hệ thống không kiểm tra tính tồn tại của hóa đơn gốc trên hệ thống, các quy tắc xác thực khác giữ nguyên hiện trạng
	Đầu ra:
-	Đối tượng Response với HTTPStatus và output Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null không có lỗi gì xảy ra)
description	Mô tả lỗi (giá trị là null không có lỗi gì xảy ra)
fileName	Tên file tải về
fileToBytes	Nội dung file được chuyển thành kiểu byte, dạng base64
Lưu ý:
Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
7.21	Tra cứu hóa đơn bằng transactionUuid
Cho phép hệ thống tích hợp tra cứu hóa đơn đã được phát hành thành công dựa vào transactionUuid (Dữ liệu xác định tính duy nhất của 1 hóa đơn do bên phần mềm tích hợp sinh dữ liệu và kiểm soát)
Thường sử dụng API này khi cần đối soát dữ liệu giữa 2 hệ thống HDDT và phần mềm tích hợp.
	Đầu vào:
-	Action (POST):  InvoiceAPI/InvoiceWS/searchInvoiceByTransactionUuid
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/x-www-form-urlencoded
Tên trường	Kiểu dữ liệu, ràng buộc	Dữ liệu/mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001


transactionUuid	Required: true
DataType: String
Minlength: 10
Maxlength: 36
Format: 	Giá trị transactionUuid gán với hóa đơn khi gửi dữ liệu lập hóa đơn. 



Ví dụ với định dạng formParam:
 Hình ảnh Response trả về thành công
 
Thông tin chi tiết Response
{ 
   "transactionUuid": "0100109106_test3_268_1",
   "errorCode": null,
   "description": null,
   "result": [ 
      { 
         "supplierTaxCode": "0100109106",
         "invoiceNo": "AB/19E0000522",
         "reservationCode": "OKMYMDX5F4",
         "issueDate": 1587797116843
         "status": "Hóa đơn gốc"
      }
   ]
}
Đối với các hóa đơn theo Thông tư 78 đã được cơ quan thuế cấp mã sẽ có các thông tin bổ sung về mã cơ quan thuế như sau
STT	Tên thẻ	Ý nghĩa
1.		exchangeStatus	Mô tả trạng thái truyền nhận của HĐ với CQT
2.		exchangeDes	Mô tả lỗi truyền nhận 
3.		codeOfTax	Mã CQT cấp
{
    "errorCode": null,
    "description": null,
    "transactionUuid": "4543Gfd565h",
    "result": [
        {
            "supplierTaxCode": "0100109106-710",
            "invoiceNo": "K21DTT4",
            "reservationCode": "UFODH7MN7LT0GW5",
            "issueDate": 1638852198000,
            "status": "Hóa đơn điều chỉnh tiền",
            "exchangeStatus": " Mã CQT cấp: 00BDD6525B75646655B654665B65466565",
            "exchangeDes": null,
            "codeOfTax": "00BDD6525B75646655B654665B65466565"
        }
    ]
}
7.22 Cấp mã bí mật
- Cho phép API cấp mã bí mật cho doanh nghiệp theo MST.
- Đường dẫn API: InvoiceAPI/BotWS/getReservationCode/{taxCode}
- Method: POST



Input: 
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
transactionUuid	Required: false
DataType: String
Minlength: 10
Maxlength: 36
Format:	ID để kiểm trùng giao dịch. 
Khuyến cáo: sử dụng UUID v4.
requestCode	Required: true
DataType: BigDecimal
Minlength: 
Maxlength: 
Format:	Số lượng mã yêu cầu
Maxlength = 30,000 – Số lượng lấy mã mà chưa sử dụng
expiredDate	Required: false
DataType: Date
Minlength: 
Maxlength: 
Format:	Ngày hết hạn sử dụng mã
Định dạng theo Tiêu chuẩn 5.1, đến giờ, phút, giây
Ví dụ: 1587797116000

Ví dụ: 
{
  "transactionUuid": "56432347787",
  "expiredDate": 1587797116000,
  "requestCode": 50  
}
Output: 
Tên trường	Mô tả
transactionUuid	transactionUuid đã truyền trong Input
expiredDate	Ngày hết hạn sử dụng mã đã truyền trong Input
reservationCode	Danh sách mã bí mật cấp cho MST 



Ví dụ: 
{
  "transactionUuid": "56432347787",
  "expiredDate": 1587797116000
  "result": 
  {
  "reservationCode": ["479765676", "867547567"]
}
}
7.23	Cập nhật trạng thái in hoá đơn
- Mô tả chung: Thêm mới API cập nhật trạng thái in của hóa đơn đã phát hành.
- Đường dẫn API: InvoiceAPI/InvoiceUtilsWS/updateInvoicePrintStatus
- Method: PUT
- Phạm vi: NA
Input: 
Tên trường	Kiểu dữ liệu	Mô tả
taxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. 
Ví dụ:
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
templateCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: 	Mã mẫu hóa đơn
Ví dụ: 
Hóa đơn TT32: 01GTKT0/001
Hóa đơn TT78: 1/001
invoiceNo	Required: true
DataType: String
Minlength: 7
Maxlength: 35
Format: [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + Số hóa đơn 
Ví dụ: 
Hóa đơn TT32: AA/20E0000001
Hóa đơn TT78: K22THY12
printStatus	Required: true
DataType: int(3)
Minlength: 
Maxlength: 1
Format: 	Trạng thái in của hóa đơn
1-in 
0-chưa in
Output: 
Ví dụ trường hợp thành công:
{
    "code": 200,
    "message": "SUCCESS_UPDATE_PRINT_STATUS",
    "data": "Cập nhật trạng thái in thành công"
}
Ví dụ trường hợp lỗi:
{
    "code": 400,
    "message": "INVOICE_NOT_FOUND",
    "data": "Hóa đơn không tồn tại"
}

7.24 Số lần quét QRcode của hoá đơn
- Mô tả chung: Thêm mới API cập nhật số lần quét QRCODE của hóa đơn đã phát hành.
- Đường dẫn API: InvoiceAPI/InvoiceUtilsWS/updateInvoiceScanQrcode
- Method: PUT
- Phạm vi: NA
Input: 
Tên trường	Kiểu dữ liệu	Mô tả
taxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. 
Ví dụ:
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
templateCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: 	Mã mẫu hóa đơn
Ví dụ: 
Hóa đơn TT32: 01GTKT0/001
Hóa đơn TT78: 1/001
invoiceNo	Required: true
DataType: String
Minlength: 7
Maxlength: 35
Format: [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + Số hóa đơn 
Ví dụ: 
Hóa đơn TT32: AA/20E0000001
Hóa đơn TT78: K22THY12

Output: 
Ví dụ trường hợp thành công:
{
    "code": 200,
    "message": "SUCCESS_UPDATE_SCAN_QRCODE",
    "data": "Cập nhật quét QRCODE thành công",
    "remainScan": 5
}
Ví dụ trường hợp lỗi:
{
    "code": 400,
    "message": "INVOICE_NOT_FOUND",
    "data": "Hóa đơn không tồn tại"
}
7.25 Thống kê hóa đơn theo user
- Mô tả chung: Yêu này thêm mới API thống kê hóa đơn.
- Đường dẫn API: Action (GET): InvoiceAPI/InvoiceWS/getInvoiceUsage
- Phạm vi: Tất cả các loại hóa đơn

-	Headers:
 + Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
 + Content-Type: application/json
Input: 
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 
Format: 	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn.
issueDateFrom	Required: true
DataType: DateTime
Minlength: 
Maxlength: 
Format:	Thời gian phát hành hóa đơn từ ngày
Định dạng milliseconds

issueDateTo	Required: true
DataType: DateTime
Minlength: 
Maxlength: 
Format:	Thời gian phát hành hóa đơn đến ngày
Định dạng milliseconds
createdUser	Required: true
DataType: String
Minlength: 
Maxlength: 
Format:	Người tạo hóa đơn 
(Truyền username)
deletedStatus	Required: false
DataType: Integer
Minlength: 
Maxlength: 
Format:	Trạng thái hủy của hóa đơn, gồm: 
0-Chưa hủy 
1-Đã hủy
templateCode	Required: false
DataType: String
Minlength: 
Maxlength: 
Format:	Mã mẫu hóa đơn 
Ví dụ với TT32: 01GTKT0/001
Ví dụ với TT78: 1/0234
invoiceSeri	Required: false
DataType: String
Minlength: 
Maxlength: 25
Format:	Ký hiệu hóa đơn
Ví dụ: K22THY, AB/22E
itemName	Required: false
DataType: String
Minlength: 
Maxlength: 
Format:	Tên hàng hóa dịch vụ 
itemCode	Required: false
DataType: String
Minlength: 
Maxlength: 
Format:	Mã hàng hóa dịch vụ
totalAmountWithVat	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format:	Tổng tiền sau thuế của hóa đơn
scanStatus	Required: false
DataType: Integer
Minlength: 
Maxlength: 
Format:	Trạng thái quét QrCode của hóa đơn, gồm:
1-Chưa quét
2-Đã quét
3-Hết lượt
4-Còn lượt

Output: 
Ví dụ trường hợp thành công
{
  "errorCode": "",
  "description": "",
  "result": {
    "totalDeletedInvoice": 5,
    "totalNotDeletedInvoice": 50,
    "totalScanInvoice": 10,
    "totalNotScanInvoice": 5,
    "totalOutOfScanInvoice": 5,
    "totalRemainScanInvoice": 20,
    "totalAmountDeleted": 5000000,
    "totalAmountNotDeleted": 700000000
  }
}
Ví dụ trường hợp lỗi 
{
    "code": 400,
    "message": "FROM_BIGGER_DAY_TO_DAY",
    "data": "Từ ngày không được lớn hơn đến ngày"
}
7.26 Giải trình 
- Mô tả chung: Yêu cầu này thực hiện thêm mới API cho phép người dùng giải trình thông tin cho hóa đơn đã phát hành.
- Method: PUT
- Đường dẫn API: InvoiceWS/update-explanation
- Phạm vi: Chỉ áp dụng với hóa đơn theo TT78, hóa đơn có trạng thái khác Hủy.
Input: 
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format 	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. 
templateCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: 	Mã mẫu hóa đơn
VD: 
01GTKT0/001
1/001
invoiceNo	Required: true
DataType: String
Minlength: 
Maxlength: 35
Format:	Là ký hiệu hóa đơn ghép với số hóa đơn 
VD: AA/20E0000001 hoặc K22THY112

strIssueDate	Required: true
DataType: milisecond
Minlength: 
Maxlength: 
Format: Tiêu chuẩn 5.1	Ngày lập hóa đơn 

reason	Required: False
DataType: String
Minlength: 
Maxlength: 255
Format:	Nội dung giải trình của hóa đơn 
Cho phép nhập tối đa 255 ký tự
Ví dụ: 
{
    "supplierTaxCode": "0100109106-710",
    "templateCode": "5/036",
    "invoiceNo": "C22MTY1",
    "strIssueDate": 1666084951000,
    "reason": "ok"
}
Output: 
Tên trường	Mô tả
errorCode	NULL trong trường hợp giải trình thành công
description	Thông báo trong trường hợp giải trình thành công
code	Mã lỗi (trong trường hợp lỗi)
message	Mã lỗi (trong trường hợp lỗi)
data	Mô tả lỗi (trong trường hợp lỗi)
Ví dụ trường hợp thành công: 
{
    "errorCode": null,
    "description": "SUCCESSFUL INVOICE EXPLANATION!"
}
Ví dụ trường hợp lỗi: 
{
    "code": 400,
    "message": "INVOICE_STATUS_INVALID",
    "data": "Trạng thái hóa đơn không hợp lệ"
}

Ví dụ: 
{
    "taxCode": "0100109106-710",
    "invoiceType": "5"
}
Output: 
STT	Tên trường	Mô tả
1.		errorcode	Mã lỗi
2.		description	Mô tả lỗi
3.		totalRows	Tổng số dòng kết quả tìm được
4.		template	NA
5.		templateCode	Mẫu hóa đơn
6.		invoiceSeri	Ký hiệu hóa đơn
7.		originalTemplateCode	Mẫu hóa đơn gốc
7.27 Phát hành hóa đơn có mã bí mật cho CTS SERVER
* Quy tắc kiểm tra ngày lập hóa đơn:
Hệ thống Hóa đơn điện tử SInvoice V2, phần Cấu hình chung liên quan ngày lập hóa đơn có 2 checkbox: Cho phép ngày lập hóa đơn khác ngày hiện tại, Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất.
Khi phát hành hóa đơn qua API, ngày lập hóa đơn sẽ bị ảnh hưởng khi người dùng tích chọn các checkbox này, xảy ra 4 trường hợp như mô tả sau:
TH1: Không tick cả 2
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: ngày lập không hợp lệ
- Ngày lập > ngày hiện tại: lấy ngày truyền vào (không kiểm tra giờ)
TH2: Tick “Cấu hình ngày ký là thời điểm hiện tại”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH3: Tick “Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH4: Tích cả 2 
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại:  lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
- Mô tả chung: Yêu cầu này thực hiện thêm mới API cho phép người dùng lập hóa đơn có mã số bí mật
- Đường dẫn API: InvoiceAPI/BotWS/createInvoiceWithCode/{taxCode}
- Đầu vào tương tư như lập hóa đơn, bổ sung thêm thông tin: 
+ thêm reservationCode trong input generalInvoiceInfo (bắt buộc) 
+ điều kiện hợp lệ: mã được cấp cho đúng MST, mã chưa được sử dụng cho hóa đơn nào, mã chưa hết hạn 
+ reservationCode trong input chính là reservationCode trong output

reservationCode	Required: true
DataType: String
Minlength: 
Maxlength: 100
Format:	Mã số bí mật



Ví dụ: 
Input generalInvoiceInfo: 
generalInvoiceInfo": {
        "invoiceType": "13",
        "templateCode": "2/035",
        "invoiceSeries": "C22DVH",
        "currencyCode": "VND",
        "adjustmentType": "1",
        "paymentStatus": true,
        "cusGetInvoiceRight": true,
        "invoiceIssuedDate": null,
        "reservationCode": " 0RS5LCM7P2ODPB4"
    }
         Output:

{
    "errorCode": null,
    "description": null,
    "result": {
        "supplierTaxCode": "0100109106-710",
        "invoiceNo": "C22DVH26",
        "transactionID": "167238328041929055",
        "reservationCode": "0RS5LCM7P2ODPB4"
       }
}
Ví dụ trường hợp lỗi: 
{
    "code": 400,
    "message": "reservation.code.used",
    "data": "BAD_REQUEST_RESERVATION_CODE_USED"
}
Lưu ý: 
1.	Nếu là lập hóa đơn máy tính tiền thì respond trả về có cả thông tin Mã CQT cấp: "codeOfTax", nếu không phải hóa đơn máy tính tiền thì trả về “codeOfTax” = null
 VD mẫu output
{
    "errorCode": null,
    "description": null,
    "result": {
        "supplierTaxCode": "0100109106-710",
        "invoiceNo": "C23MHY3",
        "transactionID": "168378907853232661",
        "reservationCode": "2QTBFEMAXFWZO5B",
        "codeOfTax": "M1-23-34567-00000000201"
    }
}
2.	Nếu cấu hình Không ký hóa đơn có mã khởi tạo từ máy tính tiền và hóa đơn thuộc loại máy tính tiền thì cho phép doanh nghiệp dùng chữ ký USB Token và CloudCA lập hóa đơn phát hành có mã bí mật bằng API Server.
3.	Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
7.28 Phát hành hóa đơn có mã bí mật cho USB-TOKEN
- Mô tả chung: Yêu cầu này thực hiện thêm mới API cho phép người dùng lập hóa đơn có mã số bí mật
- Đường dẫn API lấy chuỗi hash: InvoiceAPI/InvoiceWS/createInvoiceUsbTokenGetHash/{supplierTaxCode}
- Đường dẫn API ký và sinh hóa đơn: 
InvoiceAPI/InvoiceWS/createInvoiceUsbTokenInsertSignature
- Nội dung tương tự như phần lập hóa đơn mã số bí mật server mục 7.28
Lưu ý:
Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
7.29 Lấy danh sách mẫu và ký hiệu hóa đơn theo mã số thuế trên toàn hệ thống
-	API cho phép người dùng hệ thống tích hợp lấy danh sách mẫu và ký hiệu hóa đơn khả dụng của mã số thuế cho trước trên toàn bộ hệ thống
- Đường dẫn API: /InvoiceAPI/InvoiceUtilsWS/getAllInvoiceTemplates
Input: 
Tên trường	Kiểu dữ liệu	Mô tả
taxCode	Required: True
DataType: String
Minlength: N/A
Maxlength: 
Format:	Mã số thuế doanh nghiệp
Quy tắc validate như hiện trạng hệ thống 

invoiceType	Required: True
DataType: String
Minlength: N/A
Maxlength: 
Format:	Ví dụ với TT32: 01GTKT 
Ví dụ với TT78: 1

Ví dụ: 
{
    "taxCode": "0100109106-710",
    "invoiceType": "all"
}
Output: 
STT	Tên trường	Mô tả
1	errorcode	Mã lỗi
2	description	Mô tả lỗi
3	totalRows	Tổng số dòng kết quả tìm được
4	template	NA
5	templateCode	Mẫu hóa đơn
6	invoiceSeri	Ký hiệu hóa đơn
7	originalTemplateCode	Mẫu hóa đơn gốc 

Ví dụ:
{
    "errorCode": null,
    "description": null,
    "totalRows": 10,
    "template": [
        {
            "templateCode": "1/138",
            "invoiceSeri": "K23TYH",
            "originalTemplateCode": "1/0001"
        },
        {
            "templateCode": "1/141",
            "invoiceSeri": "K23TKH",
            "originalTemplateCode": "1/0008"
        },
        {
            "templateCode": "1/142",
            "invoiceSeri": "K23TRW",
            "originalTemplateCode": "1/0005"
        },
        {
            "templateCode": "1/143",
            "invoiceSeri": "K22TYT",
            "originalTemplateCode": "1/0001"
        },
        {
            "templateCode": "1/143",
            "invoiceSeri": "K23TEF",
            "originalTemplateCode": "1/0001"
        },
        {
            "templateCode": "1/001",
            "invoiceSeri": "C21TUH",
            "originalTemplateCode": "1/0001"
        },
        {
            "templateCode": "2/002",
            "invoiceSeri": "K23MAA",
            "originalTemplateCode": "2/0002"
        },
        {
            "templateCode": "2/002",
            "invoiceSeri": "K22MAB",
            "originalTemplateCode": "2/0002"
        },
        {
            "templateCode": "2/005",
            "invoiceSeri": "C21MYH",
            "originalTemplateCode": "2/0002"
        },
        {
            "templateCode": "6/003",
            "invoiceSeri": "K22NKL",
            "originalTemplateCode": "6/0001"
        }
    ]
}
7.30	Phát hành/thay thế/điều chỉnh cho CLOUD CA (Bước 1: Lấy chuỗi hash)
*Quy tắc kiểm tra ngày lập hóa đơn:
Hệ thống Hóa đơn điện tử SInvoice V2, phần Cấu hình chung liên quan ngày lập hóa đơn có 2 checkbox: Cho phép ngày lập hóa đơn khác ngày hiện tại, Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất.
Khi phát hành hóa đơn qua API, ngày lập hóa đơn sẽ bị ảnh hưởng khi người dùng tích chọn các checkbox này, xảy ra 4 trường hợp như mô tả sau:
TH1: Không tick cả 2
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: ngày lập không hợp lệ
- Ngày lập > ngày hiện tại: lấy ngày truyền vào (không kiểm tra giờ)
TH2: Tick “Cấu hình ngày ký là thời điểm hiện tại”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
TH3: Tick “Tự động đặt giá trị cho ngày lập hóa đơn bằng ngày lập gần nhất”
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: ngày lập không hợp lệ
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại: lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ

TH4: Tích cả 2 
- Ngày lập (invoiceIssuedDate) null: lấy ngày giờ hiện tại (sysdate)
- Ngày lập < ngày lập của hóa đơn gần nhất: lấy ngày của hóa đơn đã lập gần nhất 
- Ngày lập >= ngày lập của hóa đơn gần nhất và <= ngày hiện tại:  lấy ngày truyền vào 
- Ngày lập > ngày hiện tại: ngày lập không hợp lệ
- Sinh ra file xml và chuỗi hash của file XML của hóa đơn ký bởi USB Token.
	Đầuvào:
-	Action (POST):  InvoiceAPI/InvoiceWS/createInvoiceUsbTokenGetHash/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web  hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Đầu vào tương tư như lập hóa đơn, bổ sung thêm thông tin chứng thư gửi kèm.
Bổ sung trường Lý do sai sót hoá đơn. Điều chỉnh cho phép truyền dấu âm số lượng/ đơn giá
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
certificateSerial	Required : true
DataType: String
Minlength :  
Maxlength : 100
Format : 	Serial Number của chứng thư số của doanh nghiệp, chứng thư số này đã được doanh nghiệp đẩy lên trên hệ thống khi đăng ký sử dụng USB Token.
Định dạng Hex.
Vị dụ: 5404FFFEB7033FB316D672201B7BA4FE
adjustedNote	Required: False
DataType: String
Minlength: N/A
Maxlength: 255
Format:	Lý do sai sót 
Cho phép nhập chuỗi ký tự tối đa 255 ký tự. 
Không bắt buộc truyền.
Đặt trong generalInvoiceInfo
unitPrice	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+-	Đơn giá của hàng hóa. 
Các quy tắc ràng buộc giữ nguyên hiện trạng. 
Bổ sung cho phép truyền giá trị âm


quantity	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+-	Số lượng của hàng hóa 
Các quy tắc ràng buộc giữ nguyên hiện trạng. 
Bổ sung cho phép truyền giá trị âm



originalInvoiceType	Required: True
DataType: String
Minlength: N/A
Maxlength: 
Format:	Loại hóa đơn gốc
Truyền giá trị số với ý nghĩa như sau 
0- Không phải hóa đơn giấy/hóa đơn không tồn tại trên hệ thống 
1-Hóa đơn TT78 
2-Hóa đơn theo QĐ 1209 
3-Hóa đơn điện tử/giấy TT32
4-Hóa đơn giấy TT 78
Chú ý: 
- Trường hợp thẻ originalInvoiceType không truyền hoặc truyền giá trị rỗng/0 thì không bắt buộc truyền thẻ originalTemplateCode, hệ thống xác thực thông tin khi lập hóa đơn như hiện trạng. 
- Trường hợp thẻ originalInvoiceType truyền giá trị 1, 2, 3 hoặc 4 thì 
+ Bắt buộc phải truyền thẻ originalTemplateCode, quy tắc xác thực thẻ này tương tự như thẻ templateCode hiện tại. 
+ Khi lập hóa đơn, hệ thống không kiểm tra tính tồn tại của hóa đơn gốc trên hệ thống, các quy tắc xác thực khác giữ nguyên hiện trạng
originalTemplateCode	Required: 
DataType: String
Minlength: N/A
Maxlength: 20
Format:	Bắt buộc truyền nếu originalInvoiceType là 1, 2, 3 hoặc 4
Ví dụ mẫu TT32: 01GTKT0/001
Ví dụ mẫu TT78: 1/0224


{
   "generalInvoiceInfo":{
      "invoiceType":"01GTKT",
      "templateCode":"01GTKT0/170",
      "invoiceSeries":"AA/17E",
      "transactionUuid": "123e4567-e89b-12d3-a456-426655440000",
      "invoiceIssuedDate":1587797116843,
      "currencyCode":"VND",
      "adjustmentType":"1",
      "adjustedNote":"",
      "originalInvoiceType": "1",
      "originalTemolateCode": "1/0224",
      "paymentStatus":true,
      "paymentType":"TM",
      "paymentTypeName":"TM",
      "cusGetInvoiceRight":true,
      "userName":"user 1",
      “certificateSerial”:”5404FFFEB7033FB316D672201B7BA4FE”
   },
   "buyerInfo":{
      "buyerName":"Đặng thị thanh tâm",
      "buyerLegalName":"",
      "buyerTaxCode":"",
      "buyerAddressLine":"HN VN",
      "buyerPhoneNumber":"11111",
      "buyerEmail":"",
      "buyerIdNo":"123456789",
      "buyerIdType":"1"
   },
   "sellerInfo":{
      "sellerLegalName":"Đặng thị thanh tâm",
      "sellerTaxCode":"0100109106-501",
      "sellerAddressLine":"test",
      "sellerPhoneNumber":"0123456789",
      "sellerEmail":"PerformanceTest1@viettel.com.vn",
      "sellerBankName":"vtbank",
      "sellerBankAccount":"23423424"
   },
   "extAttribute":[

   ],
   "payments":[
      {
         "paymentMethodName":"TM"
      }
   ],
   "deliveryInfo":{

   },
   "itemInfo":[
      {
         "lineNumber":1,
         "itemCode":"ENGLISH_COURSE",
         "itemName":"Khóa học tiếng anh",
         "unitName":"khóa học",
         "unitPrice":"-3500000.0",
         "quantity":"-10.0",
         "itemTotalAmountWithoutTax":35000000,
         "taxPercentage":10.0,
         "taxAmount":0.0,
         "discount":0.0,
         "itemDiscount":150000.0
      }
   ],
   "discountItemInfo":[

   ],
"metadata":[

   ],

  "meterReading": [{
            "previousIndex": "5454",
            "currentIndex": "244",
            "factor": "22",
            "amount": "2"
          },
          {
            "previousIndex": "44",
            "currentIndex": "44",
            "factor": "33",
            "amount": "3"
          }],
   "summarizeInfo":{
      "sumOfTotalLineAmountWithoutTax":35000000,
      "totalAmountWithoutTax":35000000,
      "totalTaxAmount":3500000.0,
      "totalAmountWithTax":38500000,
      "totalAmountWithTaxInWords":"Ba mươi tám triệu năm trăm nghìn đồng chẵn",
      "discountAmount":0.0,
      "settlementDiscountAmount":0.0,
      "taxPercentage":10.0,
      "extraName": "{ Tiền phí đặc biệt, Tiền phí,  } ",
      "extraValue": "{ 00 ,00,}"
   },
   "taxBreakdowns":[
      {
         "taxPercentage":10.0,
         "taxableAmount":35000000,
         "taxAmount":3500000.0
      }
   ]
}
	Dữ liệu chuỗi Hash trả về
{
  "errorCode": "",
  "description": "",
  "result": {
    "hashString": 0HFm34vX525V3Syg5EwdTnfO21s=,  }
}

Ví dụ response trường hợp truyền sai giá trị originalInvoiceType
{
    "code": 400,
    "message": "BAD_REQUEST_ORIGINAL_INVOICE_TYPE_INVALID",
    "data": "BAD_REQUEST_ORIGINAL_INVOICE_TYPE_INVALID"
}
Lưu ý: 
1.	Dữ liệu hóa đơn gốc lưu vào cột instance_file_name trong bảng invoice như sau: 
Loại hóa đơn | Mẫu hóa đơn | Ký hiệu hóa đơn | Số hóa đơn
trong đó:
- Loại hóa đơn là giá trị thẻ originalInvoiceType 
- Mẫu hóa đơn là giá trị thẻ originalTemplateCode 
2.	Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
Output:
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
errorCode	DataType: String	Mã lỗi nếu có, không có lỗi thì trả về null
description	DataType: String	Mô tả chi tiết lỗi
hashString	DataType: String	Chuỗi Hash trả về của hóa đơn, dạng Base64

7.31	Phát hành/thay thế/điều chỉnh cho CLOUD CA (Bước 2: Ký Cloud CA và sinh hóa đơn)
- Thực hiện sử dụng CLOUD CA để ký chuỗi hashString nhận được từ API trong bước 7.31. Lấy chuỗi ký để sinh hóa đơn.
	Đầu vào:
-	Action (POST):  InvoiceAPI/InvoiceWS/createInvoiceUsbTokenInsertSignature
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type: application/json
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength :  
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
templateCode	Required : true
DataType: String
Minlength : 
Maxlength : 20	Mã mẫu hóa đơn. 

hashString	Required : true
DataType: String	Chuỗi Hash mà dữ liệu trả về ở trong request getHash phía bên trên
= out put của API : 7.15 Lập hóa đơn ký USB Token (Bước 1: Lấy chuỗi hash)
signature	Required : true
DataType: String	Chữ ký sau khi hashString đã được ký bởi USB token. dạng Base64
Vị dụ Json
{
  "supplierTaxCode": "0100109106-712",
  "templateCode": "01GTKT0/002",
  "hashString": "0HFm34vX525V3Syg5EwdTnfO21s=",
  "signature": "U0WpJk2Q/rDsnZDz8hiWKvs6QEf5DHTG8JyXjjNMtggZ/MIDP0hn9Mutc2uPZEOxqk2YnMjuRSxU8ST/T+C5i46Vb/0+7uIfzKpPm2yrsOSivCdzr6FrY6nJPkfkOWEdEs/hqDzcf4Vn8ZCVkNfovYR4prPGc7kNpO21sNb9BAI="
}
Kết quả trả về
	Dữ liệu về thông tin về hóa đơn đã lập0
{
  "errorCode": "",
  "description": "",
  "result": {
    "supplierTaxCode": 0100109106-712,
    "invoiceNo": AA/20E0000018,
    "transactionID": 12523522245,
    "reservationCode": AXHBNK8I0H
  }
}


Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lập hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lập hóa đơn thành công)
supplierTaxCode	Mã số thuế người bán (doanh nghiệp phát hành hóa đơn)
invoiceNo	Số hóa đơn vd: AA\20E0000001 
transactionID	Id của giao dịch
reservationCode	Mã số bí mật dùng để khách hàng tra cứu
Tham khảo thêm tại https://sinvoice.viettel.vn/download/soft/signhash.rar
Lưu ý: Nếu là lập hóa đơn máy tính tiền thì respond trả về có cả thông tin Mã CQT cấp: "codeOfTax", nếu không phải hóa đơn máy tính tiền thì trả về codeOfTax = null
7.32 Phát hành hóa đơn có mã bí mật cho CLOUD CA
- Mô tả chung: Yêu cầu này thực hiện thêm mới API cho phép người dùng lập hóa đơn có mã số bí mật
- Đường dẫn API lấy chuỗi hash: InvoiceAPI/InvoiceWS/createInvoiceUsbTokenGetHash/{supplierTaxCode}
- Đường dẫn API ký và sinh hóa đơn: 
InvoiceAPI/InvoiceWS/createInvoiceUsbTokenInsertSignature
- Nội dung tương tự như phần lập hóa đơn mã số bí mật server mục 7.2 
Lưu ý:
Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
7.33 Gửi email hóa đơn cho phép truyền email khách hàng
- Mô tả chung: API gửi email hóa đơn cho khách hàng dùng cho máy POS, không check cấu hình gửi email các loại hóa đơn (Quản lý hệ thống > Cấu hình doanh nghiệp > Email > Cấu hình gửi Mail)
	Đầu vào:
- Đường dẫn: api/InvoiceAPI/InvoiceUtilsWS/sendEmailToCustomer
- Method: POST
- Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json
•	Các tham số sendEmailToCustomer
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : true
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
transactionUuid	Required : true
DataType: String	Key request, transactionUuid tương ứng với 1 hoá đơn (Validate độ dài transactionUuid trong khoảng 10 – 36 ký tự).
buyerEmail	Required: true
DataType: String
Maxlength: 500	Email khách hàng cần gửi hóa đơn. Các Email cách nhau bởi dấu “;”






Vị dụ mẫu và các trường dữ liệu:
-	JSON:
{
	"supplierTaxCode": "0100109106-712s",
	"transactionUuid": "idtest9999999999 ",
	“buyerEmail”: “EmailKhachHang1@abc.xyz;EmailKhachHang2@abc.xyz;””
}

	Đầu ra:
Đối tượng Response với HTTPStatus và output Entity.
Tên trường	Mô tả
code	Mã lỗi (giá trị là “200” không có lỗi gì xảy ra)
message	Mô tả lỗi (giá trị là “OK” không có lỗi gì xảy ra)
data	Mô tả dữ liệu (giá trị là null không có lỗi gì xảy ra)


	Bộ mã lỗi:

 
STT	MÃ LỖI	NỘI DUNG LỖI	DATA	Hướng dẫn xử lý
1	BAD_REQUEST	TAX_CODE_INVALID	Mã số thuế không hợp lệ	Kiểm tra lại Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn.
2	BAD_REQUEST	TRANSACTION_UUID_REQUIRED	Transaction Uuid là bắt buộc	Truyền transactionUuid.
3	BAD_REQUEST	TAX_CODE_REQUIRED	Mã số thuế bắt buộc nhập.	Truyền Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn.
4	BAD_REQUEST	BUYER_EMAIL_REQUIRED	Email khách hàng bắt buộc nhập.	Truyền Email khách hàng.
5	BAD_REQUEST	NOT_FOUND_DATA	Không tìm thấy bản ghi.	Kiểm tra transactionUuid truyền vào.
6	BAD_REQUEST	BUYER_EMAIL_ADDRESS_FORMAT	Email không đúng định dạng.	Kiểm tra lại Email khách hàng khi truyền vào.
7	BAD_REQUEST	EMAIL_CONFIG_NOT_ACTIVE	Cấu hình Email ngừng hoạt động.	Chuyển Cấu hình Email sang Hoạt động trong Quản lý hệ thống > Cấu hình doanh nghiệp > Email.
8	
BAD_REQUEST	EMAIL_NOT_CONFIG	Chưa cấu hình Email.	Cấu hình Email trong Quản lý hệ thống > Cấu hình doanh nghiệp > Email.



 
7.34 Lập hóa đơn xăng dầu nháp
	Đầu vào:
Webservice dùng để lưu dữ liệu hóa đơn nháp lên hệ thống SInvoice. Các hóa đơn nháp này không có số hóa đơn hay kí số, chỉ có thể xem/phát hành trên website của SInvoice. Khi phát hành thì các số hóa đơn sẽ không được cập nhật lại phần mềm tích hợp.
-	Action (POST): InvoiceAPI/InvoiceWS/createOrUpdateInvoiceDraftForFuel/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/json 
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
-	Data: Định dạng JSON
-	Thông số dữ liệu truyền vào tương tự phần Lập hóa đơn (Tham khảo json tại phần 7.2). Trong thông tin hàng hóa bổ sung trường đơn giá đã bao gồm thuế:
Tên trường	Kiểu dữ liệu	Mô tả
unitPriceWithTax	Required: false
DataType: BigDecimal
Minlength: 
Maxlength: 
Format: [0-9.]+	Đơn giá của hàng hóa bao gồm thuế. 
Được sử dụng trong API lập hóa đơn nháp cho xăng dầu
-	Đơn giá của hàng hóa sẽ được tính từ đơn giá của hàng hóa đã bao gồm thuế nếu đơn giá hàng hóa đã bao gồm thuế được truyền.
-	Tổng tiền trước thuế của hàng hóa sẽ được tính từ tổng tiền đã bao gồm thuế của hàng hóa nếu tổng tiền đã bao gồm thuế của hàng hóa được truyền.
-	Ví dụ JSON đầu vào:  
	Đầu ra:
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về:
	Dữ liệu về thông tin về hóa đơn nháp lập thành công
{
  "errorCode": "",
  "description": "",
  "result": {    
  }
}

Mô tả
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null nếu lập hóa đơn thành công)
description	Mô tả lỗi (giá trị là null nếu lập hóa đơn thành công)

Lưu ý:
Nếu người dùng truyền giá trị 0 hoặc “0” cho tham số validation trong phần generalInvoiceInfo thì các thông tin được truyền trong phần itemInfo, taxBreakdowns, summarizeInfo sẽ được giữ nguyên mà không thực hiện kiểm tra ràng buộc và tính toán lại.
7.35 Tra cứu hóa đơn trả về chứa thông tin hàng hóa
- Mô tả chung: Yêu cầu này thực hiện thay đổi dữ liệu trả về. Thêm trường listProduct, fileName, buyerUnitName, buyerCode, buyerAddress, exchangeRate và listInfoUpdate so với API 7.6. Tra cứu hóa đơn.
- Đường dẫn API: 
InvoiceAPI/InvoiceUtilsWS/getAllInvoices/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web 
+ Content-Type : application/json 
Input:
Giữ nguyên như hiện tại
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : false
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
GetInvoiceInput	Object	Đối tượng gồm các trường dữ liệu tham số
- Các tham số của đối tượng GetInvoiceInput
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
invoiceNo	Required : false
DataType: String
Minlength : 7
Maxlength : 35
Format :  [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + số hóa đơn vd : AA/20E0000001

startDate	Required : true
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required : true
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập đến ngày
Định dạng "2019-05-12"

invoiceType	Required : false
DataType: String
Minlength : 
Maxlength : 
Format : 	Loại hóa đơn, là một trong các giá trị
Thông tư 32: 01GTKT, 02GTTT, 03XKNB,  04HGDL, 07KPTQ
Thông tư 78: 1, 2, 3, 4, 5, 6
rowPerPage	Required : true
DataType: Number
Min : 1
Max: 	Số dòng trên một trang 
pageNum	Required : true
DataType: Number
Min : 0
Max	Chỉ số trang
buyerTaxCode	Required : false
DataType: String
Minlength : 
Maxlength : 20	Mã số thuế của khách hàng

buyerIdNo	Required : false
DataType: String	Số giấy tờ của khách hang

templateCode	Required : false
DataType: String
Minlength : 
Maxlength : 	Mã mẫu hóa đơn.

invoiceSeri	Required : false
DataType: String
Minlength : 
Maxlength : 25
Format : [a-zA-Z0-9]*$	Ký hiệu hóa đơn

getAll	Required : false
DataType: Boolean
Minlength: 
Maxlength: 
Format : true/false	Cho phép tra cứu thông tin hóa đơn của toàn doanh nghiệp đối với user của công ty mẹ.
Các giá trị là true/false
issueStartDate	Required: false
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày phát hành từ ngày
Định dạng "2019-05-12"

issueEndDate	Required: false
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày phát hành đến ngày
Định dạng "2019-05-12"

adjustmentType	Required: false
DataType: String
Minlength: 
Maxlength: 1
Format:	Trạng thái điều chỉnh hóa đơn: 
1: Hóa đơn gốc (hóa đơn đã phát hành, hóa đơn bị điều chỉnh, hóa đơn bị thay thế)
3: Hóa đơn thay thế 
5: Hóa đơn điều chỉnh thông tin
7: Hóa đơn xóa bỏ
9: Hóa đơn điều chỉnh tiền
Không truyền sẽ trả tất cả
Ví dụ gửi dữ liệu với JSON:
{
    "supplierTaxCode": "0200572621",
    "startDate": "2023-10-20",
    "endDate": "2023-12-24",
    "rowPerPage": 1,
    "pageNum": 1
}
Output:
{
    "errorCode": null,
    "description": null,
    "totalRows": 1,
    "invoices": [
        {
            "invoiceId": 64959023,
            "invoiceType": "5",
            "adjustmentType": "1",
            "templateCode": "5/010",
            "invoiceSeri": "K24GHY",
            "invoiceNumber": "0000001",
            "invoiceNo": "K24GHY1",
            "currency": "VND",
            "total": 60500000.000000000,
            "issueDate": null,
            "issueDateStr": "2024-03-14T03:17:59Z",
            "state": 1,
            "requestDate": null,
            "description": null,
            "buyerIdNo": "123",
            "stateCode": 1,
            "subscriberNumber": null,
            "paymentStatus": 1,
            "viewStatus": null,
            "downloadStatus": null,
            "exchangeStatus": 0,
            "numOfExchange": null,
            "createTime": null,
            "contractId": null,
            "contractNo": "0123",
            "supplierTaxCode": "0100109106-990",
            "buyerTaxCode": "0100109106",
            "totalBeforeTax": 55000000.000000000,
            "taxAmount": 5500000.000000000,
            "taxRate": null,
            "paymentMethod": "3",
            "paymentTime": null,
            "customerId": null,
            "no": null,
            "paymentStatusName": "Đã thanh toán",
            "buyerName": "Khánh Linh",
            "transactionUuid": null,
            "originalInvoiceId": "K22THY32",
             "errorCode": "INVOICE_NO_CODE_APPROVED",
    "errorDescription": null,

            "listProduct": "{\"itemInfo\":[{\"selection\":1,\"lineNumber\":1,\"itemCode\":\"02\",\"itemName\":\"Tên hàng hóa\",\"unitCode\":null,\"unitName\":\"chiếc\",\"unitPrice\":55000000,\"quantity\":1,\"itemTotalAmountWithoutVat\":55000000.000000,\"itemTotalAmountWithVat\":60500000.00,\"itemTotalAmountAfterDiscount\":55000000.000000,\"itemServiceChargePercentage\":null,\"itemServiceChargeAmount\":0.00000,\"itemExciseTaxPercentage\":null,\"itemExciseTaxAmount\":0.00000,\"vatPercentage\":10,\"vatAmount\":5500000.00000,\"discount\":null,\"discount2\":null,\"itemDiscount\":null,\"itemNote\":null,\"batchNo\":null,\"expDate\":null,\"isIncreaseItem\":null,\"adjustRatio\":null}],\"invoiceTaxBreakdowns\":[{\"vatPercentage\":10,\"vatTaxableAmount\":55000000.000000,\"vatTaxAmount\":5500000.00000,\"isIncreaseItem\":null}]}",
            "fileName": null,
            "buyerUnitName": "Công ty VTT",
            "buyerCode": null,
            "buyerAddress": "Hà Nội",
            "exchangeRate": 1.00,
            "listInfoUpdate": "[{\"invoiceCustomFieldId\":0,\"keyTag\":\"gioitinh\",\"keyLabel\":\"Giới tính\",\"dateValue\":null,\"stringValue\":\"Giới tính\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"ngaysinh\",\"keyLabel\":\"Ngày sinh\",\"dateValue\":\"2024-03-07T17:00:00.000Z\",\"stringValue\":null,\"numberValue\":null,\"valueType\":\"3\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"maqg\",\"keyLabel\":\"Mã quốc gia\",\"dateValue\":null,\"stringValue\":\"Mã quốc gia\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"sodkpt\",\"keyLabel\":\"Số đăng ký phương tiện\",\"dateValue\":null,\"stringValue\":\"Số đăng ký phương tiện\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"soghe\",\"keyLabel\":\"Số ghế\",\"dateValue\":null,\"stringValue\":\"Số ghế\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"giotc\",\"keyLabel\":\"Giờ tàu chạy\",\"dateValue\":null,\"stringValue\":\"Giờ tàu chạy\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"ngaydi\",\"keyLabel\":\"Ngày đi\",\"dateValue\":\"2024-03-07T17:00:00.000Z\",\"stringValue\":null,\"numberValue\":null,\"valueType\":\"3\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false}]"
        }
    ]
}

Đối tượng Response với HTTPStatus và output  Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null lấy hóa đơn thành công)
description	Mô tả lỗi (giá trị là null lấy hóa đơn thành công)
List<InvoiceBean>	Danh sách các bản ghi hóa đơn thỏa mãn điều kiện  

7.36 Gửi hóa đơn sang CQT bằng transactionUuid
       -     Mô tả chung: API gửi hóa đơn cho cơ quan thuế  
	Đầu vào:
-	Action (POST):  InvoiceAPI/InvoiceWS/sendInvoiceByTransactionUuid
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web
+ Content-Type : application/x-www-form-urlencoded

Tên trường	Kiểu dữ liệu, ràng buộc	Dữ liệu/mô tả
supplierTaxCode	Required: true
DataType: String
Minlength: 
Maxlength: 20
Format: [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
transactionUuid	Required: true
DataType: String	Danh sách key request, mỗi transactionUuid tương ứng với 1 hoá đơn (Validate độ dài transactionUuid trong khoảng 10 – 36 ký tự). Các transactionUuid cách nhau bởi dấu “,”
startDate	Required: true
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required: true
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày lập đến ngày
Định dạng "2019-05-12"


Ví dụ với định dạng formParam:
 
Hình ảnh Response trả về thành công
 
-	Ouput:
o	Lỗi chung do dữ liệu đầu vào:
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
code	DataType: String	Loại lỗi
message	DataType: String	Mã lỗi
data	DataType: String	Mô tả lỗi
Ví dụ:
{
    "code": 400,
    "message": "START_DATE_INVALID",
    "data": "Ngày bắt đầu không hợp lệ"
}
o	Lỗi khi check quyền:
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
error	DataType: String	Loại lỗi
error_description	DataType: String	Mã lỗi
Ví dụ:
<InvalidTokenException>
    <error>invalid_token</error>
    <error_description>Access token expired: xxx</error_description>
</InvalidTokenException>
o	Lỗi khi gửi hóa đơn sang CQT bị lỗi:
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
total	DataType: String	Tổng số hóa đơn
success	DataType: String	Số hóa đơn thành công
fail	DataType: String	Số hóa đơn không thành công
errorlist	DataType: array	Mảng data
errorlist.transactionUuid	DataType: String	Danh sách transactionUuid có cùng mã lỗi
errorlist.detail	DataType: String	Mô tả lỗi
errorlist.message	DataType: String	Mã lỗi
Ví dụ trường hợp không có dữ liệu gửi sang CQT:
{
    "errorCode": null,
    "description": null,
    "total": "3",
    "success": "1",
    "fail": "2",
    "errorlist": [
        {
            "transactionUuid": "028717bc-5315-4a0b-9ab0-ce8d5495e56g,028717bc-5315-4a0b-9ab0-ce8d5495e57f",
            "detail": "Không tìm thấy bản ghi cần gửi sang CQT",
            "message": "INVOCIE_NOT_FOUND"
        }
    ]
}
Ví dụ trường hợp gửi dữ liệu sang CQT thành công, có dữ liệu không thành công:
{
    "errorCode": null,
    "description": null,
    "total": "3",
    "success": "1",
    "fail": "2",
    "errorlist": [
        {
            "transactionUuid": "028717bc-5315-4a0b-9ab0-ce8d5495e56f",
            "detail": "Hóa đơn xóa bỏ không gửi thuế",
            "message": "INVOCIE_NOT_SEND_CQT"
        },
        {
            "transactionUuid": "028717bc-5315-4a0b-9ab0-ce8d5495e56g",
            "detail": "Không tìm thấy bản ghi cần gửi sang CQT",
            "message": "INVOCIE_NOT_FOUND"
        }
    ]
}
Ví dụ trường hợp gửi dữ liệu sang CQT thành công:
{
    "errorCode": null,
    "description": null,
    "total": "2",
    "success": "2",
    "fail": "0",
    "errorlist": []
}
-	Ví dụ cho phần đầu vào gọi API:
curl --location 'http://localhost:8080/api/InvoiceAPI/InvoiceWS/sendInvoiceByTransactionUuid' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Bearer XXX \
--data-urlencode 'supplierTaxCode=0100109106-710' \
--data-urlencode 'transactionUuid=028717bc-5315-4a0b-9ab0-ce8d5495e56e' \
--data-urlencode 'startDate=2023-10-10' \
--data-urlencode 'endDate=2024-10-10' 

7.37 Tra cứu hóa đơn trả về chứa thông tin hàng hóa (UTC + 7)
- Mô tả chung: Yêu cầu này thực hiện nâng cấp API 7.37 dữ liệu trả về trường “issueDateStr” trả về đúng thời gian phát hành hóa đơn (có nghĩa là UTC + 7)
- Đường dẫn API: 
InvoiceAPI/InvoiceUtilsWS/getInvoicesAll/{supplierTaxCode}
-	Headers:
+ Cookie: giá trị access_token hoặc Authorization: username/pass như đăng nhập trên web 
+ Content-Type : application/json 
Input:
Giữ nguyên như hiện tại
Tên trường	Kiểu dữ liệu, ràng buộc	Mô tả
supplierTaxCode	Required : false
DataType: String
Minlength : 
Maxlength : 20
Format : [0-9-]+	Mã số thuế của doanh nghiệp/chi nhánh phát hành hóa đơn. Một doanh nghiệp có thể có nhiều mã số thuế
Mẫu 1: 0312770607 
Mẫu 2: 0312770607-001
GetInvoiceInput	Object	Đối tượng gồm các trường dữ liệu tham số
- Các tham số của đối tượng GetInvoiceInput
Tên tham số	Kiểu dữ liệu, ràng buộc	Mô tả
invoiceNo	Required : false
DataType: String
Minlength : 7
Maxlength : 35
Format :  [a-zA-Z0-9]*$	Là ký hiệu hóa đơn + số hóa đơn vd : AA/20E0000001

startDate	Required : true
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập từ ngày
Định dạng "2019-05-12"

endDate	Required : true
DataType: Date
Minlength : 
Maxlength : 50
Format :	Ngày lập đến ngày
Định dạng "2019-05-12"

invoiceType	Required : false
DataType: String
Minlength : 
Maxlength : 
Format : 	Loại hóa đơn, là một trong các giá trị
Thông tư 32: 01GTKT, 02GTTT, 03XKNB,  04HGDL, 07KPTQ
Thông tư 78: 1, 2, 3, 4, 5, 6
rowPerPage	Required : true
DataType: Number
Min : 1
Max: 	Số dòng trên một trang 
pageNum	Required : true
DataType: Number
Min : 0
Max	Chỉ số trang
buyerTaxCode	Required : false
DataType: String
Minlength : 
Maxlength : 20	Mã số thuế của khách hàng

buyerIdNo	Required : false
DataType: String	Số giấy tờ của khách hang

templateCode	Required : false
DataType: String
Minlength : 
Maxlength : 	Mã mẫu hóa đơn.

invoiceSeri	Required : false
DataType: String
Minlength : 
Maxlength : 25
Format : [a-zA-Z0-9]*$	Ký hiệu hóa đơn

getAll	Required : false
DataType: Boolean
Minlength: 
Maxlength: 
Format : true/false	Cho phép tra cứu thông tin hóa đơn của toàn doanh nghiệp đối với user của công ty mẹ.
Các giá trị là true/false
issueStartDate	Required: false
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày phát hành từ ngày
Định dạng "2019-05-12"

issueEndDate	Required: false
DataType: Date
Minlength: 
Maxlength: 50
Format:	Ngày phát hành đến ngày
Định dạng "2019-05-12"

adjustmentType	Required: false
DataType: String
Minlength: 
Maxlength: 1
Format:	Trạng thái điều chỉnh hóa đơn: 
1: Hóa đơn gốc (hóa đơn đã phát hành, hóa đơn bị điều chỉnh, hóa đơn bị thay thế)
3: Hóa đơn thay thế 
5: Hóa đơn điều chỉnh thông tin
7: Hóa đơn xóa bỏ
9: Hóa đơn điều chỉnh tiền
Không truyền sẽ trả tất cả
Ví dụ gửi dữ liệu với JSON:
{
    "supplierTaxCode": "0200572621",
    "startDate": "2023-10-20",
    "endDate": "2023-12-24",
    "rowPerPage": 1,
    "pageNum": 1
}
Output:
{
    "errorCode": null,
    "description": null,
    "totalRows": 1,
    "invoices": [
        {
            "invoiceId": 64959023,
            "invoiceType": "5",
            "adjustmentType": "1",
            "templateCode": "5/010",
            "invoiceSeri": "K24GHY",
            "invoiceNumber": "0000001",
            "invoiceNo": "K24GHY1",
            "currency": "VND",
            "total": 60500000.000000000,
            "issueDate": null,
            "issueDateStr": "2024-03-14T03:17:59Z",
            "state": 1,
            "requestDate": null,
            "description": null,
            "buyerIdNo": "123",
            "stateCode": 1,
            "subscriberNumber": null,
            "paymentStatus": 1,
            "viewStatus": null,
            "downloadStatus": null,
            "exchangeStatus": 0,
            "numOfExchange": null,
            "createTime": null,
            "contractId": null,
            "contractNo": "0123",
            "supplierTaxCode": "0100109106-990",
            "buyerTaxCode": "0100109106",
            "totalBeforeTax": 55000000.000000000,
            "taxAmount": 5500000.000000000,
            "taxRate": null,
            "paymentMethod": "3",
            "paymentTime": null,
            "customerId": null,
            "no": null,
            "paymentStatusName": "Đã thanh toán",
            "buyerName": "Khánh Linh",
            "transactionUuid": null,
            "originalInvoiceId": "K22THY32",
             "errorCode": "INVOICE_HAS_CODE_APPROVED",
    "errorDescription": null,

            "listProduct": "{\"itemInfo\":[{\"selection\":1,\"lineNumber\":1,\"itemCode\":\"02\",\"itemName\":\"Tên hàng hóa\",\"unitCode\":null,\"unitName\":\"chiếc\",\"unitPrice\":55000000,\"quantity\":1,\"itemTotalAmountWithoutVat\":55000000.000000,\"itemTotalAmountWithVat\":60500000.00,\"itemTotalAmountAfterDiscount\":55000000.000000,\"itemServiceChargePercentage\":null,\"itemServiceChargeAmount\":0.00000,\"itemExciseTaxPercentage\":null,\"itemExciseTaxAmount\":0.00000,\"vatPercentage\":10,\"vatAmount\":5500000.00000,\"discount\":null,\"discount2\":null,\"itemDiscount\":null,\"itemNote\":null,\"batchNo\":null,\"expDate\":null,\"isIncreaseItem\":null,\"adjustRatio\":null}],\"invoiceTaxBreakdowns\":[{\"vatPercentage\":10,\"vatTaxableAmount\":55000000.000000,\"vatTaxAmount\":5500000.00000,\"isIncreaseItem\":null}]}",
            "fileName": null,
            "buyerUnitName": "Công ty VTT",
            "buyerCode": null,
            "buyerAddress": "Hà Nội",
            "exchangeRate": 1.00,
            "listInfoUpdate": "[{\"invoiceCustomFieldId\":0,\"keyTag\":\"gioitinh\",\"keyLabel\":\"Giới tính\",\"dateValue\":null,\"stringValue\":\"Giới tính\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"ngaysinh\",\"keyLabel\":\"Ngày sinh\",\"dateValue\":\"2024-03-07T17:00:00.000Z\",\"stringValue\":null,\"numberValue\":null,\"valueType\":\"3\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"maqg\",\"keyLabel\":\"Mã quốc gia\",\"dateValue\":null,\"stringValue\":\"Mã quốc gia\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"sodkpt\",\"keyLabel\":\"Số đăng ký phương tiện\",\"dateValue\":null,\"stringValue\":\"Số đăng ký phương tiện\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"soghe\",\"keyLabel\":\"Số ghế\",\"dateValue\":null,\"stringValue\":\"Số ghế\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"giotc\",\"keyLabel\":\"Giờ tàu chạy\",\"dateValue\":null,\"stringValue\":\"Giờ tàu chạy\",\"numberValue\":null,\"valueType\":\"1\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false},{\"invoiceCustomFieldId\":0,\"keyTag\":\"ngaydi\",\"keyLabel\":\"Ngày đi\",\"dateValue\":\"2024-03-07T17:00:00.000Z\",\"stringValue\":null,\"numberValue\":null,\"valueType\":\"3\",\"isRequired\":false,\"isSeller\":false,\"required\":false,\"seller\":false}]"
        }
    ]
}

Đối tượng Response với HTTPStatus và output Entity.
Tên trường	Mô tả
errorCode	Mã lỗi (giá trị là null lấy hóa đơn thành công)
description	Mô tả lỗi (giá trị là null lấy hóa đơn thành công)
List<InvoiceBean>	Danh sách các bản ghi hóa đơn thỏa mãn điều kiện  


 

8	Danh sách lỗi trả về của hệ thống 
Đối tượng Response mô tả trạng thái lỗi Webservice trả về và đối tượng dữ liệu Webservice trả về. Bao gồm mã lỗi và mô tả lỗi. 
Note: Khi phát sinh lỗi việc đầu tiên kiểm tra mã lỗi trong danh sách lỗi để nắm được tại sao lỗi và cách khắc phục.
Bộ mã lỗi hay gặp:
STT	MÃ LỖI	NỘI DUNG LỖI	DATA	Hướng dẫn xử lý
1	BAD_REQUEST	VAT_AMOUNT_INVALID	Tiền thuế không hợp lệ	Kiểm tra lại tiền thuế, tiền thuế chỉ được lệch 1đ so với tiền thuế hệ thống tính
2	BAD_REQUEST	VAT_TAX_AMOUNT_NEGATE	Tiền thuế không được nhập giá trị âm	Mọi giá trị đều phải là số dương
3	BAD_REQUEST	VAT_PERCENTAGE_INVALID	Thuế GTGT( %) không hợp lệ	Kiểm tra xem thuộc các giá trị: -2, -1, 0, 5, 8, 10
4	BAD_REQUEST	INVOICE_SERIAL_NOT_FOUND	Ký hiệu hóa đơn không tồn tại	Kiểm tra lại mã mẫu và ký hiệu có ở trạng thái hoạt động không
5	BAD_REQUEST	IVI_TOTAL_A_WITHOUT_TAX_
AND_UP_QUAN_NOT_COMPARED	Đơn giá nhân thành tiền không so khớp	Kiểm tra lại xem thành tiền đã khớp với đơn giá nhân số lượng chưa
6	BAD_REQUEST	JSON_PARSE_ERROR	Lỗi định dạng dữ liệu truyền vào	Kiểm tra lại xem đúng định dạng json chưa
7	500	"error": "Internal Server Error",
"message": "Request processing failed; 
nested exception is java.lang.
NullPointerException",	Request processing failed; 
nested exception is java.lang.NullPointerException	Kiểm tra lại mã mẫu, ký hiệu đã truyền đúng với thông báo phát hành chưa và thông báo phát hành đấy đã ở trạng thái đang hoạt động chưa, nếu rồi thì kiểm tra lại mẫu có ở trạng thái đang hoạt động không
8	500	"error": "Internal Server Error",
    "message": "GENERAL"	Token hết hạn	Lấy lại token mới
9	
400	BAD_REQUEST_INVOICE_NOT
_USE_OTHER_FEE	BAD_REQUEST_INVOICE_NOT_
USE_OTHER_FEE	Cài đặt cấu hình phí khác xem đủ dữ liệu chưa
10	
400	BAD_REQUEST_INVALID_
DECIMAL_POINT_QUANTUM	Cấu hình số thập phân	Kiểm tra lại cấu hình số thập phân
11	
400	BAD_REQUEST_EXISTS_OTHER
_USB_SIGN_PROCESSING	Có hóa đơn đang xử lý chưa được ký	Xóa hết nháp đã tạo r lấy chuỗi hash
 
9	Mapping giữa các trường thông tin và mẫu hóa đơn
Các trường thông tin sẽ được mapping lên mẫu hóa đơn phụ thuộc vào thiết kế chi tiết của mẫu hóa đơn đó. Về cơ bản sẽ các mẫu hóa đơn sẽ được mapping các trường như sau:
Lưu ý: trong trường hợp trường thông tin không hiển thị đúng, nguyên nhân có thể do dữ liệu gửi sang chưa đúng hoặc mẫu hóa đơn thiết kế không hiển thị đúng thông tin. Kiểm tra dữ liệu trong file hóa đơn gốc (xml) tải về xem đúng chưa.
