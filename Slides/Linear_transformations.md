% Linear Tranformations and Eigenvalues/Eigenvectors
% Nicolás Guarín-Zapata
    email: nguarinz@eafit.edu.co
    github: nicoguaro
% July 26, 2017


------------------

# Linear Transformation

A linear map (also called a linear mapping, linear transformation) is a mapping $V \rightarrow W$ between two vector spaces that preserves the operations of addition and scalar multiplication.

Let $V$ and $W$ be vector spaces over the same [field](https://en.wikipedia.org/wiki/Field_(mathematics)) $K$. A function $f : V \rightarrow W$ is said to be a _linear map_ if for any two vectors $x$ and $y$ in $V$ and any scalar $α$ in $K$, the following two conditions are satisfied:

- $f(\mathbf{x}+\mathbf{y}) = f(\mathbf{x})+f(\mathbf{y})\quad \text{(Additivity)}$
- $f(\alpha \mathbf{x}) = \alpha f(\mathbf{x})\quad \text{(Homogeneity)}$

------------------

# Video lecture: Linear transformations

<iframe
    width="1280" height="720"
    src="https://www.youtube.com/embed/kYB8IZa5AuE?rel=0"
    frameborder="0"
    allowfullscreen
    class="centObj"></iframe>

------------------

# Applet: Linear transformations

<iframe
    width="1280" height="720"
    src="http://math.mercyhurst.edu/~lwilliams/Applets/algebra/linearTransformations.php"
    frameborder="0"
    allowfullscreen
    class="centObj"></iframe>

------------------

# Examples of linear transformation matrices

In two-dimensional space $\mathbb{R}^2$ linear maps are described by 2 × 2 real matrices. These are some examples:

- rotation by 90 degrees counterclockwise:

$$\mathbf{A}=\begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$$

- rotation by angle ''θ'' counterclockwise: $$\mathbf{A}=\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
- reflection against the ''x'' axis: $$\mathbf{A}=\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$$
- reflection against the ''y'' axis: $$\mathbf{A}=\begin{pmatrix}-1 & 0\\ 0 & 1\end{pmatrix}$$
- scaling by 2 in all directions: $$\mathbf{A}=\begin{pmatrix}2 & 0\\ 0 & 2\end{pmatrix}$$
- horizontal shear mapping: $$\mathbf{A}=\begin{pmatrix}1 & m\\ 0 & 1\end{pmatrix}$$
- squeeze mapping: $$\mathbf{A}=\begin{pmatrix}k & 0\\ 0 & 1/k\end{pmatrix}$$
- projection onto the ''y'' axis: $$\mathbf{A}=\begin{pmatrix}0 & 0\\ 0 & 1\end{pmatrix}.$$

------------------

# Eigenvalues and Eigenvectors

An eigenvector or characteristic vector of a linear transformation is a non-zero vector whose direction does not change when that linear transformation is applied to it. More formally, if $T$ is a linear transformation from a vector space $V$ over a field $F$ into itself and $v$ is a vector in $V$ that is not the zero vector, then $v$ is an eigenvector of $T$ if $T(v)$ is a scalar multiple of $v$. This condition can be written as the equation

$$T ( v ) = λ v ,$$

where $λ$ is a scalar in the field $F$, known as the eigenvalue, characteristic value, or characteristic root associated with the eigenvector $v$.

------------------

<img src="./img/Mona_Lisa_eigenvector_grid.png"
    width=800
    class="centObj">

In this [shear mapping](https://en.wikipedia.org/wiki/Shear_mapping) the red arrow changes direction but the blue arrow does not. The blue arrow is an eigenvector of this shear mapping because it doesn't change direction, and since its length is unchanged, its eigenvalue is 1.

------------------
# References

- Grant Sanderson. [Essence of linear algebra.](http://www.3blue1brown.com/essence-of-linear-algebra/), 2016. Retrieved February 1, 2017.
- Lauren Kelly Williams. [Linear Tranformations Applet](http://math.mercyhurst.edu/~lwilliams/Applets/LinearTransformations.html), 2016. Retrieved February 1, 2017.
- Wikipedia contributors. [Eigenvalues and eigenvectors](https://en.wikipedia.org/w/index.php?title=Eigenvalues_and_eigenvectors&oldid=763060013). Retrieved February 1, 2017.
