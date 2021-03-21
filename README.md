# E lection_Analysis
## Overview of Election Audit

A Colarado Board of Elections employee gave the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a list of all counties where votes were cast.
3. Get a complete list of candidates who received votes.
4. Calculate the number of votes casted from each county.
5. Calculate the county with the largest turnout. 
6. Calculate the total number of votes each candidate received. 
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of election based on popular vote.

## Resources
* Data source: election_results.csv
* Software: Python, Visual Code Studio 

## Results
The analysis of the election show that that:
* There were 369,711 votes cast in the election
* The counties part of the election were:  
  * Jefferson
  * Denver 
  * Arapahoe

* The result of each county was: 
  * There were 38,855 votes from Jefferson representing 10.5% of total turnout 
  * There were 306,055 votes from Denver representing 82.8% of total turnout 
  * There were 24,801 votes from Arapahoe representing 6.7% of total turnout 
  
* The county with the largest turnout was: 
  * Denver with 306,055 votes representing 82.8% of total turnout 
  
* The candidates were:  
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane

* The candidate results were: 
  * Charles Casper Stockham received 23.0% of votes and 85,213 number of votes. 
  * Diana DeGette received 73.8% of votes and 272,892 number of votes. 
  * Raymon Anthony Doane received 3.1% of votes and 11,606 number of votes. 

* The winner of the election was: 
  * Diana DeGette who received 73.8% of votes and 272,892 number of votes. 

The result can be viewed in this image: 
https://github.com/madihajaved/Election_Analysis/blob/main/Resources/output.png


## Election Audit Summary and Recommendation
This script can be modified and used in future elections or for elections in other states. To use it for other states, a csv file in a similar format needs to be referenced to - so where election_results.csv is referenced that file name needs to reflect the new data file. 
This can also be used for future elections and results can be saved in different output files. For  future election, instead of overwriting the current text file, a new text file can be created, and with the new data or csv file, the results can be saved there.  
