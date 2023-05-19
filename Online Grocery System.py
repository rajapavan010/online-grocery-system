import hashlib
import time
totalsum=[]

def fruits():
    costv=[37,43,67,15,43,67,15,32,20,12,34,102,201,109,157,83,52,44,43,31]
    sumv=0
    time.sleep(3)
    print("\n1.Onion-Rs:37(per KG)")
    print("2.Potato-RS:43(Per KG)")
    print("3.Carrot-Rs:67(per KG)")
    print("4.Tomato-Rs:15(per KG)")
    print("5.Potato-RS:43(Per KG)")
    print("6.Carrot-Rs:67(per KG)")
    print("7.Beans-Rs:15(per 500g")
    print("8.Ladies Finger-Rs:32(per KG)")
    print("9.Couliflowe-Rs:20(Per pic-400 to 600g)")
    print("10.Cucumber-Rs:12(Per 500g)")
    print("11.Banana-Rs:34(Per 500g)")
    print("12.Apple-Rs:102(per 4 pic)")
    print("13.pomegranate-Rs:201(per 4 pic)")
    print("14.orange-Rs:109(per KG)")
    print("15.Kiwi-Rs:157(3 pic)")
    print("16.Watermelon-Rs:83(per pic)")
    print("17.Papaya-Rs:52(per pic-500 to 800g)")
    print("18.Pineapple-Rs:44(per pic-800 to 1000g)")
    print("19.Guava-Rs:43(per pic)")
    print("20.Muskmelon-Rs:31(per pic-500 to 900g)")
    chv=int(input("Enter how many products do you want to select : "))
    for i in range(chv):
        j=int(input("Enter choice : "))
        kg=float(input("Enter how many kgs or grams do you want : "))
        amount=kg*costv[j-1]
        sumv=sumv+amount
    totalsum.append(sumv)
    print("Total Amount for this category",sumv)
    a=int(input("Enter 1 to continue or 7 to Bill: "))
    if a==1:
        mainmenu()
    else:
        bill()

def Foodgrains():
    costf=[63,116,274,49,41,55,49,1375,60,1650,1275,149,179,61,143,139,135,160,164,759]
    sumf=0
    time.sleep(3)
    print("\n1.Atta-Rs:63(1kg)")
    print("1.Atta-Rs:116(2kg)")
    print("1.Atta-Rs:274(5kg)")
    print("4.Sooji-Rs:49(1Kg)")
    print("5.Rice-Rs:41(1Kg)")
    print("6.Bansi Sooji-Rs:55(1Kg)")
    print("7.Maida-Rs:49(1Kg)")
    print("8.Sona Masoori-Rs:1375(25Kg)")
    print("9.Poha-Rs:60(1Kg)")
    print("10.HMT Rice-Rs:1650(25Kg)")
    print("11.Steam Rice-Rs:1275(25Kg)")
    print("12.Dal-Rs:149(1Kg)")
    print("13.Peanuts-Rs:179(1Kg)")
    print("14.Fried Gram-Rs:61(500g)")
    print("15.Moong Dal-Rs:143(1Kg)")
    print("16.UradDal-Rs:139(1Kg)")
    print("17.Green Moong-Rs:135(1Kg)")
    print("18.Sunflower Oil-Rs:160(1L)")
    print("19.Refined Oil-Rs:164(1L)")
    print("20.Olive Oil-Rs:759(1L)")
    chf=int(input("Enter how many products do you want to select : "))
    for i in range(chf):
        j=int(input("Enter choice : "))
        kg=float(input("Enter how many kgs or L do you want : "))
        amount=kg*costf[j-1]
        sumf=sumf+amount
    totalsum.append(sumf)
    print("Total Amount for this category",sumf)
    a=int(input("Enter 1 to continue or 7 to Bill : "))
    if a==1:
        mainmenu()
    else:
        bill()
        
def diary():
    costb=[97,44,60,265,60,386,23,106,104,104,99,16,30,175,5,10,15,90,175,50]
    sumb=0    
    time.sleep(3)
    print("\n1.Panner-Rs:97(200g)")
    print("2.Curd-Rs:44(500g)")
    print("3.Milk-Rs:60(1L)")
    print("4.Butter-Rs:265(500g)")
    print("5.Butter Milk-Rs:60(1L)")
    print("6.Cheese-Rs:386(750g)")
    print("7.Lassi-Rs:23(250Ml)")
    print("8.Condensed Milk-Rs:106(400g)")
    print("9.Bread-Rs:104(6 pcs)")
    print("10.Brown Bread-Rs:104(6 pcs)")
    print("11.Sandwich Bread-Rs:99(6 Pcs)")
    print("12.Treat Croissant-Rs:16(45g)")
    print("13.Gobbles Bar Cake-Rs:30(110g)")
    print("14.Plum Cake-Rs:175(450g)")
    print("15.Lava Cake-Rs:5(15g)")
    print("16.Choco Muffills-Rs:10(30g)")
    print("17.NOVO Cake Finger-Rs:15(25g)")
    print("18.Swiss Roll Cake-Rs:90(156g)")
    print("19.Tea Cake-Rs:175(250g)")
    print("20.Cup Cake-Rs:50(6 pcs)")
    chb=int(input("Enter how many products do u want to select : "))
    for i in range(chb):
        j=int(input("Enter choice : "))
        sumb=sumb+costb[j-1]
    totalsum.append(sumb)
    print("Total Amount for this category",sumb)
    a=int(input("Enter 1 to continue or 7 to Bill : "))
    if a==1:
        mainmenu()
    else:
        bill()
    
