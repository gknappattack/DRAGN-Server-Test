# DRAGN-Server-Test
Python console application to test DRAGN-Server. Used to test DRAGN-Town Quest generation engine in preparation for Foundations of Digital Games 2022 Conference Submission (http://fdg2022.org/).

## Setup
Run DRAGN-Server on your local machine and make note of the IP address and port number it is running on.

Before running servertest.py, you must update the ip and port values in class Console __init__() to match those given from 
DRAGN-Server. 

No additional inputs are needed to run from console. 

```
python servertest.py
```

The above command is sufficient to run the code, if the server IP address and port number values are updated in servertest.py. 

Future implementation of this code will have the IP Address and Port Numbers passed as paramenters when the code is run from the command line. 

## Run instructions

When the test client is running, it will ask for the index of a chatbot to connect to. Chatbots indices are printed upon startup but
can be viewed again by typing -h or --help. Input should be a single integer value.

When you are done, quit the test client by typing --quit, quit, or q in the input.
