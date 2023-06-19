import random


c=3+4j
b=[]
print(type(c))

g='gautam'
b='gandotra'


m=100
y=200

li=['dfs','fdsf','fd','fsdfs','fsdfdsf','sfsdfsdf','sfsdfsdrwerwerwe','gdfgewefsg','gsgfsdg']

print(li)

#ui=input('enter in string u want to find in list')
if('fd' in li):
    print('yes it is in list')
else:
    print('nope not in list')

print(li[::-1])

print(len(li[-3]))

li[0:2]=['gautam','gandotra']
print(li)

if(m<y):
    
    print('m is greater than y')
    
else:
    print('y is greater than x')
print(bool(c))
print(bool(b))
print(g.capitalize()+' , '+b)
print('my name is \"mr\" gandotra')
print(g+' '+b)
print(g.replace('g', 'ma'))

print(g.split('a'))

print(random.randrange(30344))



import sympy as sp


x = sp.Symbol('x')
a = sp.Symbol('a')
b = sp.Symbol('b')
c = sp.Symbol('c')


quad_formula = sp.Eq(x, sp.simplify((-b + sp.sqrt(b**2 - 4*a*c))/(2*a)))


sp.pprint(quad_formula)


gautam=[]
print(len(gautam))