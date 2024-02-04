import numpy as np
import matplotlib.pyplot as plt


####zad 1
e0 = 0.01
s0 = 1-e0
i0 = 0
r0 = 0

b = 1 #beta zakazen
s = 1 #sigma inkubacji
g = 0.1 #gamma ozdrowien

h = 0.001
t = np.arange(0,60,h)

N = np.zeros((t.shape[0],4))
N[0,0] += s0
N[0,1] += e0
N[0,2] += i0
N[0,3] += r0


for i in range(1,t.shape[0]):
    F10 = h*((-b)*N[i-1,0]*N[i-1,2])
    F20 = h*( -b*(N[i-1,0] + (1/2)*F10)*(N[i-1,2]+(1/2)*F10 ))
    F30 = h*(-b*(N[i-1,0] + (1/2)*F20)*(N[i-1,2]+(1/2)*F20 ))
    F40 = h*(-b*(N[i-1,0] + F30)*(N[i-1,2] + F30 ))
    N[i,0] += N[i-1,0] + (1/6)*( F10   +  2*F20 + 2*F30 + F40)
    F11 = h * ( b * N[i-1,2] * N[i-1,0] - s*N[i-1,1]) 
    F21 = h * ( b * (N[i-1,2]+(1/2)*F11) * (N[i-1,0]+(1/2)*F11) - s*(N[i-1,1]+(1/2)*F11))
    F31 = h * ( b * (N[i-1,2]+(1/2)*F21) * (N[i-1,0]+(1/2)*F21) - s*(N[i-1,1]+(1/2)*F21))
    F41 = h * ( b * (N[i-1,2]+F31) * (N[i-1,0]+F31) - s*(N[i-1,1]+F31))
    N[i,1] += N[i-1,1] + (1/6)*( F11  + 2*F21 + 2*F31 + F41)
    F12 = h * (s*N[i-1,1] - g*N[i-1,2])
    F22 = h * (s*(N[i-1,1]+(1/2)*F12) - g*(N[i-1,2]+(1/2)*F12))
    F32 = h * (s*(N[i-1,1]+(1/2)*F22) - g*(N[i-1,2]+(1/2)*F22))
    F42 = h * (s*(N[i-1,1]+F32) - g*(N[i-1,2]+F32))
    N[i,2] += N[i-1,2] + (1/6)*( F12  + 2*F22 + 2*F32 + F42)
    F13 = h * g*N[i-1,2]
    F23 = h * g*(N[i-1,2] + (1/2)*F13)
    F33 = h * g*(N[i-1,2] + (1/2)*F23)
    F43 = h * g*(N[i-1,2] + F33)
    N[i,3] += N[i-1,3] + (1/6)*( F13  + 2*F23 + 2*F33 + F43)
    
    
plt.plot(t, N[:,0], label = 's')
plt.plot(t, N[:,1], label = 'e')
plt.plot(t, N[:,2], label = 'i')
plt.plot(t, N[:,3], label = 'r')
plt.xlabel('czas')
plt.ylabel('ilosc ludzi')
plt.title('wykres do Zad. 1.')
plt.legend()
plt.show()


####zad 2   
#beta zmniejszone do 1/2 
e0 = 0.01
s0 = 1-e0
i0 = 0
r0 = 0

b = 0.5 #beta zakazen
s = 1 #sigma inkubacji
g = 0.1 #gamma ozdrowien

h = 0.001
t = np.arange(0,60,h)

N = np.zeros((t.shape[0],4))
N[0,0] += s0
N[0,1] += e0
N[0,2] += i0
N[0,3] += r0


for i in range(1,t.shape[0]):
    F10 = h*((-b)*N[i-1,0]*N[i-1,2])
    F20 = h*( -b*(N[i-1,0] + (1/2)*F10)*(N[i-1,2]+(1/2)*F10 ))
    F30 = h*(-b*(N[i-1,0] + (1/2)*F20)*(N[i-1,2]+(1/2)*F20 ))
    F40 = h*(-b*(N[i-1,0] + F30)*(N[i-1,2] + F30 ))
    N[i,0] += N[i-1,0] + (1/6)*( F10   +  2*F20 + 2*F30 + F40)
    F11 = h * ( b * N[i-1,2] * N[i-1,0] - s*N[i-1,1]) 
    F21 = h * ( b * (N[i-1,2]+(1/2)*F11) * (N[i-1,0]+(1/2)*F11) - s*(N[i-1,1]+(1/2)*F11))
    F31 = h * ( b * (N[i-1,2]+(1/2)*F21) * (N[i-1,0]+(1/2)*F21) - s*(N[i-1,1]+(1/2)*F21))
    F41 = h * ( b * (N[i-1,2]+F31) * (N[i-1,0]+F31) - s*(N[i-1,1]+F31))
    N[i,1] += N[i-1,1] + (1/6)*( F11  + 2*F21 + 2*F31 + F41)
    F12 = h * (s*N[i-1,1] - g*N[i-1,2])
    F22 = h * (s*(N[i-1,1]+(1/2)*F12) - g*(N[i-1,2]+(1/2)*F12))
    F32 = h * (s*(N[i-1,1]+(1/2)*F22) - g*(N[i-1,2]+(1/2)*F22))
    F42 = h * (s*(N[i-1,1]+F32) - g*(N[i-1,2]+F32))
    N[i,2] += N[i-1,2] + (1/6)*( F12  + 2*F22 + 2*F32 + F42)
    F13 = h * g*N[i-1,2]
    F23 = h * g*(N[i-1,2] + (1/2)*F13)
    F33 = h * g*(N[i-1,2] + (1/2)*F23)
    F43 = h * g*(N[i-1,2] + F33)
    N[i,3] += N[i-1,3] + (1/6)*( F13  + 2*F23 + 2*F33 + F43)
    
    
