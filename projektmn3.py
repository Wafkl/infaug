import numpy as np
import math
import matplotlib.pyplot as plt


#####Zad. 1.
h = 0.1
t = np.arange(75,110,h)
r = 0.4
lam = r
K = 100000

x = np.zeros(t.shape[0])
x[0] = 75
z = np.zeros(t.shape[0])
z[0] = 75

#model gompertza
for i in range(1,t.shape[0]):
    x[i] = x[i-1] + h*(r*x[i-1]*math.log(K/x[i-1])) 

plt.plot(t,x,label = 'model Gompertza')
plt.ylabel('objetosc guza')
plt.xlabel('czas')

#model Verhulsta
for i in range(1,t.shape[0]):
    z[i] = z[i-1] + h*lam*(1-(z[i-1]/K))*z[i-1] + (1/2)*(h**2)*((lam**2)*z[i-1]*(1-(z[i-1]/K))*(1-((2*z[i-1])/K)))
    
plt.plot(t,z,label = 'model Verhulsta')
plt.legend()
plt.show()


######Zad. 2.

h = 0.001
t = np.arange(0,15,h) 

#a

N1 = np.zeros(t.shape[0])
N2 = np.zeros(t.shape[0])

N1[0] = 3
N2[0] = 4

e1 = 1.25 #epsilon 1
g1 = 0.5 #gamma 1
h1 = 0.1
e2 = 0.5
g2 = 0.2
h2 = 0.2

for i in range(1,t.shape[0]):
    N1[i] = N1[i-1] + h*(e1-g1*(h1*N1[i-1]+h2*N2[i-1]))*N1[i-1]
    N2[i] = N2[i-1] + h*(e2-g2*(h1*N1[i-1]+h2*N2[i-1]))*N2[i-1]

    
plt.plot(t,N1,label = 'populacja 1')
plt.plot(t,N2,label = 'populacja 2')
plt.title('Wykres podpunkt #a')
plt.xlabel('czas')
plt.ylabel('liczebnosc')
plt.legend()
plt.show()

'''
Na wykresie do podpunktu #a widać, że obie populacje rosną do okreslonego punktu. Po osiagnieciu danej wartosci obie funkcje sa stale.
Populacja 2 jest wieksza do pewnego momentu po czym populacja 1 ja przerasta.
'''

#b

N1 = np.zeros(t.shape[0])
N2 = np.zeros(t.shape[0])

N1[0] = 3
N2[0] = 4

e1 = 5 #epsilon 1
g1 = 4 #gamma 1
h1 = 1
e2 = 5
g2 = 8
h2 = 4

for i in range(1,t.shape[0]):
    N1[i] = N1[i-1] + h*(e1-g1*(h1*N1[i-1]+h2*N2[i-1]))*N1[i-1]
    N2[i] = N2[i-1] + h*(e2-g2*(h1*N1[i-1]+h2*N2[i-1]))*N2[i-1]

    
plt.plot(t,N1,label = 'populacja 1')
plt.plot(t,N2,label = 'populacja 2')
plt.title('Wykres podpunkt #b')
plt.xlabel('czas')
plt.ylabel('liczebnosc')
plt.legend()
plt.show()

'''
Na wykresie do podpunktu #b widać, że obie populacje maleją, w tym populacja 2 zbiega do zera, a populacja 1 odbija maleje, odbija
sie od pewnej wartosci, wzrasta i osiaga stala wartosc.
''''

#c,d,e
e1 = 0.8
g1 = 1
h1 = 0.3
e2 = 0.4
g2 = 0.5
h2 = 0.4

N1c = np.zeros(t.shape[0])
N2c = np.zeros(t.shape[0])
N1d = np.zeros(t.shape[0])
N2d = np.zeros(t.shape[0])
N1e = np.zeros(t.shape[0])
N2e = np.zeros(t.shape[0])

N1c[0] = 4
N2c[0] = 8
N1d[0] = 8
N2d[0] = 8
N1e[0] = 12
N2e[0] = 8


for i in range(1,t.shape[0]):
    N1c[i] = N1c[i-1] + h*(e1-g1*(h1*N1c[i-1]+h2*N2c[i-1]))*N1c[i-1]
    N2c[i] = N2c[i-1] + h*(e2-g2*(h1*N1c[i-1]+h2*N2c[i-1]))*N2c[i-1]
    N1d[i] = N1d[i-1] + h*(e1-g1*(h1*N1d[i-1]+h2*N2d[i-1]))*N1d[i-1]
    N2d[i] = N2d[i-1] + h*(e2-g2*(h1*N1d[i-1]+h2*N2d[i-1]))*N2d[i-1]
    N1e[i] = N1e[i-1] + h*(e1-g1*(h1*N1e[i-1]+h2*N2e[i-1]))*N1e[i-1]
    N2e[i] = N2e[i-1] + h*(e2-g2*(h1*N1e[i-1]+h2*N2e[i-1]))*N2e[i-1]
    
    

x = np.arange(0,13,0.5)
y = np.arange(0,13,0.5)
X, Y = np.meshgrid(x,y)   
dX = np.zeros(X.shape)
dY = np.zeros(Y.shape) 

for i in range(X.shape[0]):
    for j in range(Y.shape[0]):
        dX[i,j] = (e1-g1*(h1*X[i,j]+h2*Y[i,j]))*X[i,j]
        dY[i,j] = (e2-g2*(h1*X[i,j]+h2*Y[i,j]))*Y[i,j]
    
    
plt.figure(figsize = (6,6))
plt.quiver(X,Y,dX,dY,color = 'm')
plt.plot(N1c,N2c, label = '(N1c,N2c) = (4,8)')    
plt.plot(N1d,N2d, label = '(N1d,N2d) = (8,8)') 
plt.plot(N1e,N2e, label = '(N1e,N2e) = (12,8)') 
plt.title('Portret fazowy')
plt.xlabel('populacja 1')
plt.ylabel('populacja 2')
plt.legend()
plt.show()

'''
Na portrecie fazowym widać, że im większa liczebnosc poczatkowa populacji 1 (N1), tym gwałtowniejszy spadek liczebnosci obu populacji. 
Dla populacji z podpunktu e N1e i N2e można zaobserwować najwieksze tempo zmian liczebnosci spowodowany najwiekszym warunkiem poczatkowym N1 równym 12.
'''
