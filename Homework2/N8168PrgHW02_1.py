'''***********************************************************************
   學    號 ：1148168
   姓    名 ：文仲賢
   完成日期 ：2025/10/05
   檔    名 ：N8168PrgHW02_1.py
   程式功能 ：輸入球的半徑，計算並輸出球的體積與表面積
************************************************************************'''

import math

def calculate_sphere():
    radius = float(input("請輸入球的半徑(cm)："))
    
    volume = (4/3) * math.pi * (radius ** 3)
    surface_area = 4 * math.pi * (radius ** 2)
    
    print(f"\n球的體積 = {volume:.2f} cm³")
    print(f"球的表面積 = {surface_area:.2f} cm²")

calculate_sphere()