import joblib

brand= ['Acer', 'Alienware', 'Apple', 'Asus', 'Dell', 'HP', 'HP ','Lenovo', 'Microsoft']
pro_model = ['i3', 'i5', 'i7', 'other']
graphic_brand = ['amd', 'intel', 'nvidia']
os_name = ['linux', 'mac', 'windows']

price = joblib.load("model5")


comp = input("Enter The Company Name : ")
comp = brand.index(comp)

ram = int(input("Enter The RAM Amount : "))

stype = int(input("Does it has SSD or Not answer in 1/0 :"))

storage = int(input("Enter The Storage Amount in GB: "))

screen = float(input("Enter the screen size in inches : "))

pro = input("Enter The Processor model : ")
pro = pro_model.index(pro)

speed = float(input("Enter the clock Speed : "))


graphic = input("Enter The Graphic Card Brand : ")
graphic = graphic_brand.index(graphic)

gsize = int(input("Enter The Graphic Card Size : "))

os = input("Enter Operating System : ")
os = os_name.index(os)

mass = float(input("Enter The mass of the Laptop in kg : "))
print()

a = price.predict([[comp,ram,stype,storage,screen,pro,speed,graphic,gsize,os,mass]])


print(f"The Price of this Particular laptop is : {a/1.8} INR")
