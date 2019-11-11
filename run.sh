#!/bin/sh
if [ $# == 0 ]
    then 
        echo please pass the file path to be served
        exit 1
fi

chmod u+x app.py
python app.py --file "$1"