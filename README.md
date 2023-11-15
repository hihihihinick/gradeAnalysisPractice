# Student Grade Analysis Script

## Overview
This Python script performs a statistical analysis on a dataset of student grades. 
It calculates the average grade, standard deviation, and the probability of achieving grades above certain thresholds both for individual students and for class averages. 
The script utilizes the Central Limit Theorem to understand the behavior of class averages for a typical class of 30 students.

## Prerequisites
To run this script, you will need Python installed on your machine along with the following Python libraries:
- pandas
- numpy
- scipy
- BeautifulSoup

You can install these packages using pip on macOS/Linux:
```bash
pip install pandas numpy scipy beautifulsoup4
```

## Data Format
The script expects an XHTML file containing the grades data in a table format. The file should be named `300 Grades data set.xhtml` and located in the same directory as the script.

## Running the Script
1. Export the data set as a .xhtml file
2. Place the `300 Grades data set.xhtml` file in the same directory as 'grade_analysis.py'.
3. Run the script using Python:
   ```bash
   python grade_analysis.py
   ```
