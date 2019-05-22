''' This projects makes use of an external api for searching/getting media
    meta data from known online database IMDB.

Examples:

    For this I will be using specific libraries:

    - lxml: For grabbing data in HTML format for "xpath" to parse

    - requests: Sending requests to web services.

    - json: For interfacing with the OMDBapi, and extracting Media data


Note:
    This script will potentially brake with any update to the sourced website.

Todo:
    * Tidy up/clean code
    * Rejig functions (Make work flow simple)
'''

from lxml import html
from urllib import parse
import json
import requests


SEARCH_BD_MV_TYPE = "Popularity" #Specifying global default search type, Unused for right now

Default_Location = "private_data/"
Default_File = "private_link.txt"
Default_OMDb_api_key = "private_key.txt"

def laod_api_key ():
    """Fucntion used to load API key to OMDBapi webservice.

        This Key is needed in every request to the api. And must trail any parameters/values in the request link.

    Example:
        Key is copied in plain text to a local text file "private_key.txt".
        Format of the file is "key:api_key", remove quotes ".
        This file is stored within a folder named "private_data" in the scripts home directory.

    Note:
        This is going to be the main source for title meta-data searching.

    Todo:
        Need to make sure alternative method of meta-data searching is setup, in-case of api change or close.
    """

    with open(Default_Location + Default_OMDb_api_key, 'r') as f:
        api_key_raw = f.readline()
        key = api_key_raw.split(':')[1].strip()
        f.close()
    return key

def imdb_search( title ):
    """Main function that calls the OMDBapi with search title.

    :param title: Takes as argument the "Title" of the movie to search.
        Needs to attach the api key in every request.

    :return results: Results object.

    :TODO:
        Note that can search for ttnumber. Unsure if useful at this time.

    """

    if title is not None:
        #http://www.omdbapi.com/?i=[ttnumber]&apikey=
        #http://www.omdbapi.com/?t=[title]&apikey=
        url_pre = "http://www.omdbapi.com/?t="
        url_post = "&apikey="
        encoded_title = parse.quote_plus(title)
        full_url = url_pre+encoded_title+url_post+laod_api_key()
        results = requests.get(full_url)
        if results.status_code is 200:
            return results.content
        else :
            raise IOError("Bad return code: "+results.status_code)

def pars_imdb_object( data ):
    """IMDBapi object parser function

    Simply takes input data object and decodes into json ruturn object.

    :param data: The resulting data from the imdb_search() function

    :return json_data: Returns decoded json object
    """
    #Remove starting "b'{" and ending "}" characters.
    json_data = data.decode('utf8')
    #clean_data = str(data)[3:-2:1]
    print(json_data)
    return(json_data)

def laod_imdb_object( jasonData ):
    """Movie Object builder function

    Creator function that builds movie object from parsed Json data

    :param jasonData: Some parsed Json movie meta-data
    :return movieObject: Returns a new Movie_object
    """
    #basic: [title, imdbID, format]
    data_copy = json.loads(jasonData)
    #data_test = json.load(data_copy)
    print(data_copy)
    if "title" and "imdbID" and "DVD" in data_copy:
        title = data_copy['Title']
        imdbId = data_copy['imdbID']
        # Filling parameter as Blu-ray format
        format = "blu-ray"
        dvd_released = data_copy['DVD']
        newObject = Movie_object(title,imdbId,format)
    return newObject


def output_to_html(string_data):
    """Future function to output to text file.

    Note:
        Not yet implemented!
    """
    raise NotImplementedError("This function is not yet Implemented!")

class Movie_object(object):
    """Movie Object class

    Holds meta-data information. Useful for running searches.

    Example: Object creation
        Movie_object("ant man", tt0478970, blu-ray)

    Can also save website prices and ratings to movie object

    Example: Saving store price
        add_store("website name", url, price)

    Example: Saving website rating
        add_rating("website name", url, rating)

    """
    def __init__(self,title, imdb, format):
        """Initializing the Movie object

        Requires that the "title", imdb ID, and media format be parsed as args.

        :param title: Title of the movie
        :param imdb: The IMDB ID
        :param format: Media format.
        """
        self.title = title
        self.imdbID = imdb
        self.format = format

        #Ratings format: { site: rating,}
        self.ratings = {}

        #Links format: { store: link, }
        self.links = {}

        #Prices format: { store: price, }
        self.prices = {}


    def get_title(self):
        return self.title

    def get_imdbID(self):
        return self.imdbID

    def get_format(self):
        return self.format

    def add_store (self, store, link, price):
        if store not in self.links :
            self.links[store] = link
            self.prices[store] = price

    def add_rating ( site, rating ):
        pass

    def get_format (self):
        return self.format
    def get_rating (self):
        return self.ratings
    def get_link (self):
        return self.links
    def get_prices(self):
        return self.prices

    def __str__(self):
        return "Title: %s \nimdb: %s \nFormat: %s"%(self.get_title(),self.get_imdbID(),self.get_format())

    """def __str__(self):
        return '%s | %s | %s \tLink: %s\n\t @ prices: %s'%(self.title,self.format,self.ratings,self.links,self.prices)"""

    '''def __repr__(self):
        return self.title, '|', self.format, '|', self.rating,'\tLink:', self.link,'@',self.price, '|', 'Special:', self.hprice
    The below loop works! Do not touch'''

def movie_fileName_parser(fileName):
    rawName = str(fileName)
    pre_parsed = ""
    parsed_Name = ""
    if rawName.__contains__('.'):
        splitName = str(fileName).split('.')
        pre_parsed = splitName[0]
        fileType = splitName[1]
        print("File type was: ",fileType)
    else:
        raise Exception("Invalid file Name! ",rawName)
    if rawName.__contains__("_"):
        parsed_Name = rawName.split("_")[0]
    else:
        raise Exception("Un-parsable file Name! ", rawName)
    return parsed_Name


"""copy_of_list = grab_mApe_results(search_by_Title)
for item in copy_of_list:
    print('',copy_of_list[item])"""


