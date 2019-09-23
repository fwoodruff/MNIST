# MNIST
Image recognition program using MNIST labelled images.

A list of images is converted into an array containing vectors of pixel brightnesses: __p__<sub>i</sub> where each array index i corresponds to a different image.

Each image __p__<sub>i</sub> has a corresponding label __q__<sub>i</sub>, a unit vector of dimension n, where n is the number of labels. Values of __q__<sub>i</sub> belong to a set of n orthogonal vectors that map to each label.

Now that we have a way to interpret images and labels as vectors, we need a function that takes 'image' __p__ to 'label' __q__.

One option is **q** = **W**.**p** where **W** is a matrix,

but let's define:

norm(__x__) ≡ __x__/|__x__|,

**ξ**(**M**,**R**; **p**<sub>i</sub>) ≡ norm(e<sup>norm(__R__.e<sup>__M__.__p__<sub>i</sub></sup>)</sup>),

where **R** and **M** are matrices.

**ξ** has the desired properties:
* it is differentiable;
* it also maps between vectors;
* it has more non-degenerate parameters that can be varied independently than **W**.

For some values of **R** and **M**, **ξ** will map images **p**<sub>i</sub> to vectors very close to **q**<sub>i</sub>. This happens when **q**<sub>i</sub>.**ξ**(**M**,**R**; **p**<sub>i</sub>) ≈ 1.

So the goal is to maximise f = Σ<sub>i</sub> log(__q__<sub>i</sub>.**ξ**(__p__<sub>i</sub>)) by varying **R** and **M**.

I calculated expressions for  ∂f<sub>i</sub>/∂**M** and ∂f<sub>i</sub>/∂**R** and used this program to perform many small gradients descents for each image.

Having now optimised **R** and **M**, this program applies **ξ** to new test images and can label them with 98.7% accuracy.
