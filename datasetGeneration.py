#keeping function taht returns random number as separate for flexibility

import numpy as np
from random import randint

def retRandom(a,b):
    return randint(a, b)

def generate(n,volLimit):
    #generate n lists. each list will serve as a column. For this:
    #1)convert to numpy array
    #2)take transpose

    hyperlinkMatrix = None
    volMatrix = None
    hyperlinkMatrixUnweighted = None


    for i in range(0,n):

        #should have minimum one outlink to avoid danglink link problem and maximum of n-1 outlinks since link to itself is not considered
        numLinks = retRandom(1,n-1)


        linkWeight = 1/numLinks


        #generate a set with numLinks elements. this will serve as set that contains all the nodes that is pointed to by this node
        #  it will not have element i
        columnList = [0] * n
        volList = [0]*n
        columnListUnweighted = [0] * n
        excludeList = [i]
        for j in range(numLinks):

            while True:
                fillPos = retRandom(0,n-1)
                if fillPos not in excludeList:
                    excludeList.append(fillPos)
                    break

            columnList[fillPos] = linkWeight
            columnListUnweighted[fillPos] = 1
            volList[fillPos] = retRandom(0,volLimit)

        #normalize the volList
        volSum = 0.0
        for j in range(len(volList)):
            volSum = volSum + volList[j]

        for j in range(len(volList)):
            volList[j] = volList[j] / volSum

        columnList = np.array(columnList)
        columnList = np.transpose(columnList)
        columnList.shape = (1,columnList.shape[0])

        columnListUnweighted = np.array(columnListUnweighted)
        columnListUnweighted = np.transpose(columnListUnweighted)
        columnListUnweighted.shape = (1, columnListUnweighted.shape[0])

        volList = np.transpose(np.array(volList))
        volList.shape = (1,volList.shape[0])

        #print(columnList.shape)
        if i == 0:
            hyperlinkMatrix = columnList
            hyperlinkMatrixUnweighted = columnListUnweighted
            volMatrix = volList
        else:
            hyperlinkMatrix = np.concatenate( (hyperlinkMatrix,columnList ))
            hyperlinkMatrixUnweighted = np.concatenate((hyperlinkMatrixUnweighted, columnListUnweighted))
            volMatrix = np.concatenate((volMatrix, volList))

    hyperlinkMatrix = np.transpose(hyperlinkMatrix)
    hyperlinkMatrixUnweighted = np.transpose(hyperlinkMatrixUnweighted)
    volMatrix = np.transpose(volMatrix)

    #find number of inlinks and outlinks to each node
    inlinkDict = {}
    outlinkDict = {}
    for i in range(n):
        numOut = 0
        for j in range(n):
            numOut = numOut + hyperlinkMatrixUnweighted[j][i]
        outlinkDict[i] = numOut

    for i in range(n):
        numIn = 0
        for j in range(n):
            numIn = numIn + hyperlinkMatrixUnweighted[i][j]
        inlinkDict[i] = numIn

    #compute both inlink weight as well as outlink weight
    for i in range(n):
        for j in range(n):
            if hyperlinkMatrix[i][j] > 0:
                sumOfInLinks = 0.0
                for k in range(n):
                    sumOfInLinks = sumOfInLinks + hyperlinkMatrixUnweighted[j][k]
                sumOfOutLinks = 0.0
                for k in range(n):
                    sumOfOutLinks = sumOfOutLinks + hyperlinkMatrixUnweighted[k][j]

                hyperlinkMatrix[i][j] = 1.0 * (inlinkDict[i]/sumOfInLinks) * (outlinkDict[i]/sumOfOutLinks)
    '''
    print(hyperlinkMatrix)
    print(hyperlinkMatrixUnweighted)
    print(volMatrix)
    print(hyperlinkMatrix.shape)
    '''

    np.savetxt("hyperlinkMatrix.csv", hyperlinkMatrix, delimiter=",")
    np.savetxt("hyperlinkMatrixUnweighted.csv", hyperlinkMatrixUnweighted, delimiter=",")
    np.savetxt("volMatrix.csv", volMatrix, delimiter=",")


    for filename in ["hyperlinkMatrix.csv","hyperlinkMatrixUnweighted.csv","volMatrix.csv"]:
        hlm = np.loadtxt(open(filename, "rb"), delimiter=",")
        print(hlm)
        print(hlm.shape)




if __name__ == '__main__':
    n=5
    generate(n,200)