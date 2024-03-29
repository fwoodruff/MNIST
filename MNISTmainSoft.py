import MNISTreader
import os 
import numpy
import random
import cPickle as pickle

base = 10
imagev = 28*28
random.seed(0)
dir_path = os.path.dirname(os.path.realpath(__file__))
fname = 'Desktop/NMISTnn.pkl'
random.seed(1)

trainingIG = list(MNISTreader.read(path = dir_path))
testingIG = MNISTreader.read(path = dir_path)

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
def load_object(filename):
    with open(filename, 'rb') as input:
        return pickle.load(input)
        
def feed(weights,biases,inputs):
    x = numpy.dot(inputs,weights)+biases
    expz = numpy.exp(x - max(x))
    return expz/numpy.sum(expz)
def flatten(image):
    image = numpy.array(image)
    image = image/256.
    return image.flatten()

def error(z,label):
    return -numpy.log(z[label])


def test(neuralNetwork,labeledImage):
    label,image=labeledImage
    puts = flatten(image)
    
    for layer in neuralNetwork:
        weights, biases = layer
        puts = feed(weights,biases,puts)
    
    #MNISTreader.show((numpy.argmax(puts),image))
    return label,numpy.argmax(puts)
    

def Delta(out,weight="none",delta="none",target="none"):
    if(weight=="none"):
        a = numpy.zeros(len(out))
        a[target] = 1
        return out - a
    else:
        mm = numpy.dot(weight,delta)
        rr = numpy.diag(out)-numpy.outer(out,out)
        return numpy.dot(mm,rr)


def train(neuralNetwork,labeledImage, gamma = 0.5):
    label,image=labeledImage
    inputs = flatten(image)
    xyz=[inputs]
    for layer in neuralNetwork:
        weights, biases = layer
        inputs = feed(weights,biases,inputs)
        xyz.append(inputs)
    if(random.random()<0.01):
        print error(xyz[-1],label)
        #print NN[-1][0]
        #print label,numpy.argmax(xyz[-1])
        #print xyz
        
    Dd = Delta(xyz[-1],target=label)
    dEdw = numpy.outer(xyz[-2],Dd)
    neuralNetwork[-1][0] = neuralNetwork[-1][0] - gamma*dEdw
    neuralNetwork[-1][1] = neuralNetwork[-1][1] - gamma*Dd
    for i in range(len(xyz)-2,0,-1):
        Dd = Delta(xyz[i],weight=neuralNetwork[i][0],delta=Dd)
       
        dEdw = numpy.outer(xyz[i-1],Dd)
        neuralNetwork[i-1][0] = neuralNetwork[i-1][0] - gamma*dEdw
        neuralNetwork[i-1][1] = neuralNetwork[i-1][1] - gamma*Dd
    
def randomWeights(forward,back):
    arr = numpy.zeros((forward,back))
    invwgt = 1/(back)
    for i in range(forward):
        for j in range(back):
            arr[i][j] = random.uniform(-invwgt,invwgt)
    return arr
def randomOffset(forward):
    arr = numpy.zeros(forward)
    for i in range(forward):
        arr[i] = random.uniform(-1,1)
    return arr
def randomLayer(forward,back):
    return [randomWeights(forward,back),randomOffset(back)]
    
def buildNN(nodesPerLayer):
    layers = []
    for i in range(1,len(nodesPerLayer)):
        layers.append(randomLayer(nodesPerLayer[i-1],nodesPerLayer[i])) # may be [i-1]                
    return layers
    

NN = buildNN([imagev,500,200,40,base])



if(not os.path.isfile(fname)):
    for i in range(40):
        for iml in trainingIG:
            train(NN,iml)
        save_object(NN, fname)
NN = load_object(fname)

def showBad():
    correct = 0
    incorrect = 0
    for im in testingIG:
        a,b = test(NN,im)
        
        if (a!=b):
            incorrect +=1
            if (incorrect<10):
                MNISTreader.show(im)
        else:
            correct +=1
    print "correct:", correct
    print "incorrect:", incorrect
    print "success rate:", correct*1./(incorrect+correct)
    
def showSome(N):
    for im in range(N):
        labIm = next(testingIG)
        a,b =  test(NN,labIm)
        MNISTreader.show((a,b,labIm[1]))
        
showSome(44)
