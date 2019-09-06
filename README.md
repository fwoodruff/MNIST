# MNIST
Image recognition program using MNIST labelled images.

A list of images is converted into an array containing vectors of pixel brightnesses: __p__<sub>i</sub> where each i corresponds to a different image.

Each __q__<sub>i</sub> is a unit vector of dimension n, where n is the number of labels.

Possible values of __q__ belong to a set of n orthogonal vectors that map to each label.

We define:

norm(__x__) ≡ __x__/|__x__|

ξ(__p__<sub>i</sub>) ≡ norm( e<sup>norm(__R__.e<sup>__M__.__p__<sub>i</sub></sup>)</sup>)

where __R__ and __M__ are matrices.

For some values of **R** and **M**, ξ will map images __p__<sub>i</sub> to vectors very close to __q__<sub>i</sub>. This happens when **q**<sub>i</sub>.ξ(**p**<sub>i</sub>) ≈ 1.

So the goal is to maximise f = Σ<sub>i</sub> log(__q__<sub>i</sub>.ξ(__p__<sub>i</sub>)) by varying __z__.

This program then solves df/d**z** = 0 using the Newton-Raphson Method, where I first calculated dξ/d**M** and dξ/d**R** with pen and paper.

Having found **z**, this program applies ξ to new test images and can label them with 98.7% accuracy.
