from numpy import matrix
from numpy import random
import numpy as np

def test(a,bias,weight,data) :
    error = 0
    lr = 0.6
    d = data[4]
    data = np.delete(data, 4).T
    print 'Test[%d]'%a
    if (weight*data+bias) >= 0 : 
        yn = 1
    elif (weight*data+bias) < 0 :
        yn = 0
    er = d - yn
    if er == 1:
        weight = weight+(lr*er*(data.T))
        print 'Error : 1\n'
        print weight
        error+=1
    elif er == 0:
        print 'Error : 0\n'
        print weight

    return weight

def main() :
    bias = random.uniform(-1000000,1000000)
    if (bias >= 0) :
        weights = random.uniform(-bias,bias, size=(1,4))
    elif (bias < 0) :
        weights = random.uniform(bias,-bias, size=(1,4))

    f = open('data.txt', 'r')
    data = []
    for line in f.readlines() :
        data.append(line.strip('\n').split('\t'))
    
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            data[i][j] = float(data[i][j])
    print data
    for b in range(0, 1000):
        for a in range(0, len(data)) :
            weights = test(b,bias,weights,matrix(data[a]).T)

    print 'Last Modified Weights :\n'
    print weights

if __name__ == '__main__' :
    main()


