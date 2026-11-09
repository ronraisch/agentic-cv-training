# Original shape-rendering exercise

[Chapter index](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

<details>
<summary>On this page</summary>

- [Final Exercise](#final-exercise)

- [Objectives](#objectives)

- [Intro](#intro)

- [The Task](#the-task)

- [Design Guidelines](#design-guidelines)

- [Submission Guidelines](#submission-guidelines)

- [Important Notes!](#important-notes)

- [Implementation Steps](#implementation-steps)

- [Appendix - Sample XML Input File](#appendix-sample-xml-input-file)

</details>

**Historical handout, preserved in full.** This records the older learner text; historical schedules and instructions to complete every reading or old assignment are superseded by the stage syllabus above. Reading links now point to local explanations. Video links retain their source destinations. The current required exercises are linked from the stage syllabus.

## Final Exercise

## Objectives

Practice various Design Patterns and writing quality code

Learning and incorporating various code libraries (OpenCV, ElementTree XML)

Basic experience with geometric shapes and simple transformations

## Intro

### Some terminology of computer graphics:

Canvas - A matrix of pixel values, describing the image

Rendering - the process in which the canvas is built out of vector-based description.<br>For example, the vector-based description `Line[(1,0),(1,2)]` will be translated into the matrix:<br><br>![Original handout figure](assets/legacy-shape-rendering-image1.png)

## The Task

You should build a program that accepts as input an XML file describing some shapes, and will produce as output a canvas presenting that image. The canvas should be both presented on screen and saved as an image file.

## Design Guidelines

By the end, you will support accepting an XML file as input, that describes a scene by a variety of shapes and transforms on these shapes. However the task will be given as incremental steps to implement, so having a good design that keeps in mind the end goal may benefit in later steps.

## Submission Guidelines

Before starting to code, create a design for your system and go through a design review with your shampooer.

You will use git for this project. Open a git repository and give access to your shampooer. For every step, open a new branch and when you are done submit a pull/merge request to the main branch (to be reviewed by the shampooer).

## Important Notes!

### Notes on the Task

It is highly recommended to use existing libraries - if a tool exists, no reason not to take advantage of it...

[Numpy](arrays-data.md) - representing points

[OpenCV](cv-filtering.md) - representing the canvas and rendering

[ElementTree](development-foundations.md) - XML parsing

When designing your program, consider using polymorphism and [factories](development-foundations.md)

Definition of the rotation axis and scaling are up to you, but it is recommended to define them in the most intuitive way possible

### General Notes

Pay attention to clean code principles!

Document your work process and the program itself

Avoid redundant and trivial documentation

## Implementation Steps

### Step 1

As a starting point, support reading from xml and drawing the follow shapes:

Circle

Line

Each of the basic shapes should support border/fill colors

Example XML:

<Scene>

<Circle X="100" Y="100" Radius="100" FillingColor="White" Color="Black" />

<Line Color="Black">

<Point X="100" Y="100" />

<Point X="200" Y="100" />

</Line>

</Scene>

### Step 2

Support also the following shapes

Triangle

Quadrilateral

Support the following transformations in every shape

Translation

Rotation

Scaling

Remember that each of the basic shapes should support border/fill colors

Example XML:

<Scene>

<Circle X="100" Y="100" Radius="100" FillingColor="White" Color="Black" />

<Circle X="25" Y="0" Radius="25" FillingColor="Black" Color="Black" />

<Circle X="175" Y="0" Radius="25" FillingColor="Black" Color="Black" />

<Circle X="50" Y="50" Radius="15" FillingColor="Black" Color="Black" />

<Circle X="150" Y="50" Radius="15" FillingColor="Black" Color="Black" />

<Triangle Color="Black">

<Point X="100" Y="150" />

<Point X="50" Y="125" />

<Point X="150" Y="125" />

</Triangle>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="100" Y="150" />

</Line>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="50" Y="190" />

</Line>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="150" Y="190" />

</Line>

<Circle Color="Black" X="0" Y="0" Radius="75" Scale="2" TranslateX="150" TranslateY="150" Rotate="0"/>

</Scene>

### Step 3

Support Complex Shapes:

A complex shape is a shape defined in the input file as a collection of other shapes. The program should support defining complex shape by naming them and then reusing them as shapes

Example XML:

<Scene>

<Composite Name="Panda" Draw="No">

<Circle X="100" Y="100" Radius="100" FillingColor="White" Color="Black" />

<Circle X="25" Y="0" Radius="25" FillingColor="Black" Color="Black" />

<Circle X="175" Y="0" Radius="25" FillingColor="Black" Color="Black" />

<Circle X="50" Y="50" Radius="15" FillingColor="Black" Color="Black" />

<Circle X="150" Y="50" Radius="15" FillingColor="Black" Color="Black" />

<Triangle Color="Black">

<Point X="100" Y="150" />

<Point X="50" Y="125" />

<Point X="150" Y="125" />

</Triangle>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="100" Y="150" />

</Line>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="50" Y="190" />

</Line>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="150" Y="190" />

</Line>

</Composite>

<Panda Scale="0.5" TranslateX="400" TranslateY="400" Rotate="45" />

<Panda />

</Scene>

### Step 4

Support JSON as an additional input format

Example JSON:

[

{

"type": "composite",

"name": "Panda",

"draw": false,

"children": [

{

"type": "circle",

"x": 100,

"y": 100,

"radius": 100,

"filling_color": "White",

"color": "Black"

},

{

"type": "circle",

"x": 25,

"y": 0,

"radius": 25,

"filling_color": "Black",

"color": "Black"

},

{

"type": "circle",

"x": 175,

"y": 0,

"radius": 25,

"filling_color": "Black",

"color": "Black"

},

{

"type": "circle",

"x": 50,

"y": 50,

"radius": 15,

"filling_color": "Black",

"color": "Black"

},

{

"type": "circle",

"x": 150,

"y": 50,

"radius": 15,

"filling_color": "Black",

"color": "Black"

},

{

"type": "triangle",

"color": "Black",

"children": [

{

"type": "point",

"x": 100,

"y": 150

},

{

"type": "point",

"x": 50,

"y": 125

},

{

"type": "point",

"x": 150,

"y": 125

}

]

},

{

"type": "line",

"color": "Black",

"children": [

{

"type": "point",

"x": 100,

"y": 175

},

{

"type": "point",

"x": 100,

"y": 150

}

]

},

{

"type": "line",

"color": "Black",

"children": [

{

"type": "point",

"x": 100,

"y": 175

},

{

"type": "point",

"x": 50,

"y": 190

}

]

},

{

"type": "line",

"color": "Black",

"children": [

{

"type": "point",

"x": 100,

"y": 175

},

{

"type": "point",

"x": 150,

"y": 190

}

]

}

]

},

{

"type": "Panda",

"scale": 0.5,

"translate_x": 400,

"translate_y": 400,

"rotate": 45

},

]

### Bonus Points

Support recursively defined fractals (a complex shape)

You should determine a terminating scenario (base case)

The fractal definition should be consistent with any other complex shape

<br>

## Appendix - Sample XML Input File

<Scene>

<Composite Name="Panda" Draw="No">

<Circle X="100" Y="100" Radius="100" FillingColor="White" Color="Black" />

<Circle X="25" Y="0" Radius="25" FillingColor="Black" Color="Black" />

<Circle X="175" Y="0" Radius="25" FillingColor="Black" Color="Black" />

<Circle X="50" Y="50" Radius="15" FillingColor="Black" Color="Black" />

<Circle X="150" Y="50" Radius="15" FillingColor="Black" Color="Black" />

<Triangle Color="Black">

<Point X="100" Y="150" />

<Point X="50" Y="125" />

<Point X="150" Y="125" />

</Triangle>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="100" Y="150" />

</Line>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="50" Y="190" />

</Line>

<Line Color="Black">

<Point X="100" Y="175" />

<Point X="150" Y="190" />

</Line>

</Composite>

<Panda Scale="0.5" TranslateX="400" TranslateY="400" Rotate="45" />

<Panda />

</Scene>
