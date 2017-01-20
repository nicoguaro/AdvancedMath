% Paraview Tutorial
% Nicolas Guarin-Zapata
    email: nguarin@purdue.edu
    twitter: @nicoguaro
    github: nicoguaro
% October 26, 2016


------------------

# Installation

You can download the most recent version of Paraview in the Official website and just run the installer in your machine:

- [http://www.paraview.org/download/](http://www.paraview.org/download/)

------------------

# Tutorial Data

You can clone the repo using:

    git clone https://github.com/nicoguaro/paraview_workshop.git

Or download as a zip in

- [https://github.com/nicoguaro/paraview_workshop/archive/master.zip](https://github.com/nicoguaro/paraview_workshop/archive/master.zip)

------------------

# What is Paraview?

From Wikipedia:

>> ParaView is an open source multiple-platform application for interactive, scientific visualization. It has a client–server architecture to facilitate remote visualization of datasets, and generates level of detail (LOD) models to maintain interactive frame rates for large datasets. It is an application built on top of the Visualization Toolkit (VTK) libraries.

------------------

# Examples

<img src="../img/point_load_halfspace_ux.png"
    width=900
    class="centObj">
<img src="../img/cantilever_beam_Sxx.png"
    width=1000
    class="centObj">
<video controls
    width=900
    class="centObj">
    <source src="../img/square_hole.ogv" type="video/ogg">
</video> 

------------------

# Examples

More examples at:

- [ParaView's Flickr](https://www.flickr.com/photos/kitware/sets/72157603966390403/); and
- [Kitware's Vimeo](https://vimeo.com/kitware).

------------------

# Other visualization software

### Based on VTK

- VTK itself
- Mayavi
- VisIt

### Others

- Tecplot
- Origin

------------------

# Why visualize?

<object width="1400" height="600" data="The_Scream_table.html"></object>
<img src="../img/The_Scream.png"
    width=800
    class="centObj">

------------------

# Why visualize?

<img src="../img/ascombe.svg"
    width=900
    class="centObj">
    
- Anscombe, Francis J. (1973) Graphs in statistical analysis. American Statistician, 27, 17–21.

  | Property                                  |  Value       |
  |-------------------------------------------|:------------:|
  | Mean of each $x$ variable                 | 9.0          |
  | Variance of each $x$ variable             | 11.0         |
  | Mean of each $y$ variable                 | 7.5          |
  | Variance of each $y$ variable             | 4.12         |
  | Correlation between $x$ and $y$ variables | 0.816        |
  | Regression line                           | $y=3 + 0.5x$ |
    
------------------

# Data Types

<img src="../img/Data_types1.png"
    width=800
    class="centObj">
<img src="../img/Data_types2.png"
    width=800
    class="centObj">


------------------

# Paraview Graphic Interface

<img src="../img/Paraview_UI.SVG"
    width=900
    class="centObj">

------------------

# Activate Paraview Toolbars

<img src="../img/paraview_toolbars.png"
    width=800
    class="centObj">
    
------------------

# Representations

<img src="../img/representations.png"
    width=1200
    class="centObj">

------------------

# Common filters

<img src="../img/Common_filters.svg"
    width=1000
    class="centObj">


------------------

# Exercise 1

<img src="../img/Exercise1.png"
    width=900
    class="centObj">

------------------

# Exercise 1: Some steps

1. Open the file ``disk_out_ref.ex2``.
2. Apply a ``Extract Surface`` filter.
3. Apply a ``Clip`` filter.
4. Apply a ``Contour`` filter.
5. Setup the colormap and details.

------------------

# Exercise 1: Pipeline

<img src="../img/Pipeline.svg"
    width=900
    class="centObj">

------------------

# Exercise 2

<img src="../img/Exercise2.png"
    width=900
    class="centObj">
    
------------------

# Exercise 3

<img src="../img/Exercise3.png"
    width=900
    class="centObj">

------------------

# Exercise 4

<img src="../img/Exercise4.png"
    width=1000
    class="centObj">

And the output video would be
<video controls
    width=1000
    class="centObj">
    <source src="../img/membrane_animation.ogv" type="video/ogg">
</video> 


------------------

# References

- Kenneth Moreland. [The Paraview Tutorial: Version 5.1](http://www.paraview.org/Wiki/images/f/f7/ParaViewTutorial51.pdf). Sandia National Laboratories/Department of Energy, 2015. Wiki: http://www.paraview.org/Wiki/The_ParaView_Tutorial
- Niklas Röber. [Paraview Tutorial for Climate Science](mms.dkrz.de/pdf/vis/paraview.pdf). DKRZ, Deutsches Klimarechenzentrum, August 2014.
- Utkarsh Ayachit. [The ParaView Guide: Community Edition](http://www.paraview.org/paraview-guide/). Kitware Inc, 2015.
- Will Schroeder, Ken Martin, Bill Lorensen. [The Visualization Toolkit: An Object-Oriented Approach to 3D Graphics](http://www.kitware.com/products/books/VTKTextbook.pdf), Kitware Inc, 4th ed, 2006.
- Kitware Inc, [The VTK User’s Guide](http://www.kitware.com/products/books/VTKUsersGuide.pdf). Kitware Inc, 11th ed, 2010.

------------------

# What else can we do?

We can animate PacMan in ParaView
<video controls
    width=1000
    class="centObj">
    <source src="../img/PacMan.ogv" type="video/ogg">
</video> 