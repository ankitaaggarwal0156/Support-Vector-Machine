from cvxopt import matrix, solvers
import numpy as np

def svm(X, Y):
    m = len(X)
    P = matrix(np.dot(Y, Y.T) * X)
    q = matrix(np.ones(m) * -1)
    G = matrix(np.diag(np.ones(m) * -1))
    h = matrix(np.zeros(m))
    A = np.reshape((Y.T), (1, m))
    b = matrix([0.0])
    A = A.astype(np.double)
    A = matrix(A)

    sol = solvers.qp(P, q, G, h, A, b)
    alpha = sol['x']
    #print "alpha", alpha
    return alpha


def calculateW(a, L, S):
    sumW = 0.0
    for i in range(len(S)):
        sumW += a[i] * L[i] * S[i]
    return sumW


def supportVectors(a, s):
    svList = []
    SValpha = []
    index = []
    for i in range(len(a)):
        if (a[i] > 0.001):
            SValpha.append(a[i])
            index.append(i)
    for j in index:
        svList.append(s[j])
    return svList, SValpha, index


def calculateb(sv, l, w):
    w = w.T
    w = np.reshape(w, (1, 6))

    return (1 / l) - np.dot(w, sv)


def Read_File():
    list_of_coordinates = []
    label1 = []
    Data_list = []
    with open("./nonlinsep.txt", "r") as fo:
        for line in fo:
            list_of_coordinates.append(line)
    fo.close()
    for line in list_of_coordinates:
        list_of_items_in_line = line.split(",")
        Data_list.append(
            (float(list_of_items_in_line[0]), float(list_of_items_in_line[1])))
        label1.append(float(list_of_items_in_line[2]))

    samples = np.array(Data_list, dtype=np.float)
    samples = samples.astype(np.double)

    for item in label1:
        float(item)
    labels = np.array(label1)
    labels = np.reshape(labels, (100, 1))
    return samples, labels


def kernel(X):
    Q = []
    r = []
    for i in range(len(X)):
        r = [1, (X[i, 0]) ** 2, (X[i, 1]) ** 2, np.sqrt(2) * X[i, 0], np.sqrt(2) * X[i, 1],
             np.sqrt(2) * X[i, 0] * X[i, 1]]
        Q.append(r)
        
    Q = np.array(Q)
    print "X in Z dimension:\n ", Q
    print "---------------------------------------------"
    Z = np.inner(Q, Q)
    return Q, Z
  
    
samples, labels = Read_File()
q, k = kernel(samples)
a = svm(k, labels)

sv, sVa, i = supportVectors(a, q)
weight = calculateW(a, labels, q)

b = calculateb(sv[0], labels[i[0]], weight)
print "--------------------------------------------------------------------\n"
for i in range(len(sv)):
    print "support vector",i+1,":", sv[i]
    print " alpha",i+1,":",sVa[i]
print "--------------------------------------------------------------------\n"
print "weight vector in Z: \n", weight
print "bias point = ", b
