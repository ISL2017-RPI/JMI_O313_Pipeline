# JMI_O313_Pipeline

This is the source code for our JMI primitive on the seed data O313.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jmi313 ./

Then, you can run the pipeline script in the following way:

docker run jmi313 python O313_JMI_wrapper.py

The output is the selected features stored in a csv file
