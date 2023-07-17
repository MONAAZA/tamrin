#Excersie sheet for Math. and Num. Methods Exam
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#defining the function
def integrand(z):
    #constants
    omegam=0.27
    omegal=0.73
    
    f=1./((1.+z)*(omegam*(1+z)**3.+omegal)**0.5)
    return f

def looktime(zprime):
    
    H0=67*1e5/3.086e24*3.1536e7*1e9
    ltime=integrate.quad(integrand, 0.0, zprime)
    
    look=ltime[0]
    look/=H0
    
    return look

z=10
look=[]
redshift=[]
while(z>0.0):
    look.append(looktime(z))   
    redshift.append(z)
    z-=0.01
for i in range (len(look)):
    print(redshift[i],look[i])
plt.plot(redshift,look)
    