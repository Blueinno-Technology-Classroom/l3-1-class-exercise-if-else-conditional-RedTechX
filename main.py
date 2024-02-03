##################################################
'''
Q1:

1 = True
0 = False
a: 1
b: 0
c: 1
d: 0
e: 1
f: 0
g: 1
h: 1
i: 1
'''

##################################################
'''
Q2:
a: y>0
b: z != 0 
c: abs(y) > abs(z)
d: z >= 0
e: abs(x - y) < abs(z - y)
f: z % 2 = 1
g: x % 2 = 0
h: y % z = 0
i: 0 < y < 10
j: x < 0 < z or x > 0 > z
k: (x = 7 and y % 2 = 1) or (y = 7 and x % 2 = 1)
'''

##################################################
'''
Q3:

for example, if you input the num
ber 2, 4, 8, 10, 14, and etc, it 
will output "odd number" while th
ey are actually even. the Else co
ntinuation has an extra indent. t
hat solves the weird problem or g
litch.
'''
number = int(input('Give me a number: '))

if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 6.")
    else:
        print("Odd number.")

'should be:'

if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 6.")
else:
    print("Odd number.")


##################################################
