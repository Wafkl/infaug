ygreki = [1]
xksy = 0.1
ik = 0 #ilosc krokow
print('x = 0','      y = 1              ' ,'     G(x,y) = 0')

def f(x,y):
    return((3*(x**7)) + (2*(y**5)) - (x**3) + (y**3) - 3)


def p(y):
    return 10*(y**4) + 3*(y**2)


while xksy <= 10:
    mety = [ygreki[ik]]
    for i in range(0,4):
        a = mety[i]-((f(xksy,mety[i]))/(p(mety[i])))
        mety.append(a)
        if len(mety) == 5:
            ygreki.append(mety[4])
            print('x = ',xksy, '   y = ', mety[4], '  G(x,y) = ', f(xksy,mety[4]))
    xksy += 0.1
    xksy = round(xksy,2)
    ik += 1    
    
