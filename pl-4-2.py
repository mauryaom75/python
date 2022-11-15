w = int(input("enter your w :"))
h = int(input("enter your h :"))
bmi = w/(h**2)
if bmi < 19:
        print("you are underweight")
elif bmi > 25:
        print("you are overweight")
else:
        print("you are healthy")
