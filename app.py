from flask import Flask
from flask import Response
from waitress import serve
import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file', help='file path', type=str)
args = parser.parse_args()
FILEPATH = args.file
CHUNK_SIZE = 10000

## Preprocess the file and store chunks of it (each having number of lines = CHUNK_SIZE)
## This preprocessing allows us to reduce the query processing time as for every query only CHUNK_SIZE number of lines are iterated
def preprocess(FILEPATH):
    with open(FILEPATH, 'r') as f1:
        c = -1
        for i, line in enumerate(f1):
            if math.floor(i/CHUNK_SIZE) > c: 
                c = math.floor(i/CHUNK_SIZE)
                f1 = open('files/' + str(c) + '.txt', 'w') 
            f1.write(line)

## Creates a flask application and stores it in "app"
app = Flask(__name__) 

## Route for root of the application 
@app.route('/')
def welcome():
    return Response('Welcome to the line server applcation by Ketan Kale!', status=200, content_type="application/json")


## Route for supporting the individual lines of a file being hosted
@app.route('/lines/<index>')
def get_line(index):
    if int(index) == 0:
        return Response('Illegal index requested', status=400)
    try:
        with open('files/'+str(math.floor(int(index)/CHUNK_SIZE))+'.txt', 'r') as f:
            ## calculate the offset index
            local_index = int(index) % CHUNK_SIZE
            ## enumerate returns an iterator over the file and hence only load one line into memory at a time
            ## Thus, even if a large file is to be processed this application will work
            for i, line in enumerate(f):
                if i == int(local_index) - 1:
                    return line
            ## for handling the indexes that could have been a part of the last chunk
            return Response('Requested line number is beyond end of file', status=413)
    except FileNotFoundError:
        ## Since the file for the index was not available, that means the index never occurred in the file, hence return 413
        return Response('Requested line number is beyond end of file', status=413) 

if __name__ == '__main__':
    preprocess(FILEPATH)
    serve(app, host='0.0.0.0', port=80)