#!/bin/sh

# Check how many lines there are in module - excludes blank lines
printf "\n\n\n\n CHECK MODULE SIZE:"
printf "\nNumber of lines of code & comments in LISC: "
find ./lisc -name "*.py" -type f -exec grep . {} \; | wc -l

# Check number of files using cloc
printf "\n\n\n CLOC OUTPUT (EXCLUDING TESTS): \n"
cloc lisc --exclude-dir='tests'

printf "\n\n\n CLOC OUTPUT - TEST FILES: \n"
cloc lisc/tests --exclude-dir='test_files'

# Run Tests & Check Coverage
printf "\n\n\n RUN TESTS & TEST COVERAGE: \n"
coverage run --source lisc  -m py.test
coverage report

# Run pylint and print summary
printf "\n\n\n RUN PYLINT ACROSS MODULE: \n"
pylint lisc --ignore tests -> _lint.txt
tail -n4 _lint.txt

# Print out some new lines
printf "\n\n\n"
