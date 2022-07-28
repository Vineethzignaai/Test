Python  installation 
1. Go to Python.org   (Python version 3.7 +)
2.Click Python download 
3. In Mac Os  
    (i) GO to terminal and type "python --version" --> If python version shows in terminal good to go 
    
Installing IDE , Prefred Pycharm
1. Go to JetBrains.com , Download Community version
Open Pycharm 
1. Click on New Project 
2. On next Page , Define Loaction where you want store files 
3.In Python Interpreter  ,Click in New Enivironment "Virtualenv"  , It will create Virtual Enivironment base your given Location 
4.The click on Create 


Installing Selenium base inside  Virtual env
In Mac os : Go to the  inside virtual env  trough Terminal and type "source tutorial-env/bin/activate"
In windows : using terminal in  pycharm , Type "tutorial-env\Scripts\activate.bat" . 

Note : "tutorial- env" is the name virtual env , you can choose any name 

1.If you see (tutorial- env) C:\user\.. like this , Virtual env ir activated

2.Inside the  virtual env , please install  selenium package  using pip install
     in termnial - Type "pip install seleniumbase" and click Enter , it will install auomatically 
     After installing , you will see Seleniumbase  succesfully installed in termnial 
     
3. Now install Chrome Driver  - In terminal please type "sbase install chromedriver latest" and click enter 


To Run test case 
1. Come Out side virtual environment folder  , create a folder called tests
2. create python package file run name "test_home.py" and save it 
3. Required Test cases will written and save in test_home.py 
4. Type "pytest" in terminal  and yipeee test case will run 
     
