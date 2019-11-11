# Project Title
**Explore US Biskeshare Data**

## Table of contents
* [General info](#general-info)
* [Data set](#data-set)
* [Methodology](#methodology)
* [Filed used](#files-used)
* [Date created](#date-created)
* [Contact](#contact)
* [Credits](#credit)

### Description
Data related to bike share systems for three major cities in the United States (Chicago, New York City, and Washington) are analyzed.

### Data set
Randomly selected data for the first six months of 2017 for all three cities are provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States.

Raw data-sets contain the same core six columns, i.e.:
- Start Time
- End Time
- Trip Duration
- Start Station
- End Station
- User Type

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

### Methodology
A Python raw user inputs interactive script is used to import raw data and compute descriptive statistics such as:
1. Popular times of travel (i.e., occurs most often in the start time)
   - most common month
   - most common day of week
   - most common hour of day


2. Popular stations and trip
   - most common start station
   - most common end station
   - most common trip from start to end


3. Trip duration
   - total travel time
   - average travel time


4. User info
   - counts of each user type
   - counts of each gender
   - earliest, most recent, most common year of birth

Depending on specific user inputs:
- data can be filtered by day or month (and statistics are then accordingly computed)
- raw data can be displayed    


### Files used
Three raw-data files are used as inputs:
- chicago.csv
- new_york_city.csv
- washington.csv

One Python script is used to load and analyze the data:
- bikeshare_AF.py

**Python Version**: Python 3.7.3 64-bit  

### Date created
Project created on Wednesday, ‎November ‎6, ‎2019, ‏‎5:43:59 PM

### Contact
Please contact [Alessandro Frascati](alessandro.frascati@shell.com)

### Credits
- [Markdown Quick Reference](https://en.support.wordpress.com/markdown-quick-reference/)
- [Stack Overflow](https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python)
