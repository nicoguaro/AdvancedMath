% Ordinary differential equations
% Nicolás Guarín-Zapata
    email: nguarinz@eafit.edu.co
    github: nicoguaro
% August 24, 2017



------------------

# Ordinary differential equations

An ordinary differential equation (ODE) is an equation of the form

$$F(z, y, y', y'', \cdots, y^{(n)}) = 0\, ,$$

where $F$ is a function of the independent variable $z$,
dependent variable $y(z)$, and its derivatives.

------------------

# Classification: Number of variables

How many independent variables does the equation have?

\begin{align}
&L\frac{d^2 Q}{dt^2} + R\frac{dQ}{dt} + \frac{1}{C}Q = E  &\text{(ODE)}\\
&\frac{\partial u}{\partial t} =\alpha \frac{\partial^2 u}{\partial x^2}  &\text{(PDE)}\\
&\frac{\partial u}{\partial t} =\frac{\partial^2 u}{\partial r^2} +
    \frac{1}{r} \frac{\partial u}{\partial r} +
    \frac{1}{r^2}\frac{\partial^2 u}{\partial \theta^2}  &\text{(PDE)}
\end{align}

------------------

# Classification: Order

What is the order of the higher derivative?

\begin{align}
&\frac{\partial u}{\partial t} =\alpha \frac{\partial^2 u}{\partial x^2}  &\text{(Second order)}\\
&\frac{d^2 u}{d t^2} = f(t)  &\text{(Second order)}\\
&\frac{d^{(3)} y}{dx^3} + 2 e^x \frac{d^2 y}{d x^2} +
    y\frac{d y}{dx} = x^4  &\text{(Third order)}
\end{align}

------------------

# Classification: Homogeneity

The equation is homogeneous if the right-hand-side of

$$F(z, y, y', y'', \cdots, y^{(n)}) = G(z)\, ,$$

is zero.

------------------

# Classification: Linearity

The equation

$$F(z, y, y', y'', \cdots, y^{(n)}) = 0\, ,$$

is linear if $F$ is a linear function of the variables $y, y', \cdots, y^{(n)}$.

\begin{align}
&\frac{\partial^2 u}{\partial t^2} = e^{-t} \frac{\partial^2 u}{\partial x^2}
  + \sin t  &\text{(Linear)}\\
&\frac{d^2 \theta}{d t^2} = \frac{g}{l}\sin\theta  &\text{(Non-linear)}
\end{align}

------------------

# Classification: Type of coefficients

In the case of linear equations, we analyze the coefficients of the linear
combination. Are these coefficients constant or functions of $x$?

\begin{align}
&a\frac{d^2 u}{d t^2} + b \frac{d u}{d t} + c u  = 0 &\text{(Constant coefficients)}\\
&\frac{d}{dx}\left(x\frac{d w}{dx}\right) = -\omega^2 w  &\text{(Variable coefficients)}
\end{align}


------------------

# Examples: Free fall
<table>
<tr>
<td>
In this case, gravity is the only force acting upon an object. The equation
reads
$$y'' =g = \text{const}$$
</td>
<td>
<video width="640" height="480" autoplay loop>
   <source src="./img/free_fall.mp4" type="video/mp4">
   Your browser does not support the video tag.
</video>
</td>
</tr>
</table>

------------------

# Examples: Parachute falling
<table>
<tr>
<td>
This case is similar to the previous one, but there is air resistance (drag).
The drag force is normally as a constant multiplied by the square of the speed
$$m\frac{d^2 y}{dt^2} = mg - b\left(\frac{dy}{dt}\right)^2$$
</td>
<td>
<video width="640" height="480" autoplay loop>
   <source src="./img/drag_fall.mp4" type="video/mp4">
   Your browser does not support the video tag.
</video>
</td>
</tr>
</table>

------------------

# Examples: Pendulum
<table>
<tr>
<td>
<img src="./img/PenduloTmg.gif"
    width=300
    class="centObj">
</td>
<td>
A pendulum is a weight suspended from a pivot that can swing freely. The
equation for a simple pendulum is

$$L\theta'' + g\sin\theta = 0$$
</td>
</tr>
</table>

------------------

# References

- H. Hochstadt. Differential equations: a modern approach.
  Courier Dover Publications, 1975.

- Erwin Kreyszig. Advanced engineering mathematics. John Wiley & Sons, 2010.

- Ruryk, 2011. Oscilatting pendulum. Retrieved from:
  https://commons.wikimedia.org/wiki/File:PenduloTmg.gif
