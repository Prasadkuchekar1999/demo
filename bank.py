class customer:
    def __init__(s,name,email,contact,adhar,password):
        s.name=name
        s.email=email
        s.contact=contact
        s.adhar=adhar
        s.password=password
        s.balance=0
        s.account=s.name[:3]+s.contact[:5]#s.adhar[::3]
        print('your account no is :',s.account)
    def __str__(s):
        return (s.name)+' '+str(s.email)+' '+str(s.contact)+' '+(s.adhar)+' '+str(s.password)+ ' '+str(s.balance)
##c=customer('prasad','p@gmail.com',12345678,'1235423464','0987654')
##print(c.__str__())
class bank:
    blist=[]
    def __init__(s):
        s.execute()
    
    def login(s):
        acc=input('ENTER YOUR ACCOUNT NO :')
        password=input('ENTER YOUR PASSWORD :')
        for i in s.blist:
            if acc==i.account and password ==i.password:
                print('LOGIN SUCCESSFULLY')
                a=1
                while(a>0):
                    print('enter 1 for customer details :')
                    print('enter 2 for customer deposite :')
                    print('enter 3 for customer withdraw :')
                    print('enter 4 for customer balance :')
                    print('enter 5 for exit :')
                    num=int(input('enter your bank choice : '))
                    if num==1:
                        print(i)
                    elif num==2:
                        amt=int(input('enter tour deposit amount : '))
                        i.balance=i.balance+amt
                        print(amt,'DEPOSITE SUCESSFULLY ')
                    elif num==3:
                        wit=int(input('ENTER YOUR WITHDRAL AMOUNT :'))
                        i.balance=i.balance-wit
                        print(wit,'WITHDRAWL SUCCESFULLY ')
                        print('your balance is :',i.balance)
                    elif num==4:
                        print(i.balance)
                    elif num==5:
                        a=0
                        print('THANKS FOR VISITING')
                        break
                    else:
                        print('please enter valid account')
            else:
                 print('please enter valid account')
            


                    
    def execute(s):
        b=1
        while b>0:
            print('enter 1 for add account :')
            print('enter 2 for login :')
            print('enter 3 for exit :')
            num=int(input('enter your choice :'))
            if num==1:
             name=input('enter name : ')
             email=input('enter email : ')
             contact=input('enter contact : ')
             adhar=input('enter adhar no : ')
             password=input('enter password : ')
             c=customer(name,email,contact,adhar,password)
             s.blist.append(c)
            elif num==2:
                s.login()
            elif num==3:
                b=0
                print("Thank to visit ")
            
b=bank()
