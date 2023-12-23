import sounddevice as sd
import numpy as np
from numpy import pi, sin
fs = 44100
dt = 1/fs

y = 1.5 #zmienna tempa
t1 = np.arange(0 ,y ,dt)
t2 = np.arange(0, (1/2)*y, dt)
t4 = np.arange(0, (1/4)*y, dt)
t75 = np.arange(0, (3/4)*y, dt)

#z nut na keyboard
#ton podstawowy A4 = 440Hz
few = 659.26 #E5
fdw = 587.33 #D5
fc = 523.25 #C5
fh = 493.88
fe = 329.63
fa = 440.00
sil = 0

#poszczególne nuty
ew4 = sin(2*pi*few*t4)
ew75 = sin(2*pi*few*t75)
e4 = sin(2*pi*fe*t4)
dw2 = sin(2*pi*fdw*t2)
dw4 = sin(2*pi*fdw*t4)
dw75 = sin(2*pi*fdw*t75)
c2 = sin(2*pi*fc*t2)
c4 = sin(2*pi*fc*t4)
h2 = sin(2*pi*fh*t2)
h4 = sin(2*pi*fh*t4)
a4 = sin(2*pi*fa*t4)
a75 = sin(2*pi*fa*t75)
sil2 = sin(2*pi*sil*t2) #cisza

#mizerna cicha
x = np.concatenate((ew4,ew4,ew4,dw2,dw4,c4,c4,c4,h2,e4,a4,a4,h4,c4,h4,a4,ew75,dw75,sil2,ew4,ew4,ew4,dw2,dw4,c4,c4,c4,h2,e4,a4,a4,h4,c2,h4,a75,a75,sil2,ew4,ew4,ew4,dw2,dw4,c4,c4,c4,h2,e4,a4,a4,h4,c4,h4,a4,ew75,dw75,sil2,ew4,ew4,ew4,dw2,dw4,c4,c4,c4,h2,e4,a4,a4,h4,c2,h4,a75,a75))
sd.play(x,fs)
