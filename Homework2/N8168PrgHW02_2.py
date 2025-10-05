'''***********************************************************************
   學    號 ：1148168
   姓    名 ：文仲賢
   完成日期 ：2025/10/05
   檔    名 ：N8168PrgHW02_2.py
   程式功能 ：輸入一元二次方程式的係數，求出兩個實數解
************************************************************************'''

import math

def solve_quadratic():
    print("一元二次方程式：ax² + bx + c = 0")
    a = float(input("請輸入係數 a："))
    b = float(input("請輸入係數 b："))
    c = float(input("請輸入係數 c："))
    
    if a == 0:
        print("錯誤：a 不能為 0")
        return
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        print("警告：此方程式沒有實數解（b² < 4ac）")
        return
    
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    print(f"\n方程式的兩個實數解為：")
    print(f"x₁ = {x1:.4f}")
    print(f"x₂ = {x2:.4f}")

solve_quadratic()