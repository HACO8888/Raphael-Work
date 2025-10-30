'''***********************************************************************
   學    號 ：1148168
   姓    名 ：文仲賢
   完成日期 ：2025/10/30
   檔    名 ：N8168PrgHW05_3.py
   程式功能 ：第三題 3-1~3-4 合併，選單執行各子題功能。
************************************************************************'''
def sum_1_to_1000():
    s = 0
    for i in range(1, 1001):
        s += i
    return s

def sum_div_3_or_8():
    s = 0
    for i in range(1, 101):
        if i % 3 == 0 or i % 8 == 0:
            s += i
    return s

def sum_even_not_3():
    s = 0
    for i in range(1, 101):
        if i % 2 == 0 and i % 3 != 0:
            s += i
    return s

def series():
    s = 0.0
    for n in range(1, 101):
        s += 1.0 / (n ** 3)
    return s

print("功能選單")
print("(1) 累計 1~1000 的總和")
print("(2) 1~100 中可被 3 或 8 整除的總和")
print("(3) 1~100 中可被 2 整除且不可被 3 整除的總和")
print("(4) 1 + 1/2^3 + ... + 1/100^3 的值")
k = int(input("請輸入功能代號(1~4)："))
if k == 1:
    print("累計 1~1000 的總和 = %d" % sum_1_to_1000())
elif k == 2:
    print("1~100 中可被 3 或 8 整除的總和 = %d" % sum_div_3_or_8())
elif k == 3:
    print("1~100 中可被 2 整除且不可被 3 整除的總和 = %d" % sum_even_not_3())
elif k == 4:
    print("值 = %.7f" % series())
else:
    print("輸入錯誤")
