import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--lc', help='count of lines', type=int)
args = parser.parse_args()
lineCount = args.lc
if lineCount != None:
    with open('temp.txt', 'w') as f:
        
        for i in range(lineCount):
            f.write("THIS IS LINE NUMBER " + str(i) + "\n") 
else :
    print("please pass the number of lines you want to write to the file as the argument.")