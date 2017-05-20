# hunter-gatherer
Crawler to collect newspaper articles for analysis

Requirements
------------
* Docker

And that's it. Docker will get any additional requirements and setup your development or testing environment.

Development
-----------
You can run the develop script to get you started. The script will build a Docker container and run it.
```
./develop.sh
```
This will start a Docker instance and connect to a bash terminal. Any changes made in the /app folder are also reflected in the running instance, allowing quick development. The exception to this is additional requirements.

For requirements to be loaded you need to add them to `deploy/app/requirements.txt` (python packages), or `deployment/app/Dockerfile` (ubuntu setup). A restart will be required.

Testing
-------
There is also a script to run the tests.
```
./test.sh
```
Will rebuild all the docker images to make sure everything is up to the latest production configs. In addition it will also build and launch a test container which will run unit tests.
