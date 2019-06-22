import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


#Pd (Probability of Detection) is calcuated by marcum Q function with Pfa (Probability of False Alarm) and required SNR

#https://stackoverflow.com/questions/43983050/octave-ncx2cdf-undefined-error
#the non-central chi-square distribution is simply defined as 1 minus the Marcum Q function. 

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ncx2.html#scipy.stats.ncx2
#https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
# check parameters
#nc = lambda = a**2
#df = degrees of freedom = k
#ncxcdf =  1-Q( sqrt(lambda),  sqrt(x), k/2)
#Q(a, b , m)
#a = sqrt(lambda)  nc = lambda = a**2
#b = sqrt(x)       x  = b**2

def marcumq(a, b, m):
    nc=a**2
    x=b**2
    df=m*2
    #return 1-scipy.stats.ncx2(2*m,a**2).cdf(b**2)
    return 1-scipy.stats.ncx2(df,nc).cdf(x)

def probabilityOfDetectionBySNRandPfa(SNR, Pfa):
    a = np.sqrt(2.0 * np.power(10,(.1*SNR))); 
    b = np.sqrt(-2.0 * np.log(Pfa));   
    return marcumq(a, b, 1)

#print (marcumq (a, b, 1))    
snr=13.2
pfa=1e-6
#ans 0.9021226397841027
print (probabilityOfDetectionBySNRandPfa(snr, pfa))

