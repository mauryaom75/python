sub1=int(input("enter the marks of subject :"))
sub2=int(input("enter the marks of subject :"))
sub3=int(input("enter the marks of subject :"))
sub4=int(input("enter the marks of subject :"))
sub5=int(input("enter the marks of subject :"))

a=(sub1+sub2+sub3+sub4+sub5)/5

if a>=90:
    print("grad a")
elif a>80 and a<89:
    print("grad b")
elif a>70 and a<79:
    print("grad c")
elif a>60 and a<69:
    print("grad d")
elif a>50 and a<59:
    print("grad e")
elif a<50:
    print("fail")
    
