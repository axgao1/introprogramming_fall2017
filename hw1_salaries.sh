#!/bin/bash

#f=$1
f="salaries.csv"

echo "(1) TOP SALARIES IN THE CITY!!"
# Remove dollar signs, sort the appropriate column, and show the top few.
cat salaries.csv | sed 's/\$//g' | sort -t , -k 8 -n -r | column -s "," -t | head -10
# Load/display the file.
# Find and replace $ with nothing (delete $).
# The results are indicated to be delimited by commas. Sort on key 8, Salaries, by numeraire, and reverse the results.
# Display the results by columns as a table using commas as the delimiter.
# Show the first 10 lines of results.
echo

echo "(2) CITY EMPLOYEES"
# Count the lines, but careful of headers....
cat salaries.csv | tail -n +2 | wc -l
# Load/display the file.
# Count the number of lines starting from the second line from the top.
echo

echo "(3 and 4) :: FULL AND PART-TIME WORKERS"
# Cut out the apppropriate column, sort it, and count the types.
grep '\$' salaries.csv | cut -f5 -d, | sort | uniq -c
# Filter for $ in file.
# Cut 5th field delimited by commas (Full or Part-Time).
# Sort the F or P indications so the same indications are adjacent to each other.
# Count each unique occurrence of F or P.
echo

echo "(5 and 6) HIGHEST HOURLY WAGES"
# Same approach as the first question.
grep 'Hourly' salaries.csv | sed 's/\$//g' | sort -t, -k9 -n -r | column -s , -t | head -10
grep 'Hourly' salaries.csv | sed 's/\$//g' | sort -t, -k9 -n -r | tail -n +4 | column -s , -t | head -10
# Filter for all lines that contain 'Hourly' in file.
# Find and replace $ with nothing (delete $).
# The results are indicated to be delimited by commas. Sort on key 9, Hourly Rate, by numeraire, and reverse the results.
# Start with 4th line of results (because the first 3 results are doctors in the Health Department).
# Display the results by columns as a table using commas as the delimiter.
# Show the first 10 lines of results.
echo

echo "(7) POLICE DEPARTMENT"
# Just grep out the department and count the lines.
grep '\$' salaries.csv | cut -f4 -d, | grep -i 'police' | sort | uniq -c | head -1
# Filter for all lines containing $ in file.
# Cut the 4th field, Department, delimited by commas.
# Filter for police, ignoring the case of the text.
# Sort results for all lines in Department containing police.
# Count each unique occurrence of police.
# Show only the first line of the results (because second line shows results for police board, a separate department).
echo

echo "(8) DETECTIVES"
# One more grep than the last.
grep -i 'police' salaries.csv | grep -i 'detective' | wc -l
# Filter for police, ignoring the case of the text.
# Filter results for detective, ignoring the case of the text.
# Count resulting lines.
echo

echo "(9) THE MODAL FIREMAN"
# grep out the fire department, cut the salary column, sort it and count the number with each salary.
# Then sort these and print the the most common occurrence.
grep -i 'fire' salaries.csv | cut -f8 -d, | sed 's/\$//g' | sort | uniq -c | sort
grep -i 'fire' salaries.csv | cut -f8 -d, | sed 's/\$//g' | sort | uniq -c | sort | tail -1
# Filter for fire, ignoring cases.
# Cut field 8, Salary, delimited by commas.
# Delete $.
# In the first line of code, the results of salaries are sorted so all same numeraires are adjacent to each other to count unique occurrences.
# The resulting counts are sorted again for a number with each salary.
# In the second line of code, the results are sorted on numeraires as above code and only the last result is shown (the highest count, mode salary).
echo

echo "(10) NAMES FOR POLICE OFFICERS"
# sed to remove last names (preceding the first comma).
# grep for police officers, and then remove everything else in the line.
# sort the names, and use uniq to get their frequencies.
grep -i 'police officer' salaries.csv | cut -f2 -d, | cut -d' ' -f3 |sort | uniq -c | sort
# Filter for police officer.
# Cut the second field, first names, delimited by commas, to remove last names.
# Cut the results, delimited by spaces, to get the third field, where the first name begins because there are 2 spaces before the name.
# Sort by the results, just the first names.
# Count the unique occurrences of the first names.
# Sort by the counts. Jennifer has the highest occurrence in female names.
