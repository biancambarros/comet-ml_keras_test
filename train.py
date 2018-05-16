# import comet_ml in the top of your file
from comet_ml import Experiment

# Add the following code anywhere in your machine learning file
experiment = Experiment(api_key = "ZYZWOp8YGYbWZjtv5b0kJJqC1", project_name = "Testing machine learning with keras in comet.ml", team_name = "Machine learning - UFRGS CLN") #creating a new Experiment object, sending the APY key obtained from comet.ml and testing attributes

# Run your code and go to https://www.comet.ml - creation of experiment


#testing:
experiment.log_html('<a href="www.comet.ml"> I love Comet.ml </a>')

#Documentation - Experiment class
##Experiment is a unit of measurable research that defines a single run with some data/parameters/code/results.


