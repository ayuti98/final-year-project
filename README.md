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



# 3.2 SOFTWARE REQUIREMENTS
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


# DESIGN

Design of the diabetes predictor is divided into hardware and software. The following sections describe the design.

# 4.1 HARDWARE DESIGN
MQ3 gas sensor is used to take the input as a blow through the mouth. User has to blow into the Gas Sensor, which will be fed into the microcontroller (Arduino UNO).
The microcontroller will generate the blood glucose count, which will be provided to the computer for further analysis.

4.1.1 Algorithm for BGL calculation
1) Air is passed over sensor by blowing

Working of sensor

Structure and configuration of MQ-3 gas sensor is shown as Figure, sensor composed by micro AL2O3 ceramic tube, Tin Dioxide (SnO2) sensitive layer, measuring electrode and heater are fixed into a crust made by plastic and stainless steel net. The heater provides necessary work conditions for work of sensitive components. The enveloped MQ-3 have 6 pins,4 of them are used to fetch signals, and other 2 are used for providing heating current.

 2) The analog signal obtained from sensor is input to analog pin of Microcontroller Unit (MCU)
 
 Calculations
The analog signal is converted to Blood Alcohol Concentration (BAC) using the following relation
float v= (adcValue/10) * (5.0/1024.0);                                                                               (4.2)
float mgL=0.3 * v;                                                                                                              (4.3)
Linear relationship exists between the acetone concentration in breath and blood glucose level.
BAC is then concerted to BGL using the following equation
        BGL=91.38*mgL+41.374                                                                                            (4.4)

3)Display the result on LCD screen
Method
•	The screen is first connected serially
•	The display is cleared
•	Output from MCU is sent to the LCD screen
•	Readings are in mg/dl 
4) Input the readings manually into the ML module.

# 4.2 SOFTWARE DESIGN
The dataset will be used in order to train the system to predict diabetes.
The system will be trained using an algorithm (NB) so that it can be used as a noninvasive method for the detection of diabetes. 
The Figure 4.3 shows the design of the software.

The flow diagram is as follows:
•	The inputs along with the glucose count obtained will be entered through the user interface
•	The database will have records of data that will be used to train the system using the algorithm to predict diabetes.
•	Using the data taken from user interface, based on the training, the system will predict if there is a possibility of a person having diabetes.


4.2.1 ALGORITHM
Naïve Bayes Algorithm
NB classifiers are a collection of classification algorithms based on Bayes’ Theorem. It is not a single algorithm but a family of algorithms where all of them share a common principle.
■	Steps included
	Consider a dataset.
	The dataset is divided into two parts, namely, feature matrix and the response vector.
      Feature matrix contains all the vectors (rows) of dataset in which each vector consists of    the value of dependent features.
      Response vector contains the value of class variable (prediction or output) for each row of feature matrix. (Assumption: We assume that no pair of features are dependent. Secondly, each feature is given the same weight)
	Calculate bayes.p(A/B)=p(B/A)P(A)/P(B)
	Split the evidence(given the event B is true. Event B is also termed as evidence.) into the independent parts(to put a naive assumption to the Bayes’ theorem, which is, independence among the features).
      Now, if any two events A and B are independent, then,
P(A,B)=P(A)P(B)
	To create a classifier model (For this, we find the probability of given set of inputs for all possible values of the class variable y and pick up the output with maximum probability).
	Calculate class probability and conditional probability.
Gaussian naive bays classifier
In Gaussian NB, continuous values associated with each feature are assumed to be distributed according to a Gaussian distribution.
 A Gaussian distribution is also called Normal distribution. When plotted, it gives a bell shaped curve which is symmetric about the mean of the feature values as shown below:
                                   
        

