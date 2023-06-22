# Classroom-Insights
   Classroom Insights is a simple software designed to compute various statistical metrics from a CSV file/database of students' and teachers' performance records. 
It was designed to be the teacher's companion when drafting end-of-sequence or end-of-year reports on classroom performances. This software features
tools to evaluate the teacher's own pedagogic performance against expected metrics. Classroom Insights will allow the teacher to have a unique
 perspective on their performance as well as on those of their students, and provide insights into how these performance indices may be improved upon.
As a bonus, Classroom Insights is designed to allow for archiving of statistics per sequence into a database file which can be shared with other 
colleagues for  a more comprehensive perspective on performance.
![Main](https://github.com/Forwah2023/Classsroom-Insights/assets/123673169/fb1b3eac-e486-4132-81be-067afc79e515)

## IMPORTANT FEATURES
1. Computes descriptive statistics of students and classroom test scores.
2. Computes the gender performance statistics for a given test.
3. Computes the lessons and hours statistics of the teacher for a given test.
4. Provides a graphical overview of students' performances.
5. Identifies weak and strong students based on their performance over a sequence of tests.
6. Archives the various statistics into a database for future reference and comprehensive statistical view.

## INSTALLATION

###### Python installation
1. Install Python 3 (developed, tested, and run on Python 3.9) from the official website.
2. Install PyQt5, scipy,matplotlib  from the command line using Python's pip (package manager) via:
 ```
 python -m pip install PyQt5, scipy, matplotlib,appdirs,reportlab 
 ```
3. Open the *__main__.py* with python's *IDLE* editor and run, or Install as a package:
 ```
 pip install Classroom-Insights-1.2.tar.gz
  ```
4. An example CSV file: *Example_Class1.csv* is provided with the app (in the docs folder). Open this file from the app.

###### Desktop installation
1. Download the *Classroom-Insights.exe* setup from [SourceForge](https://sourceforge.net/projects/classsroom-insights/)
2. Install and run.

# Developing
## Built With
* Python 3.9
* Pyqt5
* QT designer
* scipy
* matplotlib
* appdirs
* reportlab

# IMPORTANT NOTES
1. An Example .csv file is provided with the installer and located in the install directory folder: Example Input. 
CSV files can be created with Microsoft Excel.

2. Instructions on how to format the CSV  file are located in the documentation which can be accessed from the menu bar of the app.

###### AUTHOR
Forwah Amstrong Tah, Ph.D. <lmsoftware2023@gmail.com>

