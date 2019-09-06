# MNIST
Image recognition program using MNIST labelled images.

A list of images is converted into an array containing vectors of pixel brightnesses: __p__<sub>i</sub> where each array index i corresponds to a different image.

Each image __p__<sub>i</sub> has a corresponding label __q__<sub>i</sub>, a unit vector of dimension n, where n is the number of labels. Values of __q__<sub>i</sub> belong to a set of n orthogonal vectors that map to each label.

We need a function that takes image __p__ to label __q__.

We define:

norm(__x__) ≡ __x__/|__x__|,

ξ(**M**,**R**; **p**<sub>i</sub>) ≡ norm( e<sup>norm(__R__.e<sup>__M__.__p__<sub>i</sub></sup>)</sup>)

where **R** and **M** are matrices.

ξ is not special but has the desired properties:
* it is differentiable;
* it maps between vectors;
* it has lots of non-degenerate parameters that can be varied independently.

For some values of **R** and **M**, ξ will map images **p**<sub>i</sub> to vectors very close to **q**<sub>i</sub>. This happens when **q**<sub>i</sub>.ξ(**M**,**R**; **p**<sub>i</sub>) ≈ 1.

So the goal is to maximise f = Σ<sub>i</sub> log(__q__<sub>i</sub>.ξ(__p__<sub>i</sub>)) by varying **R** and **M**.

I calculated expressions for  ∂f<sub>i</sub>/∂**M** and ∂f<sub>i</sub>/∂**R** and used this program to perform a number of rounds of the Newton-Raphson Method for each image.

Having now optimised **R** and **M**, this program applies ξ to new test images and can label them with 98.7% accuracy.
