import wave as wv
import math
import struct as strt

spfr=4096

nums=open("nums.txt","w")
f=wv.open("C:/Users/user/Desktop/what.wav","wb")
f.setparams((1,2,spfr,spfr*4,"NONE","not compressed"))


def ep(Hz,Vol,C,Length):
    sp=[]
    for l in range(Length):
        s=0
        c=C* 2**(l/spfr)
        if c>256: c=256
        c=C
        for n in range(24):
            s+=(0.5**(n*c))*math.sin(Hz/spfr*2*math.pi*n*l)*Vol
        s*=2**c
        #limitation:
        if abs(s)>1.5*Vol:
            s=abs(s)/s*1.5*Vol
        sp.append(s)
    for i in sp:
        f.writeframes(strt.pack('h',int(i)))

for i in range(512):
    ep(1,16384,(i/32+1),4096)
        
        
f.close()