from sklean.naive_bayes import GaussianNB	
classifier = GaussianNB(priop=none)classifier.fit(x_train,y_train)
y_epect = y_test
y_pred= classifier>predict(x_test)
score= accuracy_score(y_expect, y_pred)
Pros:
•	It is easy and fast to predict class of test data set. It also performs well in multi class prediction.
•	When assumption of independence holds, a NB classifier performs better compare to other models like logistic regression and you need less training data.
•	It performs well in case of categorical input variables compared to numerical variable(s). For numerical variable, normal distribution is assumed (bell curve, which is a strong assumption).
Cons:
•	If categorical variable has a category (in test data set), which was not observed in training data set, then model will assign a 0 (zero) probability and will be unable to make a prediction. This is often known as “Zero Frequency”. To solve this, we can use the smoothing technique. One of the simplest smoothing techniques is called Laplace estimation.
•	On the other side NB is also known as a bad estimator, so the probability outputs from predict are not to be taken too seriously.
•	Another limitation of NB is the assumption of independent predictors. In real life, it is almost impossible that we get a set of predictors which are completely independent.
Applications of Naive Bayes Algorithms
•	Real time Prediction: NB is an eager learning classifier and it is sure fast. Thus, it could be used for making predictions in real time.
•	Multi class Prediction: This algorithm is also well known for multi class prediction feature. Here we can predict the probability of multiple classes of target variable.
•	Text classification/ Spam Filtering/ Sentiment Analysis: NB classifiers mostly used in text classification (due to better result in multi class problems and independence rule) have higher success rate as compared to other algorithms. As a result, it is widely used in Spam filtering (identify spam e-mail) and Sentiment Analysis (in social media analysis, to identify positive and negative customer sentiments)
•	Recommendation System: NB Classifier and Collaborative Filtering together builds a Recommendation System that uses ML and data mining techniques to filter unseen information and predict whether a user would like a given resource or not.

# 4.3 DESIGN FLOW OF THE FULL SYSTEM
The input to get the glucose level will be taken from the breathanalyzer by making the user blow into the breath analyzer.
The breathanalyzer will calculate the blood glucose level and provide the calculated output as the input to the software.
Data set will be taken from PIDD repository.
The system will be trained using blood glucose level and other parameters including Body Mass Index (BMI), Age, Blood Pressure, etc.
Parameters will be taken from the user using the User Interface (Web page)
Based on the above parameters, the system will predict whether the person has possibility of having diabetes or not.

# IMPLEMENTATION

In this chapter, detailed implementation of the hardware and software is explained. 

# 5.1 HARDWARE IMPLEMENTATION
 
                                           
The connections between the LCD and Arduino UNO is shown in the above figure. 
In order to take the input from the breath, the sensor is connected as follows:
Pin A0 of the sensor is connected to Pin A0 of Arduino UNO,
Pin Ground of the sensor is connected to Pin Ground of Arduino UNO and 
Pin VCC of the sensor is connected to Pin 5V of Arduino UNO.
For finding the BGL from the breathe, we convert the BAL to blood glucose level using the following formula:
BGL=91.38*BAL+41.374                                                                                               


 appropriate CODE is written for hardware working.


# 5.2 SOFTWARE IMPLEMENTATION

The classification model is built based on various libraries and by importing libraries
like pandas and numpy which comes along with python.
Sklearntrain_test library is used for training and testing. 
Since the data is highly imbalanced we are using sampling technique from sklearn that is smote technique which works best in most of the casesfor scaling the data. 
For normalizing it, we are using minmaxscaler. 
Import counter to check the number of yes and no, which is going to create a dictionary and going to look for all the unique values, seaborn is used for visualizing confusion matrix.

Process
•	Import the file name called PimaID.csv 
•	Check for partial data and drop if any NA are present. 
•	Assign the parameters of the dataset to a float value.
•	Define  x and y  as  pre_x and pre_y and are further passed into resampling method as dm_x and dm_y.
•	Run the smote analysis, smote is general sampling method imported from imblearn.
•	We take the minority class and fit it.
•	Fit  data is scaled and transformed using minmaxscaler.Fit transform has the transformed data having equal amount of yes’s and no’s and also scaled.
•	Use the imported train test split. In this, instead of having separate training file and testing file we are using some data from actual file and allocating 20% of them to testing and then rest to train the model.
•	Import Gaussian NB classifier from the sklearn and set the classifier equal to 
GaussianNB(priors=None)
•	Fix x_train and y_train model 
•	Set y_test to an object and pass x_test in predict function in order to calculate the accuracy of classifier which comes out to be 75.5% .
•	If the value of y_pred>0.22(setting as threshold)then it will consider it as one else zero.
Once the model is created, then the next step is to pickle the model using the pickle function by using command: 
import pickle 
Since we have a trained model which we can use over and over again. In this case, the model is known as a classifier.
The main benefit is that when you are running an application every time, we are hitting the server and the server will go ahead and compute the classifier and come up with the result of the model which is computationally expensive and heavy for server to run.
So if the model is not going to change very often or no much updates are required at that time, Pickling is the right method which can be used to lower the load of the server since 
the file is already precompiled.
To pickle the model, it is going to take the model as input and store it in pickle, which is basically going to store all the weights into pkl with which the Gaussian classifier has calculated to give strong pre5dictive model. Similarly to scale the data, we have created scaler.pkl.
To perform testing,that is if the model is predicting the output correctly or not, we have taken readymade data set and then passed the value of data into list form in an array which is created using numpy .
The next step is to reshare the data into (1, -1) and then load the scaler pkl file in order to scale the input and then passed the reshape unit into the scaler function. In order to predict the output as 1 or 0, pass the scaled value into classifier.predict(), if the value is >0.22 then it will print output as 1 or else 0.

