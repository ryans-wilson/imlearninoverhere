def computepay (hours, rate):
    if hours <= 40:
        pay = float(hours) * float(rate)
        return pay
    else:
        othours = hours - 40
        otrate = rate * 1.5
        pay = 40 * float(rate) + float(othours) * float (otrate)
        return pay
shrs = input("Enter Hours:")
srate = input("Enter Rate:")
try:
    fr = float(srate)
    fh = float(shrs)
except:
    print ('Error: Please Enter a Numerical Input')
    quit()
comp = computepay (fh, fr)
print ('Pay', comp)