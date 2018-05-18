# importing comet_ml
from comet_ml import Experiment

# importing keras
from keras.models import Sequential
from keras.layers import Dense, Dropout


# Creating the experiment object
experiment = Experiment(api_key = "ZYZWOp8YGYbWZjtv5b0kJJqC1", 
                        project_name = "Machine learning with keras", 
                        team_name = "Machine learning - UFRGS CLN",
                        auto_param_logging=True) 

batch_size = 128
num_classes = 10
epochs = 20

params={
    "batch_size":batch_size,
    "epochs":epochs,
    "num_classes":num_classes}

experiment.log_multiple_params(params)


# define model here 
with experiment.train():
    history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=1,
                        callbacks=[EarlyStopping(monitor='loss', min_delta=1e-4, patience=3, verbose=1, mode='auto')])

with experiment.test():
    loss, accuracy = model.evaluate(x_test, y_test)
    print(loss, accuracy)
    metrics = {
      'loss':loss,
      'accuracy':accuracy
    }
    experiment.log_multiple_metrics(metrics)

#You can also log specific metrics to training and test contexts with our context managers Experiment.train(), Experiment.validate() and Experiment.test()
    
# Run your code and go to https://www.comet.ml - creation of experiment
