import numpy as np
from scipy.stats import norm
from bs4 import BeautifulSoup

# Reading the HTML content from the file
file_path = '300 Grades data set.xhtml'
with open(file_path, 'r') as file:
    html_content = file.read()

# Parsing the HTML to extract grades
soup = BeautifulSoup(html_content, 'html.parser')
tables = soup.find_all('table')

# Extracting the grades from the table
grades = []
for row in tables[0].find_all('tr'):
    for cell in row.find_all('td'):
        try:
            # Extracting and converting the text in each cell to an integer
            grade = int(cell.get_text().strip())
            grades.append(grade)
            # Skip cells that do not contain integer values
        except ValueError:
            continue

# Calculating the average and standard deviation of individual grades
average_grade = np.mean(grades)
std_dev_grade = np.std(grades)

# Calculating probabilities based on the normal distribution assumption for individual grades
prob_above_90 = 1 - norm.cdf(90, average_grade, std_dev_grade)
prob_above_80 = 1 - norm.cdf(80, average_grade, std_dev_grade)

# Calculating standard deviation of the class average for a class of 30 students
sample_size = 30
std_dev_class_average = std_dev_grade / np.sqrt(sample_size)

# Calculating the probabilities for a class of 30 students
# Probability that a class of 30 students has an average grade higher than 90
prob_class_above_90 = 1 - norm.cdf(90, average_grade, std_dev_class_average)

# Probability that a class of 30 students has an average grade higher than 80
prob_class_above_80 = 1 - norm.cdf(80, average_grade, std_dev_class_average)

# Printing the results
print(f"Average Numeric Grade: {average_grade:.2f}")
print(f"Standard Deviation of Grades: {std_dev_grade:.2f}")
print(f"Probability of Individual Grade > 90: {prob_above_90:.2%}")
print(f"Probability of Individual Grade > 80: {prob_above_80:.2%}")
print(f"Average Class Average (for 30 Students): {average_grade:.2f}")
print(f"Standard Deviation of Class Average (for 30 Students): {std_dev_class_average:.2f}")
print(f"Probability of Class Average > 90: {prob_class_above_90:.2%}")
print(f"Probability of Class Average > 80: {prob_class_above_80:.2%}")
