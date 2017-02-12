% Vector Calculus
% Nicolás Guarín-Zapata
    email: nguarinz@eafit.edu.co
    github: nicoguaro
% February 9, 2017


------------------

# Curvilinear coordinates example: Cylindrical Coordinates


<iframe
    width="1280" height="720"
    src="./img/polar_coords.html"
    frameborder="0"
    allowfullscreen
    class="centObj"></iframe>


------------------

# Coordinate systems

Two common examples of curvilinear coordinates are

### Cylindrical coordinates

$$\begin{align}
x =& \rho \cos\phi\\
y =& \rho \sin\phi\\
z =& z
\end{align}$$

### Spherical coordinates

$$\begin{align}
x =& r \sin\theta \cos\phi\\
y =& r \sin\theta \sin\phi\\
z =& r \cos\theta
\end{align}$$

------------------

# Transformations

We can write the position vector as

$$d\mathbf{r} = \sum\limits_{i=1}^3 \frac{\partial \mathbf{r}}{\partial u_i} du_i \, .$$

The factor $\partial \mathbf{r}/\partial u_i$ is a non-unitary vector, we can
introduce a normalized based $\hat{\mathbf{e}}_i$

$$\frac{\partial \mathbf{r}}{\partial u_i} = h_i \hat{\mathbf{e}}_i $$

where

$$\left| \frac{\partial \mathbf{r}}{\partial u_i}\right| = h_i$$

is the [**scale factor**](https://en.wikipedia.org/wiki/Curvilinear_coordinates#Relation_to_Lam.C3.A9_coefficients).

------------------

# Jacobian

We can rewrite the transformation, in components, as

$$d x_i = \sum_j \frac{\partial x_i}{\partial u_j} du_j = \sum_j J_{ij} du_j \, ,$$

where $J_{ij} = \partial x_i/\partial u_j$ are the components of the [Jacobian
matrix](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant).

And, its determinant represents the (local) change in volume of the
transformation

$$ |J| = h_1 h_2 h_3\, .$$

------------------

# Line, surface and volume differentials

We can rewrite the transformation as

$$ d\mathbf{r} = \sum_{i=1} h_i \hat{\mathbf{e}}_i du_i = \sum_{i=1}^3 d\mathbf{l}_i \, ,$$

where $d\mathbf{l}_i  = h_i \hat{\mathbf{e}}_i du_i$ is the _line differential_
along the coordinate $u_i$.

We can define the _surface differentials_ as the vectors that are perpendicular
to the differential areas according to the right hand convention, namely

$$d\mathbf{S}_i = d\mathbf{l}_j \times d\mathbf{l}_k =
  h_j h_k \hat{\mathbf{e}}_i du_j du_k = \hat{\mathbf{e}}_i dS_i$$

And the volume differential is given by the volume of the curvilinear parallelepiped
defined by the line differentials, i.e.

$$dV = d\mathbf{l}_1 \cdot (d\mathbf{l}_2 \times \mathbf{l}_3) =
       h_1 h_2 h_3 du_1 du_2 du_3 \, .$$

------------------

# References

- Alonso Sepúlveda Soto. Física matemática. Ciencia y Tecnología. Universidad
  de Antioquia, 2009.

- Wikipedia contributors. ["Curvilinear coordinates."](https://en.wikipedia.org/wiki/Curvilinear_coordinates)
  Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, Retrieved: 3 Feb. 2017.
