# ค้นหาตัวเลขที่มากสุดหีรือน้อยสุด
max,min =0,0
while True : 
    number=int(input("ป้อนตัวเลขของคูณ :"))
    if number<0 :
        break
    if number>max:
        max=number
    if number<min: 
        min=number

print("ค่าสูงสุด = ",max)
print("ค่าต่ำสุด = ",min)