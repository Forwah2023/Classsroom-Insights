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
install_requires=['PyQt5==5.15.11','matplotlib==3.10.0','scipy==1.15.0','reportlab==4.2.5','appdirs==1.4.4','Pillow==11.1.0'],
include_package_data=True,
entry_points={
'console_scripts': [
'ClassIns=ClasssroomInsights.__main__ : main']
},
)