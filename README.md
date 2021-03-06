# hunter-gatherer
Crawler to collect newspaper articles for analysis

Requirements
------------
* Docker
* Docker-Compose

And that's it. Docker will get any additional requirements and setup your development or testing environment.

Running
-------
To run the crawler, first the initial jobs must be placed in the queue. This can be done by running the ```seed.sh``` script.

After the queue is seeded the ```run.sh``` script can be run.

The crawler can be monitored by visiting ```localhost:5555```.

Development
-----------
You can run the develop script to get you started. The script will build a Docker container and run it.

The ```develop.sh``` script will start a Docker instance and connect to a bash terminal. Any changes made in the /app folder are also reflected in the running instance, allowing quick development. The exception to this is additional requirements.

For requirements to be loaded you need to add them to `deploy/app/requirements.txt` (python packages), or `deployment/app/Dockerfile` (ubuntu setup). A restart will be required.

Testing
-------
There is also a script to run the tests.

The ```./test.sh``` script will rebuild all the docker images to make sure everything is up to the latest production configs. In addition it will also build and launch a test container which will run unit tests.

**Any Pull Request that does not pass the test suite will not be merged**
