# dj_proj_3.1

# Purpose of project

In this project we are trying to answer the question: For a given writer/director, what is their average rating across all films? In order to answer this question we are querying the IMDB database stored in google bigquery data warehouse. 

### Preparing the Environment

To set up the environment we have our requirements.txt file which holds all the packages we need to install for this project as well as our makefile which will automate the install, format, lint and test. In addition we have our devcontainer and dockerfile which will house the environment for this project. 

### Process

The first step is to take in the arguments from the user using a command line tool. This will take in the individual and the specific role of the individual. The two arguments are then passed into the logic in query_demo.py which will connect to the google bigquery API and pass in the specified queries. The queries merge together three tables from the IMDB database and return a dataframe of all the non null ratings for the individual in that role.


### Workflow diagram

<img width="1000" img height="700" alt="proj1_diagram" src="Screen Shot 2022-11-06 at 7.53.57 PM.png">

### Command Line Tool

To run this program, we can run the command line prompt: 
python ./get_rating.py cli-predict --person "name" --role "directors/writers" 
