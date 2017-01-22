def computepay(h,r):
    if(h>40):
        h1 = h-40
        h2 = h1+0.5*h1
        p = 40

    else:
        h1 = h-40
        p=h
    g_pay = p*r + h2*r
    return g_pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)

p = computepay(h,r)
print p
