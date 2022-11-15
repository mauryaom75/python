num=int(input("enter any number:"))
total_sum=0
for n in range(num):
       number=float(input("enter number:"))
total_sum+=number
avg=total_sum/num
print("average of",num,"number is",avg)