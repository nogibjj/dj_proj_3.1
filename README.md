# dj_proj_3.1

# Purpose of project

In this project we are trying to answer the question: For a given writer/director, what is their average rating across all films? In order to answer this question we are querying the IMDB database stored in google bigquery data warehouse. 

### Preparing the Environment

To set up the environment we have our requirements.txt file which holds all the packages we need to install for this project as well as our makefile which will automate the install, format, lint and test. In addition we have our devcontainer and dockerfile which will house the environment for this project. 

### Process

The first step is to take in the arguments from the user using a command line tool. This will take in the individual and the specific role of the individual. The two arguments are then passed into the logic in query_demo.py which will connect to the google bigquery API and pass in the specified queries. The queries merge together three tables from the IMDB database and return a dataframe of all the non null ratings for the individual in that role.


### Workflow diagram

<img width="700" img height="700" alt="proj1_diagram" src="https://github.com/nogibjj/dj_proj_2/blob/3055f9003dbe1369deb470a3e65a772bae6c0a53/image.png">

<img width="1019" alt="proj1_diagram" src="https://user-images.githubusercontent.com/112578130/190939981-39799b6c-6f89-4e2e-8677-2bd4bb3617fc.png">

### Command Line Tool

To run this program, we can run the command line prompt: 
python ./get_rating.py cli-predict --person "name" --role "directors/writers" 
