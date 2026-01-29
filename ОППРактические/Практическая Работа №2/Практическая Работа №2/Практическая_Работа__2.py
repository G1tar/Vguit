import math

# ¹5

x = -15.246
y = 4.642*10**(-2)
z = 21
 # s =-182.038

s = math.log(y**(-math.sqrt(abs(x))))*(x-(y/2)) + math.sin(math.atan(z))**2
print (round(s,3))

# ¹10

x = 3.981*(10**-2)
y = -1.625 * (10**3)
z = 0.512
 # s = 1.26185

mod1 = 2**(-x)
a = abs(y) ** (1/4)
mod2 = math.sqrt(x + a)
mod3 = ((math.e**(x-(1/math.sin(z))))**(1/3))

s = mod1*mod2*mod3

print (round(s,5))
