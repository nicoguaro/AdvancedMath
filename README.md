# Advanced Mathematics for Engineers

This is a repository with material for the course Advanced Mathematics for Engineers. The program of the course is located [here](./program.md). A _commented_ list of
references can be found [here](./references.md).

## Contents

- Notebooks: This folder contains several Jupyter Notebooks intended to teach SymPy
    - [SymPy in 10 minutes](http://nbviewer.jupyter.org/github/nicoguaro/AdvancedMath/blob/master/Notebooks/SymPy%20in%2010%20minutes.ipynb)
    - [Linear Algebra in SymPy](http://nbviewer.jupyter.org/github/nicoguaro/AdvancedMath/blob/master/Notebooks/Linear%20Algebra.ipynb)
    - [Vector calculus and coordinate systems](http://nbviewer.jupyter.org/github/nicoguaro/AdvancedMath/blob/master/Notebooks/Vector_calculus.ipynb)
    - [Ordinary differential equations in SymPy](http://nbviewer.jupyter.org/github/nicoguaro/AdvancedMath/blob/master/Notebooks/ODE.ipynb)
    - [Laplace Transform](http://nbviewer.jupyter.org/github/nicoguaro/AdvancedMath/blob/master/Notebooks/Laplace_transform.ipynb)
    - [Orthonormal basis and Fourier Analysis](https://github.com/nicoguaro/AdvancedMath/blob/master/Notebooks/Fourier_analysis.ipynb)

- Slides
    - [Course presentation](https://cdn.rawgit.com/nicoguaro/AdvancedMath/cddc9b94/Slides/Course_presentation.html)
    - [Linear transformations](https://cdn.rawgit.com/nicoguaro/AdvancedMath/5fa8ad68/Slides/Linear_transformations.html)
    - [Vector calculus and coordinate systems](https://cdn.rawgit.com/nicoguaro/AdvancedMath/597051f1/Slides/Vector_calculus.html)
    - [Orthonormal basis and Fourier Analysis](https://cdn.rawgit.com/nicoguaro/AdvancedMath/37e5cf49/Slides/Fourier_analysis.html)

## Downloading the Tutorial Materials
You can clone the repo using:

    git clone https://github.com/nicoguaro/AdvancedMath

or directly use the download option from GitHub.


## Installation Instructions

To display the slides a browser is needed. They have been tested in Mozilla Firefox and Google Chrome, but any _modern_ browser should work. For instruction on how to compile the source codes into the html files see the following section.

This repository also includes [Jupyter Notebooks](https://jupyter.org/). To run these you will need [Python](https://www.python.org/) and some packages:

- [IPython](http://ipython.org/), a command shell for interactive computing in multiple programming languages that offers introspection, rich media, shell syntax, tab completion, and history.
- [NumPy](http://www.numpy.org/), an extension to the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays.
- [SciPy](http://www.scipy.org/), an open source Python library used for scientific computing and technical computing.
- [matplotlib](http://matplotlib.org/),  a plotting library for the Python programming language and its numerical mathematics extension NumPy.

and the [Computer Algebra System (CAS)](https://en.wikipedia.org/wiki/Computer_algebra_system) [Sympy](http://www.sympy.org/).

The suggested method is to download a Python Distribution, preferably [Anaconda](https://www.continuum.io/downloads). This will include all the packages mentioned above.


## Slides
The slides for some lectures are in the folder [``Slides``](./Slides) as ``.html`` files. They were written as Markdown (``.md``) files, and compiled with [``pandoc``](http://pandoc.org/) using

     pandoc -t slidy --css style.css -s slides.md -o slides.html

or

     pandoc -t slidy --css style.css --mathjax -s slides.md -o slides.html

to use [MathJax](https://www.mathjax.org/) to render the equations.

## License
All code is under MIT license and media under Creative Commons Attribute.

The content of this reposirtory is licensed under the [Creative Commons Attribution 4.0 license](http://choosealicense.com/licenses/cc-by-4.0/), and the source code that accompany the content is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).
