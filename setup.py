from setuptools import setup
setup(
name='ClasssroomInsights',
version='1.2',
author='Forwah Amstrong Tah',
author_email='lmsoftware2023@gmail.com',
description=open('README.md', 'r').read(),
url="",
license='GPL-3.0 license',
keywords='Classsroom-Insights pyqt5',
package_dir={'ClasssroomInsights': ''},
packages=['ClasssroomInsights'],
py_modules =['__main__','about', 'Advanced_stats','Class_Insights_scores','Database_Manager','Glossary','Pedagogy','resources_rc','statsfuncs'],
install_requires=['PyQt5','matplotlib','scipy','reportlab','appdirs'],
include_package_data=True,
entry_points={
'console_scripts': [
'ClassIns=ClasssroomInsights.__main__ : main']
},
)