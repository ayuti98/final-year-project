# final-year-project
# Diabetespredictor
REQUIREMENTS

The hardware and software requirements are as follows:
# 3.1 HARDWARE REQUIREMENTS
3.1.1 MICROCONTROLLER – ARDUINO UNO

The ArduinoUno is an open-source microcontroller board based on the Microchip ATmega328P microcontroller and developed by Arduino.cc. The board is equipped with sets of digital and analog input/output (I/O) pins that may be interfaced to various expansion boards (shields) and other circuits. The board has 14 Digital pins, 6 Analog pins, and programmable with the Arduino IDE (Integrated Development Environment) via a type B USB cable. It can be powered by the Universal Serial Bus (USB) cable or by an external 9-volt battery, though it accepts voltages between 7 and 20 volts. It is also similar to the Arduino Nano and Leonardo. Figure 3.1 shows Arduino.

3.1.1.1 TECHNICAL SPECIFICATIONS
•	Microcontroller: Microchip ATmega328P 
•	Operating Voltage: 5 Volts
•	Input Voltage: 7 to 20 Volts
•	Digital I/O Pins: 14 (of which 6 provide PWM output)
•	Analog Input Pins: 6
•	DC Current per I/O Pin: 20 mA
•	DC Current for 3.3V Pin: 50 mA
•	Flash Memory: 32 KB of which 0.5 KB used by bootloader
•	SRAM: 2 KB
•	EEPROM: 1 KB
•	Clock Speed: 16 MHz
•	Length: 68.6 mm
•	Width: 53.4 mm
•	Weight: 25 g





3.1.2 GAS SENSOR– MQ3 SENSOR


This is a very easy to use low cost semiconductor Gas sensor Module with analog and digital output. This module uses MQ3 Alcohol gas sensor as an alcohol gas sensing element. It requires no external components just plug in VCC& ground pins and you are ready to go.
For Digital output the threshold value can be easily set by an on-board potentiometer.  Using this module you can easily interface MQ3 Alcohol sensor to any Microcontroller, Arduino or even Raspberry Pi. Since this Gas Sensor module is sensitive to alcohol it can be used in breathalyzer. MQ3 Sensor also has small sensitivity to Benzine. Figure 3.2 shows the Gas Sensor (MQ3)

3.1.2.1 SPECIFICATION OF MQ3 GAS SENSOR MODULE:-
Power Supply: 5 Volts
Interface Type: Analog & Digital
High Sensitivity to Alcohol 
Low Cost.
Stable & Long Life.
3.1.3 LCD DISPLAY
  										
                                                       

CD (Liquid Crystal Display) is a type of flat panel display which uses liquid crystals in its primary form of operation. LCDs have a large and varying set of use cases for consumers and businesses, as they can be commonly found in smartphones, televisions, computer monitors and instrument panels. Figure 3.3 shows the LCD Display.                         



3.2 SOFTWARE REQUIREMENTS
3.2.1 DATASET – Pima Indians Diabetes Dataset
A dataset is a collection of data. In the case of tabular data, a data set corresponds to one or more database tables, where every column of a table represents a particular variable, and each row corresponds to a given record of the data set in question.

3.2.2 PYTHON 3.7
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.

3.2.3 WINDOWS OPERATING SYSTEM
Windows is a series of operating systems developed by Microsoft. Each version of Windows includes a graphical user interface, with a desktop that allows users to view files and folders in windows. For the past two decades, Windows has been the most widely used operating system for personal computers PCs.


3.2.4 PYCHARM 2020.1.1
PyCharm provides smart code completion, code inspections, on-the-fly error highlighting and quick-fixes, along with automated code refactoring and rich navigation capabilities.
PyCharm’s huge collection of tools out of the box includes 
•	an integrated debugger and test runner
•	Python profiler
•	A built-in terminal
•	Integration with major Version Control System (VCS) and built-in database tools
•	Remote development capabilities with remote interpreters
•	An integrated Secure Shell (SSH) terminal 
In addition to Python, PyCharm provides first-class support for various Python web development frameworks, specific template languages, JavaScript, CoffeeScript, TypeScript, HTML/CSS, AngularJS, Node.js, and more.PyCharm integrates with IPython Notebook, has an interactive Python console, and supports Anaconda as well as multiple scientific packages including Matplotlib and NumPy.

3.2.5 DJANGO 3.0.3
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
Django's primary goal is to ease the creation of complex, database-driven websites. 
The framework emphasizes 
•	Reusability and "pluggability" of components,
•	Less code
•	Low coupling
•	Rapid development, and 
•	The principle of don't repeat yourself. 
Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.


3.2.5.1 SUPPORT PACKAGES FOR DJANGO
 1. SCIKIT LEARN 0.23.1
Scikit-learn is an open source ML library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities.
Scikit-learn provides dozens of built-in ML algorithms and models, called estimators. Each estimator can be fitted to some data using its fit method.
•	Simple and efficient tools for predictive data analysis
•	Accessible to everybody, and reusable in various contexts
•	Built on NumPy, SciPy, and matplotlib
•	Open source, commercially usable - Berkeley Software Distribution (BSD) license


2. SCIPY 1.4.1
SciPy is a free and open-source Python library used for scientific computing and technical computing. It contains modules for optimization, linear algebra, integration, interpolation, special functions, Fast Fourier Transform (FFT), signal and image processing, Ordinary Differential Equation (ODE) solvers and other tasks common in science and engineering. 
SciPy builds on the NumPy array object and is part of the NumPy stack which includes tools like Matplotlib, pandas and SymPy, and an expanding set of scientific computing libraries. 
The SciPy library is currently distributed under the BSD license, and its development is sponsored and supported by an open community of developers. It is also supported by NumFOCUS, a community foundation for supporting reproducible and accessible science. 
3. JOBLIB 0.15.1
Joblib is a set of tools to provide lightweight pipelining in Python. In particular, joblib offers:
1.	transparent disk-caching of the output values and lazy re-evaluation (memorize pattern)
2.	easy simple parallel computing
3.	logging and tracing of the execution
Joblib is optimized to be fast and robust in particular on large data and has specific optimizations for numpy arrays. It is BSD-licensed.

4.	RESTFRAMEWORK 3.11.0
A REST API is a standardized way to provide data to other applications. Those applications can then use the data however they want. Sometimes, Application Programming Interface (API) also offer a way for other applications to make changes to the data.
There are a few key options for a REST API request:
•	GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
•	POST — Creates a new record that gets appended to the database
•	PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
•	DELETE — Deletes the record at the given URI
•	PATCH — Update individual fields of a record
Typically, an API is a window into a database. The API backend handles querying the database and formatting the response. What you receive is a static response, usually in JavaScript Object Notation (JSON) format, of whatever resource you requested.
5.	PANDAS 1.0.3
In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. 
It is free software released under the three-clause BSD license. The name is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.

6.	NUMPY 1.18.4
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. 
The ancestor of NumPy, Numeric, was originally created by Jim Hugunin with contributions from several other developers. 
In 2005, Travis Oliphant created NumPy by incorporating features of the competing Num array into Numeric, with extensive modifications. NumPy is open-source software and has many contributors.

7.	CRISPY-FORMS 1.9.1
django-crispy-forms provides you with a  tag that will let you control the rendering behavior of your Django forms in a very elegant way. Have full control without writing custom form templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application.












