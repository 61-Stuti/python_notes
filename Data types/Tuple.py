T=('physics','chemistry', 1, 2)
print(T[1:3])
print(T[0:3:2])
T=T+(3,)
print(T)

T1=('a','a','b','c')
print(T1.count('a'))

ticket_price=[('APPL',200), ('GOOG',400),('MSFT',600)]
for item,price in ticket_price:
    print(price + (0.1*price))



    