#This program is written by Sanjana Doss. CB.EN.U4CCE19049
#Networking Academy ID: 1024012124



#importing necessary libs
import re
import ipaddress

lst = [] #list for storing inputs
validlst = [] #list for storing ip address in different formats

def validIPv4(lst):
    """regex for ip address validation"""
    regex = '^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$'
    for i in range(0,10):
        if(re.search(regex, lst[i])):
            print("Valid Ipv4 address")
            binary = bin(int(ipaddress.IPv4Address(lst[i])))
            octal = oct(int(ipaddress.IPv4Address(lst[i])))
            hexa = hex(int(ipaddress.IPv4Address(lst[i])))
            validlst.append([lst[i],binary,octal,hexa])
        else:
            print("Not Valid")

#asking inputs from the user and storing it in an empty list, lst = []
for i in range(0,10):
    x = input("Enter the IP address %d: " %(i+1))
    lst.append(x)

validIPv4(lst)
#print(validlst)

with open('conversion.txt' , 'w') as f:
      for ip in validlst:
          f.writelines("%s\n" %ip)

d = {0:'first',1:'second',2:'third',3:'fourth',4:'fifth',5:'sixth',6:'seventh',7:'eighth',8:'ninth',9:'tenth'}    
with open('conversion.txt', 'r') as f:
     for i,line in enumerate(f):
        print(f"The {d[i]} IP address in Decimal, Binary, Octal and Hexadecimal format is {line}") 