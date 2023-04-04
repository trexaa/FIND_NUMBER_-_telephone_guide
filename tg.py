import os 
import sys 
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

telephone_guide ={}

menu = """
Choose
1) Search in telephone guide
2) add in telephone guide
3) show the all the telephone guide
4) to Know about the number :)
5) to exti the program

"""

def st():
    def se():
        try:
            num = int(input("enter the number : "))
            print([telephone_guide[num]])
            var = input("do you want to serch again? ")
            if var.lower()=='no':
                os.execl(sys.executable, sys.executable, *sys.argv)
            if var.lower()=='yes':
                st()
        except KeyError:
            print("Sorry, the number is not found")
        except ValueError:
            print("This is invalid number")

    def add():
        try:
            name = input("enter the name")
            number = int(input("enter the numder "))
            telephone_guide[name]=number
            var = input("do you want to run again? ")
            if var.lower()=='no':
                os.execl(sys.executable, sys.executable, *sys.argv)
            if var.lower()=='yes':
                st()
        except KeyError:
            print("Sorry, the number is not found")
        except ValueError:
            print("This is invalid number")

    def show():
        print(telephone_guide)
        var = input("do you want to run again? ")
        if var.lower()=='no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower()=='yes':
            st()

    def find():
        enter_num = str(input("Please enter a phone number: "))
        phone_num = phonenumbers.parse(enter_num,None)
        print(phone_num)
        ge=("The State Key : " + geocoder.description_for_number(phone_num,"en"))
        ca=("The Telecom Company :" + carrier.name_for_number(phone_num,"en"))
        tz=timezone.time_zones_for_number(phone_num)
        print("The number: "+ str(phone_num)+"The State Key: "+ str(ge) +"The Telecom Company: "+ str(ca) +"The Time zone: "+str(tz))
        var = input("do you want to run again? ")
        if var.lower()=='no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower()=='yes':
            st()

    def exit():
        print("good bye")
        os.execl(sys.executable, sys.executable, *sys.argv)

    ans = input(menu)
    if ans =='1':
        se()
    if ans=='2':
        add()
    if ans=='3':
        show()
    if ans=='4':
        find()
    if ans=='5':
        exit()
st()