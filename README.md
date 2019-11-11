# Line Server Assignment

## System requirements
- Python 3.x
- Flask 1.0.2 
   ```
   pip install flask
   ```  
- Waitress
   ```
   pip install waitress
   ```


## Instructions to run the code
- make sure you have the files/ folder created in the same directory as the "app.py" file 
- create a file to be served if you don't already have using: 
    ```
    python createFile.py --lc <NUMBER_OF_LINES_IN_THE_FILE>
    ```
    NOTE: The file will be created inside the project root directory 
- run the script "run.sh" with the file path as the parameter:
    ```
    ./run.sh <FILEPATH>
    ```

## Contents of the folder

 - app.py :  Contains the actual code for the application to locate the line at the given index
 - requirements.txt: Contains the dependencies for the applcation 
 - build.sh: Script for building the application  (empty in this case) 
    ```
    ./build.sh
    ```
 - run.sh: Script for running the application
    ```
    ./run.sh <FILEPATH>
    ```
 - files/ : Folder that will contain the chunks of the file
 - createFile.py: Helper python script for creating a test file for serving. This will create a file called "temp.txt" with given arbitrary text and given number of lines.
    
    NOTE: The file will be created inside the project root directory 
    ```
    python createFile.py --lc <NUMBER_OF_LINES_IN_THE_FILE>
    ```
## Answers to the questions

 - How does your system work? 
   * The system starts with preprocessing the given file and dividing it into chunks in order to save query processing time.
   * Then according to the index supplied in the request, the system looks up the chunk to be iterated over and then iterates over it
   * This way, for every query, the system has to iterate over the lines equal to the lines in the chunk (controlled by the variable CHUNK_SIZE in app.py)

 - How will your system perform with a 1 GB file? a 10 GB file? a 100 GB file?
   * Since the system starts with preprocessing the file, the query time will be the same even if the file is 1GB , 10GB or 100 GB as it depends only on the CHUNK_SIZE. The only difference the size of the file will cause is the time taken to preprocess (i.e to form the chunks). Thus the query performance will be unaffected by the size of the file. 

 - How will your system perform with 100 users? 10000 users? 1000000 users?
   * The system uses [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) to allow multithreaded serving of requests.
   * Since, the Flask run is a single threaded application, the system required a production standard server to handle multiple concurrent requests
   * The parameters like maximum_active_connections, threads etc. can be passed to the Waitress server and adjusted based on the observed performance  
 
 - What documentation, websites, papers, etc did you consult in doing this assignment?
   * [Flask Documentation](https://flask.palletsprojects.com/en/1.0.x/)
   * [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
   
 - What third-party libraries or other tools does the system use? How did you choose each library or framework you used?
   * [Flask](https://www.palletsprojects.com/p/flask/)
   * [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
   * The other choices in contention were [Gunicorn](https://gunicorn.org/), uwsgi and other WSGI servers for production standard performance. The choice of Waitress is mainly influenced by the following factors:
      - Performance
      - No dependencies except for the ones that are in Python's standard library
      - Ease of Use 

 - How long did you spend on this exercise? If you had unlimited more time to spend on this, how would you spend it and how would you prioritize each item?
   * The current implementation of the system took 10 hours
   * If more time was available I would have spent it testing for concurrency and scalability. 
   * I would also love to explore more prepprocessing techniques to minimize the time taken in that phase

 - If you were to critique your code, what would you have to say about it?
   * I think the code could be more modular. 
   * I would love to get more feedback for the code.
