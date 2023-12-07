'''
Zad.1. Korzysając z algorytmu wyprowadzonego na ćwiczeniac napisać program do obliczania naturalnej funkcji sklejanej sześciennej S, która spełnia
następujące warunki interpolacyjne:
ti 1.0 2.0 3.5 5.0 6.0 9.0 9.5
yi 3.0 1.0 4.0 0.0 0.5 −2.0 −3.0
gdzie ti są węzłami, a yi odpowiedającymi im wartościami. Narysować wykres
funkcji S.
'''
import numpy as np
import matplotlib.pyplot as pl
from scipy.interpolate import CubicSpline
data = np.array([[1.0,3.0],[2.0,1.0],[3.5,4.0],[5.0,0.0],[6.0,0.5],[9.0,-2.0],[9.5,-3.0]])

n = len(data) - 1 #6
N = n

h = np.zeros(n)
b = np.zeros(n)
u = np.zeros(n-1)
v = np.zeros(n-1)
z = np.zeros(n+1)


for i in range(n):
    h[i] = data[i+1,0] - data[i,0]
    
u[0] = 2*(h[0]+h[1])

for i in range(n):
    b[i] = (6/(h[i]))*(data[i+1,1]-data[i,1])
    
v[0] = b[1]-b[0]
    
for i in range(1,n-1):
    u[i] = 2*(h[i]+h[i+1])-(((h[i])**2)/u[i-1])
    
for i in range(1,n-1):
    v[i] = b[i+1]-b[i] - (((h[i])*(v[i-1]))/u[i-1])
    
for i in range(n-1,0,-1):
    z[i] = (1/u[i-1])*(v[i-1]-((h[i])*(z[i+1])))

def A(i):
    return ((1/(6*h[i]))*(z[i+1]-z[i]))


def B(i):
    return ((z[i])/2)


def C(i):
    return ((-(h[i]/6)*(z[i+1]+2*z[i])) + ((1/h[i])*(data[i+1,1]-data[i,1])))


x = np.linspace(0,10,100)    
   

def Spline(data):
    S_Cubic = np.zeros(x.shape[0])
    S_Cubic += (data[0,1] + (x - data[0,0])*(C(0)+((x-data[0,0])*(B(0)+((x-data[0,0])*A(0))))))*(x <= data[0,0])
    for i in range(0,len(data)-1):
        S_Cubic += (data[i,1] + (x - data[i,0])*(C(i)+((x-data[i,0])*(B(i)+((x-data[i,0])*A(i))))))*(x <= data[i+1,0])*(x > data[i,0])
    S_Cubic += (data[6,1] + (x - data[6,0])*(C(5)+((x-data[6,0])*(B(6)+((x-data[6,0])*A(5))))))*(x > data[6,0])
    pl.plot(x,S_Cubic, label = 'f sklejana 3 st')



'''
Zad.2. Na jednym rysunku przedstawić wykresy funkcji sklejanej sześciennej
z poprzedniego zadania, funkcji sklejanej stopnia 1 (z ostatnich ćwiczeń) oraz
wielomianu interpolującego otrzymanego ze wzoru Lagrange’a dla danych z
Zad.1. Na wykresie powinna znaleźć się legenda z oznaczeniem każdej z
funkcji.
'''

#Lagrange
lagrange_poly = np.ones((N, x.shape[0]))
for i in range(N):
    for j in range(N):
        if j!=i:
            lagrange_poly[i,:] *= (x-data[j,0])/(data[i,0]-data[j,0])
            
            
p = np.zeros(x.shape[0])
for n in range(N):
    a = (lagrange_poly[n, :] * data[n, 1])
    if a.all() <= 5:
        p += lagrange_poly[n, :] * data[n+1, 1]

        
#funkcja sklejana 1st
def ps(data,n):
    ai = []
    bi = []
    S_linear = np.zeros(x.shape[0])
    
    for i in range(n+1):
        ai.append((data[i,1]-data[i+1,1])/(data[i,0]-data[i+1,0]))
        bi.append(data[i,1]-ai[i]*data[i,0])
    S_linear+= (ai[0]*x + bi[0])*(x<=data[0,0])
    for i in range(n+1):
        S_linear+= (ai[i]*x + bi[i])*(x<=data[i+1,0])*(x > data[i,0])
    S_linear+= (ai[5]*x + bi[5])*(x>data[6,0])
    pl.plot(x,S_linear, label = 'funkcja sklejana 1.stp')
 

#wykresy do zadania drugiego
Spline(data)
ps(data,n)
pl.plot(x,p, label = 'lagrnange')
pl.legend()
pl.title('Wykres 2')
pl.show()



'''
Zad.3. Porównać wykresy uzyskanej funkcji sklejanej sześciennej oraz
funkcji CubicSpline z modułu scipy.interpolate dla danych z Zad.1. Czy
wykresy się pokrywają? Jeśli nie, to dlaczego?
'''

#3.a
cs = CubicSpline(data[:,0], data[:,1])
cs = cs(x)
Spline(data)
pl.plot(x,cs, label = 'Cubic Spline')
pl.legend()
pl.title('Wykres 3.a')
pl.show()
#3.b
cs = CubicSpline(data[:,0], data[:,1],bc_type = 'natural')
cs = cs(x)
Spline(data)
pl.plot(x,cs, label = 'Cubic Spline')
pl.legend()
pl.title('Wykres 3.b')
pl.show()


#Odp do zadania 3.:
'''
Wykres z użyciem funkcji znajdujacej sie w module scipy.interpolate nie pokrywa sie z wykresem
narysowanym z uzyciem funkcji sklejanej 3. stopnia Spline (widać to na wykresie 3.a),
ponieważ domyslnie druga pochodna w pierwszym i ostatnim wezle nie sa rowne 0, wartosc dla tych 
pochodnych nie jest tu z gory narzucana. Jesli zmienimy warunek bc_type z "not_a_knot" na "natural"
wtedy, tak samo jak w naszym zalozeniu, ze nasza funkcja sklejana jest naturalna, druga pochodna
dla pierwszego i ostatniego wezla przyjmuja wartosc 0 i wykresy
sie pokrywaja (widac to na wykresie 3.b).
'''
