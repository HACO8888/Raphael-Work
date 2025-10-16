'''***********************************************************************
   學    號 ：1148168
   姓    名 ：文仲賢
   完成日期 ：2025/10/05
   檔    名 ：N8168PrgHW03_3.py
   程式功能 ：電影院售票系統：輸入全票與學生票張數，計算總金額
             （全票 250 元/張；學生票 85 折）。
************************************************************************'''

full_price = 250
student_discount = 0.85

full_count = int(input("請輸入全票張數："))
student_count = int(input("請輸入學生票張數："))

total = full_count * full_price + student_count * full_price * student_discount
print("總金額 = %.2f 元" % total)