def drinks():
    costd=[36,65,28,35,115,86,34,106,104,50,35,40,336,329,186,145,685,80,400,360]
    sumd=0
    time.sleep(3)
    print("\n1.Diet Coke-Rs:36(300ml)")
    print("2.Original Coke-Rs:65(1.25L)")
    print("3.Sparkling Water(clube soda)-Rs:28(1.25L)")
    print("4.Black Pepsi-Rs:35(250ml)")
    print("5.Red Bull-Rs:115(250ml)")
    print("6.Cheese-Rs:386(750g)")
    print("7.Sprite-Rs:34(750Ml)")
    print("8.Condensed Milk-Rs:106(400g)")
    print("9.Bread-Rs:104(6 pcs)")
    print("10.soda-Rs:50(300ml-Can)")
    print("11.Mountain Dew-Rs:35(250ml)")
    print("12.Thums Up-Rs:40(300 ml-can)")
    print("13.Bourn Vita-Rs:336(1Kg)")
    print("14.Boost-Rs:329(750g)")
    print("15.Horlicks-Rs:186(450g)")
    print("16.Hot Chocolate-Rs:145(200g)")
    print("17.Taj Mahal-Rs:685(1Kg)")
    print("18.Bru Green Lable-Rs:80(150g)")
    print("19.Green Tea-Rs:400(500g)")
    print("20.3 Roses-Rs:360(500g)")
    chd=int(input("Enter how many products do u want to select : "))
    for i in range(chd):
        j=int(input("Enter choice : "))
        sumd=sumd+costd[j-1]
    totalsum.append(sumd)
    print("Total Amount for this category",sumd)
    a=int(input("Enter 1 to continue or 7 to Bill : "))
    if a==1:
        mainmenu()
    else:
        bill()
        
def Snacks():
    costs=[97,124,150,28,39,386,46,415,500,414,223,172,109,149,95,90,330,202,250,123]
    sums=0
    time.sleep(3)
    print("\n1.Masala Maggi-Rs:97(560g)")
    print("2.Yippee-Rs:124(10*67.5g(pack of 10))")
    print("3.Hakka Noodles-Rs:150(800g)")
    print("4.Cheese Macaroni Pazzta-Rs:28(70g)")
    print("5.Hot & Spicy Noodles-Rs:39(80g)")
    print("6.Cheese-Rs:386(750g)")
    print("7.Mood Masala-Rs:46(260g(pack of 4))")
    print("8.Muesli Breakfast Cereal-Rs:415(750g)")
    print("9.Con Flakes-Rs:500(1Kg)")
    print("10.Chocos-Rs:414(1.2Kg)")
    print("11.Oats-Rs:223(1.5Kg)")
    print("12.Chocos Fills-Rs:172(250g)")
    print("13.Frozen Green Peas-Rs:109(500g)")
    print("14.Frozen Sweet Corn-Rs:149(1Kg)")
    print("15.Whole Wheat Parota-Rs:95(400g-5 pcs)")
    print("16.French Fries-Rs:90(425g)")
    print("17.Chicken Nuggets-Rs:330(500g)")
    print("18.Smiles Crispy-Rs:202(750g)")
    print("19.Panner Paratha-Rs:250(400g-4 pcs)")
    print("20.Potato Bits-Rs:123(420g)")
    chs=int(input("Enter how many products do you want to select : "))
    for i in range(chs):
        j=int(input("Enter choice : "))
        sums=sums+costs[j-1]
    totalsum.append(sums)
    print("Total Amount for this category",sums)
    a=int(input("Enter 1 to continue or 7 to Bill : "))
    if a==1:
        mainmenu()
    else:
        bill()
        
