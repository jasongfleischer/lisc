"""Tests for the Count class and related functions from lisc."""

import numpy as np

from lisc.objects.counts import Counts

###################################################################################################
###################################################################################################

def test_counts():

    assert Counts()

def test_scrape_one():

    counts = Counts()

    counts.add_terms(['language', 'memory'], dim='A')
    counts.add_exclusions(['protein', 'protein'], dim='A')

    counts.run_scrape(db='pubmed')
    check_funcs(counts)
    drop_data(counts)

def test_scrape_tw0():

    counts = Counts()

    counts.add_terms(['language', 'memory'], dim='A')
    counts.add_exclusions(['protein', 'protein'], dim='A')
    counts.add_terms(['cognition'], dim='B')

    counts.run_scrape(db='pubmed')
    check_funcs(counts)
    drop_data(counts)

def check_funcs(counts):

    counts.check_cooc()
    counts.check_top()
    counts.check_counts()

def drop_data(counts):

    counts.drop_data(0)
