"""
Database and Terms Lists
========================

Exploring the LISC database and using files of terms.
"""

###################################################################################################

from lisc.utils.db import SCDB, create_file_structure

###################################################################################################
#
# SCDB Database Structure
# ~~~~~~~~~~~~~~~~~~~~~~~
#
# LISC comes with, and uses, a custom directory structure.
#
# If you want to store terms in files, place those files into a LISC database structure,
# and then relevant functions and objects will be able to load and use these terms.
#

###################################################################################################

# Create a database file structure.
#   When called without a path input, the folder structure is created in the current directory.
db = create_file_structure()

###################################################################################################
#
# Storing Terms in Text Files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Here we will explore using files to store terms to use for LISC collections.
#
# The typical use case would be to curate and write text files manually.
#
# For demonstration here, we will first programmatically create an example text file of terms to use.
#

###################################################################################################

# Set some terms file
terms = [['brain', 'cortex'], ['body', 'corporeal']]

# Save the terms out to a txt file
with open(db.get_file_path('terms', 'terms.txt'), 'w') as term_file:
    for term in terms:
        term_file.write(','.join(term))
        term_file.write('\n')

###################################################################################################

# Check the file structure for the created database
db.check_file_structure()

###################################################################################################

# Get a list of all files available in the 'terms' folder
term_files = db.get_files('terms')
print(term_files)

###################################################################################################

# Get the full file path for the terms file
db.get_file_path('terms', 'terms.txt')

###################################################################################################
#
# Term File Structure
# ~~~~~~~~~~~~~~~~~~~
#
# For term files, each line stores a new term, with synonyms for the same file stored
# as comma-separated values on the same line.
#

###################################################################################################

# Check out the terms file contents
with open(db.get_file_path('terms', 'terms.txt'), 'r') as term_file:
    print(term_file.read())

###################################################################################################
#
# Loading Terms from File
# ~~~~~~~~~~~~~~~~~~~~~~~
#
# Text files of Terms can be loaded and used with LISC objects, such as 'Counts' and 'Words'.
#
# For a general example, here we will use the underlying 'Base' object.
#

###################################################################################################

# Load the base object in LISC
from lisc.objects.base import Base

###################################################################################################

# Initialize a base LISC object
base = Base()

# Add terms to object, loading from file
base.add_terms_file('terms.txt', directory=db)

###################################################################################################

# Check the terms that were loaded from file
base.check_terms()

###################################################################################################
#
# The same structure can be used to store exclusion and inclusion words for terms.
#
# Exclusion and inclusions words should be stored in their own text files, also
# using one line per term, with comma-separated values for synonyms.
#
# Files that reflect the same set of terms, with a file for search terms, and optionally
# associated files for inclusion and exclusion terms should line up on the number of lines.
# That is, the n-th line of each file should refer to the same term. If a given search
# term does not have an associated inclusion or exclusion term, leave that line blank.
#