def meat():
    coste=[49,100,99,393,479,96,555,319,290,559,481,899,799,149,184,239,160,550,330,195]
    sume=0
    print("\n1.Eggs-Rs:49(6 pcs)")
    print("2.Brown Eggs-Rs:100(6 pcs)")
    print("3.Chicken Without Skin-Rs:99(250g)")
    print("4.Chicken-Rs:393(1Kg)")
    print("5.Chicken Kema-Rs:479(1Kg)")
    print("6.Chicken Meat Loaf-Rs:96(100g)")
    print("7.Chicken MeatBalls-Rs:555(300g)")
    print("8.Chicken Finger-Rs:319(500g)")
    print("9.Sausags-Rs:290(500g)")
    print("10.Chicken Momos-Rs:559(pack of 2)")
    print("11.Mutton Seekh-Rs:481(500g)")
    print("12.Mutton Curry cut-Rs:899(1Kg)")
    print("13.Mutton Kema-Rs:799(500g)")
    print("14.Mutton Liver-Rs:149(250g)")
    print("15.Frozen Prawns-Rs:184(250g)")
    print("16.Fish cut-Rs:239(500g)")
    print("17.Tuna Fish-Rs:160(185g)")
    print("18.pork Belly Slice-Rs:550(200g)")
    print("19.Pork-Rs:330(250g)")
    print("20.Premium pork & Bacon-Rs:195(130g)")
    che=int(input("Enter how many products do you want to select : "))
    for i in range(che):
        j=int(input("Enter choice : "))
        sume=sume+coste[j-1]
    totalsum.append(sume)
    print("Total Amount for this category",sume)
    a=int(input("Enter 1 to continue or 7 to Bill : "))
    if a==1:
        mainmenu()
    else:
        bill()


def details():
    name=str(input("Enter your full name : "))
    number=str(input("Enter your phone number : "))
    if len(number)<10:
        print("Enter current mobile number")
        time.sleep(3)
        details()
    else:
        pincode=str(input("Enter your pincode: "))
        if len(pincode)<6:
            print("Enter current pincode")
            time.sleep(3)
            details()
        else:
            flat=str(input("Enter your Flat,House no,Building,company,Apartment : "))
            area=str(input("Enter your area :" ))
            landmark=str(input("Enter landmark : "))
            town=str(input("Enter your town : "))
            
def bill():
    details()
    date=str(input("Enter Today's data(dd/mm/yy) : "))
    billname=str(input("Enter the name to be on the bill : "))
    print("=================Total Bill===================")
    print("Date : ",date)
    print("Name : ",billname)
    print("==============================================")
    print(sum(totalsum))
    b=int(input("Press 2 to confirm your order or 1 to main menu or 8 to exit : "))
    if b==1:
        mainmenu()
    elif b==2:
        payment()
    else:
        exit()
        
def payment():    
    print("\n1.cash")
    print("2.card")
    print("\nEnter your choice : ")
    chcash=int(input())
    if(chcash==1):
        print("Your order delivered :)")
        time.sleep(5)
        cashamount=float(input("Enter the amount customer given : "))
        balance=cashamount-sum(totalsum)
        print("balance : ",balance)
        time.sleep(3)
        exit()
    elif chcash==2:
            cardnum=str(input("Enter your card number : "))
            cardname=str(input("Enter the name on the card : "))
            topayamount=int(input("Enter the amount you need to pay"))
            cardpin=int(input("Enter your pin number "))
            time.sleep(3)
            print("Amount piad Successfully!")
            print("Your order conformed...")
            a=int(input("Enter 1 to continue or 8 to Exit"))
            if a==1:
                mainmenu()
            else:
                exit()
            
def exit():
    print("\nThank You For Shopping...")

def mainmenu():
    print("\nSelect your category:")
    print("1.Fruits & Vegatables")
    print("2.Foodgrains,Oil & Masala")
    print("3.Bakery,Cakes & Dairy")
    print("4.Beverages")
    print("5.Snacks")
    print("6.Eggs,Meat & Fish")
    print("7.Bill")
    print("8.exit")
    ch1=int(input("select your choice : "))
    if ch1==1:
        fruits()
    elif ch1==2:
        Foodgrains()
    elif ch1==3:
        diary()
    elif ch1==4:
        drinks()
    elif ch1==5:
        Snacks()
    elif ch1==6:
        meat()
    elif ch1==7:
        bill()
    elif ch1==8:
        exit()
        
        
def signup():
    username = input("Enter username: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("details.txt", "w") as f:
             f.write(username + "\t" + hash1+"\t")
            
        f.close()
        print("You have registered successfully!")
        time.sleep(3)
        mainmenu()
    else:
        print("Password is not same as above! \n")
        time.sleep(3)
        Signup()
        
def login():
    username = input("Enter username: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("details.txt", "r") as f:
        stored_username, stored_pwd = f.read().split()
    f.close()
    if username == stored_username and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         time.sleep(3)
         mainmenu()
    else:
         print("Login failed! \n")
         time.sleep(3)
         login()
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")