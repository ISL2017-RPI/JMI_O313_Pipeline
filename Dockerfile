FROM keyi/python2-mcr2017a-rpi-isl

COPY JMI_O313/ ./JMI_O313
COPY setup.py ./
COPY O313_JMI_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
