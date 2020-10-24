a=int(input("도형을 입력하시오.(1: 사각형, 2: 삼각형, 3: 원) "))

if a==1:
    width=float(input("가로 : "))
    height=float(input("세로 : "))
    print("면적 : ", width*height)
elif a==2:
    width=float(input("밑변 : "))
    height=float(input("높이 : "))
    print("면적 : ", width*height/2)
elif a==3:
    r=float(input("반지름 : "))
    print("면적 : ", r*r*3.14)
else :
    print("잘못 입력하셨습니다. ")