Web Interface Implementation using Django 
•	To build diabetes predictor using Django and Django restframework API,we have used Pycharm Community version as the Text editor.
•	PyCharm takes care of creating specific directory structure and files required for a Django application, and providing the correct settings.
                                         
                                              
•	Install all the required libraries and tools in the virtual environment created for Django program to work.
•	Create a new Django project - DjangoAPI
Now, your directory structure will look like the figure shown below after opening it in Pycharm-
                                   
                                                    
•	Create an app, in our case it is MyAPI - to deploy the model.
•	The structure of the directories and files will look as below when opened in Pycharm. 
                              
                                         
                                            

•	Next, go to settings.py(as shown in5.5) and add rest_framework, crispy_forms and app name i.e MyAPI in our case to INSTALLED_APPS section
                                      
                                              

•	The next is to update and add the urls in DjangoMYAPI(shown in 5.6), the project file, which we are going to call the urls.py ofmyapi.We have added the include() function to our imports.
•	We have added a new URL dispatcher. In this file, the dispatcher is simply including the urls.py file from the MyAPI app. 
•	The empty string ('') will match everything after the domain name.  This pattern must be the last entry in the urlpatterns list.  We have added the include() function to our imports.
                        
                                                   

•	The next step is to create same urls.py file in MyAPI folder(shown in 5.7) and need to add the urls which are needed to be created and then add it to the list urlpatterns in urls.py. 
•	In this, a request to http://127.0.0.1:8000/form would be routed to the index function in the application’s views.py file.
 
                                                  
•	The next step includes the file called model.py (shown in 5.8). Every model inherits from django.db.models.
•	Models in django are classified as a file which is created and consist of how the actual form is going to look like or what kind of data you want to enter. Depending on how you have designed the data, it is going to capture the data.
 
                                                      

•	Update serializer.py(shown in 5.9) from MyAPI.Serializers files allow complex data such as query sets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
 
                                                   
•	views.py(shown in 5.10) from MyAPI is basically a view python function that takes a Web request and returns a Web response. views.py is the main file which is going to have model files as well as form files. This file is responsible for how our application is going to run. 
              
                                                       
•	It has viewset model so anytime there is need to call request it will get all the data which is sitting in prediction class under model, the serializer is used for it.
                          
                                              
•	The dataframe passed by is passed into approvereject where it is going  to hit first the pickle files and then check the condition and predict the output and if it is true it will print ‘possibility that you may have diabetes’ and false implies ’you are safe’.
 
                                                      
•	Wecreate the form function in which the method which is used is post, then we have defined the form object where we are passing whatever data we take from the user interface.
 
                                                              
•	Check if the data entered in the form is valid, then we create the dataframe and passing it to the model, in this case its approvereject()and the output is reflected back on the server. This process of displaying onto the form is done by library called message, which only upon success is going to print the message.
 
                                                    


•	Form creation(shown in 5.11)
	With Django forms,we can either define one from scratch or create a PredictionForm which will save the result of the form to the model. Django. Forms have their own file: forms.py.
	We need to import Django forms first (from django import forms)
	PredictionForm, is the name of our form. We need to tell Django that this form is a Form – forms.Form
	Then we have our form fields defined by its type of input.We are using this form file to construct the skeleton of our form in which we are creating the class and using various form objects and we use this in the views to validate.

 
                                                     



•	Creating template(shown in 5.12)
-	In this we have written the normal html code for designing of our html page. It will look if any messages are present in views and if so then it runs the piece of code written and at the end it returns the messages back onto html.
                        
                                                      

•	To run the project we type 
•	python manage.py runserver
in the terminal window.
 
                                        

•	In the web browser, type - https://127.0.0.1:8000/

 

Then insert the data and it will display the output.
                                                          



 
                               












