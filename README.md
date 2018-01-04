# PyResistor

## Description
This python app aims to find quickly the code of three colors corresponding to an electrical resistor to a determined value.

## Graphical User Interface (GUI)
![image_resistor1](https://github.com/nicolaschen1/PyResistor/blob/master/images/image1.PNG)

## Supported platforms:
- Windows
- Linux

## How to use
It is simply to use this application, just put the value in the input and press the enter key.

## Resistor Color Code
Here is the code of colors for a resistor:
Black = 0
Brown = 1
Red = 2
Orange = 3
Yellow = 4
Green = 5
Blue = 6
Purple = 7
Grey = 8
White = 9

The colored bands indicate the value of the resistor (ohms). The first two bands indicate the first two digits of the numerical value. Then, we append these two digits a number of zeros equal to the indication provided by the third band. 

![image_resistor2](https://github.com/nicolaschen1/PyResistor/blob/master/images/resistor1.png)

## Constraint
This application can accept any digital input supplied in integer or real form, within the limits of from 10 to 10e11 Ω.

If the digit input is out of the limits, the background will be red during one second and the value will be deleted.

In this system, we specify two digits and it is sufficient for most electronic applications such as radio, computers, TV, etc.

## Example
For a value of 5300 Ω, the colored bands are green, orange and red.

![image_resistor3](https://github.com/nicolaschen1/PyResistor/blob/master/images/image2.PNG)

## Author
Nicolas Chen

## License
This project is under MIT License.

Copyright (c) 2017 Nicolas Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
