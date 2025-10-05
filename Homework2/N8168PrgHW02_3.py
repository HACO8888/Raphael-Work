'''***********************************************************************
   學    號 ：1148168
   姓    名 ：文仲賢
   完成日期 ：2025/10/05
   檔    名 ：N8168PrgHW02_3.py
   程式功能 ：輸入身高及體重，計算BMI值與男女理想體重
************************************************************************'''

def calculate_bmi_and_ideal_weight():
    height_cm = float(input("請輸入身高(cm)："))
    weight_kg = float(input("請輸入體重(kg)："))
    
    height_m = height_cm / 100
    
    bmi = weight_kg / (height_m ** 2)
    
    ideal_weight_male = (height_cm - 80) * 0.7
    ideal_weight_female = (height_cm - 70) * 0.6
    
    print(f"\n=== 計算結果 ===")
    print(f"您的BMI值 = {bmi:.2f}")
    print(f"\n理想體重：")
    print(f"男生理想體重 = {ideal_weight_male:.2f} kg")
    print(f"女生理想體重 = {ideal_weight_female:.2f} kg")
    
    print(f"\nBMI分類參考：")
    if bmi < 18.5:
        print("體重過輕")
    elif 18.5 <= bmi < 24:
        print("正常範圍")
    elif 24 <= bmi < 27:
        print("過重")
    elif 27 <= bmi < 30:
        print("輕度肥胖")
    elif 30 <= bmi < 35:
        print("中度肥胖")
    else:
        print("重度肥胖")

calculate_bmi_and_ideal_weight()