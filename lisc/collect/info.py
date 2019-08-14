"""Collect info & meta data from Pubmed."""

from bs4 import BeautifulSoup

from lisc.requester import Requester
from lisc.collect.process import extract
from lisc.data.meta_data import MetaData
from lisc.urls.eutils import EUtils, get_wait_time

###################################################################################################
###################################################################################################

def collect_info(db='pubmed', api_key=None, logging=None, folder=None, verbose=False):
    """Collect database information & metadata from pubmed.

    Parameters
    ----------
    db : str, optional, default: 'pubmed'
        Which pubmed database to use.
    api_key : str
        An API key for a NCBI account.
    logging : {None, 'print', 'store', 'file'}
        What kind of logging, if any, to do for requested URLs.
    folder : str or SCDB object, optional
        Folder or database object specifying the save location.
    verbose : bool, optional, default: False
        Whether to print out updates.

    Returns
    -------
    meta_data : MetaData object
        Meta data about the data collection.
    """

    urls = EUtils(db=db, retmode='xml', api_key=api_key)
    urls.build_url('info', settings=['db'])

    meta_data = MetaData()
    req = Requester(wait_time=get_wait_time(urls.authenticated),
                    logging=logging, folder=folder)

    if verbose:
        print('Gathering info on {} database.'.format(db))

    meta_data.add_db_info(get_db_info(req, urls.get_url('info')))
    meta_data.add_requester(req)

    return meta_data


def get_db_info(req, info_url):
    """Calls EInfo to get info and status of db to be used for scraping.

    Parameters
    ----------
    req : Requester object
        Requester object to launch requests from.
    info_url : str
        URL to request db information from.

    Returns
    -------
    db_info : dict
        Information about the database from which the data was accessed.
    """

    # Get the info page and parse with BeautifulSoup
    info_page = req.request_url(info_url)
    info_page_soup = BeautifulSoup(info_page.content, 'lxml')

    # Set list of fields to extract from EInfo
    fields = ['dbname', 'menuname', 'description', 'dbbuild', 'count', 'lastupdate']

    # Extract basic information into a dictionary
    db_info = dict()
    for field in fields:
        db_info[field] = extract(info_page_soup, field, 'str')

    return db_info
