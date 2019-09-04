import numpy
import scipy.signal

a = numpy.array([[0,0,0,0,0,0],
                 [0,2,0,4,0,0],
                 [0,0,1,0,0,0]])
                 
b = numpy.array([[0,1,0],
                 [0,0,0]])

def convolve(a,b):
    out = scipy.signal.convolve2d(a,b)
    sX = abs(len(a)-len(b))
    sY = abs(len(a[0])-len(b[0]))
    ll = len(out)
    lll = len(out[0])
    return out[(ll-sX)/2:(ll+sX)/2+1,(lll-sY)/2:(lll+sY)/2+1]

def pad(mat, mod):    
    b1 = (-len(mat))%mod
    b2 = (-len(mat[0]))%mod
    return numpy.pad(mat,((0,b1),(0,b2)),'constant')
    
def pool(mat, siz):
    a = numpy.zeros(((len(mat)+siz-1)/siz,(len(mat[0])+siz-1)/siz))
    mat = pad(mat,siz)
    for i in range(len(mat[0])/siz):
        for j in range(len(mat)/siz):
            a[j][i] = numpy.max(mat[siz*j:siz*(j+1),siz*i:siz*(i+1)].flatten())
    return a

def buildNN():
    mapsNo = 3
    maps = []
    for i in range(mapsNo):
        maps.append([numpy.zeros([5,5]),1])
    layer = numpy.zeros((mapsNo*12*12),10)
    return [maps,layer]
    
def feedForward(NN,labeledImage):
    label,image = labeledImage
    maps, layer = NN
    mapA,mapB,mapC = maps
    convolutionA = convolve(image,mapA).flatten()
    convolutionB = convolve(image,mapB).flatten()
    convolutionC = convolve(image,mapC).flatten()
    
    out = numpy.hstack(convolutionA,convolutionB)
    out = numpy.hstack(out,convolutionC)
    
    nextr = numpy.dot(layer,out)
    
                 
c = convolve(a,b)
print c
print pool(c,4)



    
print buildNN()
