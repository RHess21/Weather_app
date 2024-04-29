My chosen SAST for this project was SNYK, it does both CLI and github scanning to look for any security flaws for both dependecies and the source code itself. My scan came up completely clean and I had 0 vulnerabilites in the source code. 

I Created Two unit test classes which each run 2-4 tests on the methods.

There is a Logger that writes to the log.txt file on any success or failure.

I also partitioned the code into multiple files to ensure the processes were seperate. 

The packages im using are logging, unittest, and re.
The logger needed the logging module, unit tests needed the unittest module and re was needed for the regex to  check the zipcode, all of which are on the most recent versions.

The third party API I used was the OpenWeather API.