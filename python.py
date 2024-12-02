x,y,z = ['Bouraghda', 'Mohamed', 'Elhadi']
print(x,y,z)

x,y,z = 10, 'Python' , True
print(x,y,z)
print('-'*30)
# dic = {'k1':'Java', "k2":20 , 'k3': 'Volvo'}
# for k,v in dic:
#     print(k + ' => ' + v)
a = {'one':1, 'tow':2, 'three':3}
b = {'four':4, 'five':5}
print(a|b) # => {'one': 1, 'tow': 2, 'three': 3, 'four': 4, 'five': 5}

print('-'*30) # => ------------------------------

print('Hello world'.removeprefix('Hel')) # => lo world
print('Hello world'.removesuffix('ld'))  # => Hello wor

print('-'*30) # => ------------------------------
import math
print (math.gcd(12,20,40)) # => 4 القاسم المشترك الأصغر
print(math.lcm(4,8,5))     # => 40 المضاعف المشترك الأصغر

