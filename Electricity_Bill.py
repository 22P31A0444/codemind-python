u = int(input())
if(u<199):
    uc=1.20
elif(u>=200 and u<400):
    uc=1.40
elif(u>=400 and u<600):
    uc=1.60
elif(u>=600 and u<800):
    uc=1.80
elif(u>=800):
    uc=2.00
b=u*uc
s=0
if(b>400):
    s=b*0.15
t=b+s
print(f"Units Consumed: {u}")
print(f"Cost per Unit: {uc:.2f}")
print(f"Bill: {b:.2f}")
print(f"Surcharge: {s:.2f}")
print(f"Total Amount: {t:.2f}")