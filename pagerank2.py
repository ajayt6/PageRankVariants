##Standard PageRank implementation
##Requires a square matrix
import numpy as np
import scipy as sc
import pandas as pd
from fractions import Fraction
# keep it clean and tidy

# we have 50 webpages and probability of landing to each one is 1/50
#(defaultProbability)
dp = Fraction(1,50)
# penalty
beta = 0.7
maxerr = .0001
hlm = np.loadtxt(open("./hyperlinkMatrix.csv", "rb"), delimiter=",")
vol = np.loadtxt(open("./volMatrix.csv", "rb"), delimiter=",")
hlmu = np.loadtxt(open("./hyperlinkMatrixUnweighted.csv", "rb"), delimiter=",")


print("1.PR")
print("2.WPR")
print("3.PR-VOL")
print("4.WPR-VOL")

choice = input("Choose an option:")

A=None

if choice == '1':
    #load the unweighted matrix
    A = np.matrix(hlmu)
    pass
elif choice == '2':
    #load the wighted matrix
    A = np.matrix(hlm)
    pass
elif choice == '3':
    #load the unweighted matrix and squash in vol values
    for i in range(hlmu.shape[0]):
        for j in range(hlmu.shape[1]):
            hlmu[i][j] = hlmu[i][j] * vol[i][j]
    A = np.matrix(hlmu)

    pass
elif choice == '4':
    # load the weighted matrix and squash in vol values
    for i in range(hlm.shape[0]):
        for j in range(hlm.shape[1]):
            hlm[i][j] = hlm[i][j] * vol[i][j]
    A = np.matrix(hlm)

    pass
else:
    print("invalid choice. exiting in 5")
    import time
    time.sleep(5)
    exit()


E = np.zeros(A.shape)
E[:] = .02
#A = beta * A + ((1-beta) * E)
r = np.zeros((A.shape[0],1))
print(np.sum(A,axis=0))
r[:] = .02
#r = r.T
print(r.shape)
prev_r = r

for i in range(1,100):
    print("iteration: \n",i)
    r = np.dot(A, r)
    #check if converged
    if (prev_r-r<maxerr).all():
        break
    prev_r = r

print ("Final:\n", r)
print ("sum", np.sum(r))
