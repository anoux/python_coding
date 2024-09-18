sh = input('Enter hours:' )
sr = input('Enter rate:' )

"""since the "dangerous lines are the 
ones that convert the inputs to 
float type, this is where the try
and except must be added"""

try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, please enter only numeric input')

print('something is not working')

if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
    
print('Pay: ', xp)