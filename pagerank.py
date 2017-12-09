##Standard PageRank implementation
##Requires a square matrix
import numpy as np
maxerr = .0001
hlm = np.loadtxt(open("./hyperlinkMatrix.csv", "rb"), delimiter=",")
A = np.matrix(hlm)
rsums = np.array(A.sum(1))[:,0]
n = A.shape[0]
# bool array of sink states
sink = rsums==0
# Compute pagerank r until we converge
ro, r = np.zeros(n), np.ones(n)
while np.sum(np.abs(r-ro)) > maxerr:
    ro = r.copy()
    # calculate each pagerank at a time
    for i in range(0,n):
        # inlinks of state i
        A_i = np.matrix(A[:,i].todense())[:,0]
        # account for sink states
        D_i = sink / float(n)
        # account for teleportation to state i
        Ei = np.ones(n) / float(n)
        r[i] = ro.dot( Ai*s + Di*s + Ei*(1-s) )

# return normalized pagerank
print( r/float(sum(r)))
