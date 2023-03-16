# Classsroom-Insights
   Classroom Insights is a simple software designed to compute various statistical metrics from a CSV-file/database of students' and teachers' performance records. 
It was designed to be the teacher's companion when drafting end-of-sequence or end-of-year reports on classroom performances. This software features
tools to evaluate the teacher's own pedagogic performance against expected metrics. Classroom Insights will allow the teacher to have a unique
 perspective on their performance as well as on those of their students, and provide insights into how these performance indices may be improved upon.
As a bonus, Classroom Insights is designed to allow for archiving of statistics per sequence into a database file which can be shared with other 
colleagues for  more comprehensive perspective on performance.

![Main UI](https://a.fsdn.com/con/app/proj/classsroom-insights/screenshots/CI_ScoreUI%20.png/max/max/1)

## IMPORTANT FEATURES
1. Computes descriptive statistics of student's and classroom test scores.
2. Computes the gender performance statistics for a given test.
3. Computes the lessons and hours statistics of the teacher for a given test.
4. Provides a graphical overview of students' performances.
5. Identifies weak and strong students based on the performance over a sequence of tests.
6. Archives the various statistics into a database for future reference and comprehensive statistical view.

## INSTALLATION

###### Python installation
1. Install python 3 (developed, tested and run on python 3.9) from the official website.
2. Install PyQt5, scipy,matplotlib  from command line using python's pip (package manager) via:
 ```
 python -m pip install PyQt5, scipy, matplotlib 
 ```
3. Open the *ClassroomInsights.py* with python's *IDLE* editor and run
4. An example CSV file: *Example_Class1.csv* is provided wih the app. Open this file from the app.

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

# IMPORTANT NOTES
1. An Example .csv file is provided with the installer and located in the install directory folder: Example Input. 
CSV files can be created with Microsoft Excel.
2.Instructions on how to format the csv  file is located in the documentation which can be accessed from the menu bar of the app.

###### AUTHOR
Forwah Amstrong Tah, Ph.D <lmsoftware2023@gmail.com>

