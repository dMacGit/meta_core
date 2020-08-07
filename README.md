# Meta_Core - Search
_A basic package that handles Blu-Ray and DVD Movie Media, Meta data searching_

## Table of Contents
___

- [General Info](#General-Info)
- [Technologies](#Technologies)
- [Setup](#Setup)
- [Future](#Future)
- [Status](#Status)


---

## General Info

This makes use of the 3rd party API OMDBapi _http://www.omdbapi.com_ in order to grab information/meta-data on the searched DVD and Blu-Ray Movie title. Currently works on **Text** titles, but in future **imdb** specific id's as well.

## Technologies

- Python 3
- OMDBapi (**API Service**) [Here](http://www.omdbapi.com)
- lxml (**Library**) [Info here](https://lxml.de/) 
- Requests (**Library**) [Info here](https://requests.readthedocs.io/en/master/)

## Setup

1. Create an OMDBapi API key.
Read more [here](http://www.omdbapi.com/apikey.aspx)

2. Clone repo into target folder/directory.

3. Create **private_data** folder in root directory.

4. In **private_data** folder, create text file **private_key.txt** and paste in the key. Make sure the text format in the file reads: `key:placeKeyTextHere`

## Future

Most of the core functionality is complete. 
Requires adding support for imdb ID's as well as user defined Lists (Both tt-ids and titles).

Also Need to remove old code leftovers.

## Status

 - Currently still in development