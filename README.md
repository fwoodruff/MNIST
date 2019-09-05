# MNIST
Neural Network for MNIST labelled image recognition

This is a project I made in 2018 to build a neural network from scratch.

A list of images is converted into an array of vector of pixel brightnesses __p__<sub>i</sub> where each i corresponds to a different image.

Each __q__<sub>i</sub> is a unit vector of dimension n, where n is the number of labels.

Possible values of __q__ belong to a set of n orthogonal vectors that map to each label.

We define:

norm(__x__) ≡ __x__/|__x__|

ξ(__p__<sub>i</sub>) ≡ norm( e<sup>norm(__R__.e<sup>__M__.__p__<sub>i</sub></sup>)</sup>)

where __R__ and __M__ are matrices. Let's also define a vector **z** where each element maps to some element of {__M__, __R__} bijectively.

For some value of **z**, ξ will map image __p__<sub>i</sub> to a vector very close to __q__<sub>i</sub>. We can say our 'neural network has labelled the image'.

So the goal is to maximise f = Σ<sub>i</sub> log(__q__<sub>i</sub>.ξ(__p__<sub>i</sub>)) by varying __z__.

This program then solves df/d**z** = 0 using the Newton-Raphson Method.
