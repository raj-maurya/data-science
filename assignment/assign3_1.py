hrs = raw_input("Enter Hours:")
h = float(hrs)

rat  = (raw_input("Enter rate:"))
rate = float(rat)
times = 1.5

if(h>40):
    h1 = h-40
    p = 40
else:
    h1 = h-40
    p=h

g_pay = p*rate + h1*times*rate

print g_pay
