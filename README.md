# Classroom-Insights
   Classroom Insights is a software designed to compute various statistical metrics from a CSV file/database of students' and teachers' performance records. It was intended to be the teacher's companion when drafting end-of-sequence or end-of-year reports on classroom performances after evaluations. This software features multiple tools to provide the teacher with a unique perspective on their students' performances across evaluations. This software makes use of quantitative and graphical methods to provide insights. As a bonus, Classroom Insights is designed to allow for archiving statistics per sequence into a database file that can be shared with other colleagues for a more comprehensive perspective on performance. Furthermore, this software leverages the power of machine learning to predict students' performances on exams.
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

1. From the command line:
    ```
     python setup.py install
   ```
2. or using the release file coupled with the command:
   ```
    pip install Classroom-Insights-1.2.tar.gz
   ```
3. And run __main__.py:
  ```
     python __main__.py
   ```
4. An example CSV file: *Example_Class1.csv* is provided with the app (in the docs folder). Open this file from the app.

###### Desktop installation
1. Download the *Classroom-Insights.exe* setup from [SourceForge](https://sourceforge.net/projects/classsroom-insights/)
2. Install and run.

# Developing
1. Add functionality for teachers to import their classroom lessons and hours programs for a given year. That way,
when the pedagogy widget is activated, it can load this data and update itself automatically.
2. Include a remember functionality in the pedagogy window as well, so that it can keep track of previous progress.
3.  Add Qsettings object and widget to allow users to modify some program functionalities.
4. Add a function to include a personal timetable from the database or create one.
5.  Add functionality to fill the pedagogy widget from database info.
6. Add functions to tidy data, and perhaps scale scores to different values. It should request the former max score and
 sequences over which to apply this scaling.
7. Add the possibility to delete multiple rows from DB or class list
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