plt.plot(t, N[:,0], label = 's')
plt.plot(t, N[:,1], label = 'e')
plt.plot(t, N[:,2], label = 'i')
plt.plot(t, N[:,3], label = 'r')
plt.xlabel('czas')
plt.ylabel('ilosc ludzi')
plt.title('wykres do Zad. 2.')
plt.legend()
plt.show()   

'''
ODP do Zad. 2. :
    W wyniku zmniejszenia współczynnika beta tempo na początku pandemii jest mniejsze niz w zadaniu pierwszym.
    e(t) oraz i(t) po zmniejszeniu wspolczynnikaa beta nigdy nie osiagaja tak duzej wartossci maksymalnej jak w zad. 1.
''' 


#####zad 3
#R0 = 4,95 dla parametróW z zadania drugiego: beta = 0.5, gamma = 0.1, s0 = 0.99
plt.plot(t, N[:,0], label = 's')
plt.plot(t, N[:,1], label = 'e')
plt.plot(t, N[:,2], label = 'i')
plt.plot(t, N[:,3], label = 'r')
plt.xlabel('czas')
plt.ylabel('ilosc ludzi')
plt.title('wykres #a do Zad. 3. dla R0 = 4,95')
plt.legend()
plt.show() 


#R0 = 0,72
e0 = 0.1
s0 = 1-e0
i0 = 0
r0 = 0

b = 0.4 #beta zakazen
s = 1 #sigma inkubacji
g = 0.5 #gamma ozdrowien

h = 0.001
t = np.arange(0,60,h)

N = np.zeros((t.shape[0],4))
N[0,0] += s0
N[0,1] += e0
N[0,2] += i0
N[0,3] += r0


for i in range(1,t.shape[0]):
    F10 = h*((-b)*N[i-1,0]*N[i-1,2])
    F20 = h*( -b*(N[i-1,0] + (1/2)*F10)*(N[i-1,2]+(1/2)*F10 ))
    F30 = h*(-b*(N[i-1,0] + (1/2)*F20)*(N[i-1,2]+(1/2)*F20 ))
    F40 = h*(-b*(N[i-1,0] + F30)*(N[i-1,2] + F30 ))
    N[i,0] += N[i-1,0] + (1/6)*( F10   +  2*F20 + 2*F30 + F40)
    F11 = h * ( b * N[i-1,2] * N[i-1,0] - s*N[i-1,1]) 
    F21 = h * ( b * (N[i-1,2]+(1/2)*F11) * (N[i-1,0]+(1/2)*F11) - s*(N[i-1,1]+(1/2)*F11))
    F31 = h * ( b * (N[i-1,2]+(1/2)*F21) * (N[i-1,0]+(1/2)*F21) - s*(N[i-1,1]+(1/2)*F21))
    F41 = h * ( b * (N[i-1,2]+F31) * (N[i-1,0]+F31) - s*(N[i-1,1]+F31))
    N[i,1] += N[i-1,1] + (1/6)*( F11  + 2*F21 + 2*F31 + F41)
    F12 = h * (s*N[i-1,1] - g*N[i-1,2])
    F22 = h * (s*(N[i-1,1]+(1/2)*F12) - g*(N[i-1,2]+(1/2)*F12))
    F32 = h * (s*(N[i-1,1]+(1/2)*F22) - g*(N[i-1,2]+(1/2)*F22))
    F42 = h * (s*(N[i-1,1]+F32) - g*(N[i-1,2]+F32))
    N[i,2] += N[i-1,2] + (1/6)*( F12  + 2*F22 + 2*F32 + F42)
    F13 = h * g*N[i-1,2]
    F23 = h * g*(N[i-1,2] + (1/2)*F13)
    F33 = h * g*(N[i-1,2] + (1/2)*F23)
    F43 = h * g*(N[i-1,2] + F33)
    N[i,3] += N[i-1,3] + (1/6)*( F13  + 2*F23 + 2*F33 + F43)
    
    
plt.plot(t, N[:,0], label = 's')
plt.plot(t, N[:,1], label = 'e')
plt.plot(t, N[:,2], label = 'i')
plt.plot(t, N[:,3], label = 'r')
plt.xlabel('czas')
plt.ylabel('ilosc ludzi')
plt.title('wykres #b do Zad. 3. dla R0 = 0.72')
plt.legend()
plt.show()


'''
żeby R0 < 1 , beta < gamma co oznacza ze wspolczynnik zakazen jest mniejszy od
 wspolczynnika wyzdrowien i w takim przypadku wybierajac wartosc s(0) z przedzialu 0-1, w modelu nie dojdzie do rozwoju epidemii
 jak widac na wykresie #b.
R0 > 1 jesli beta > gamma czyli wspolczynnik zakazen jest wiekszy od wspolczynnika wyzdrowien tak jak to widac na wykresie #a.
 
'''  
