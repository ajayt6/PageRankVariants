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
A = np.matrix(hlm)
E = np.zeros(A.shape)
E[:] = .02
A = beta * A + ((1-beta) * E)
r = np.zeros((A.shape[0],1))

r[:] = .02
#r = r.T
print(r.shape)
prev_r = r

for i in range(1,100):
    print("iteration: \n",i)
    r = np.dot(A, r)
    #check if converged
    if (prev_r==r).all():
        break
    prev_r = r

print ("Final:\n", r)
print ("sum", np.sum(r))
