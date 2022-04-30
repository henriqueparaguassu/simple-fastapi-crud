from sys import argv
from os import system

dev = "uvicorn api:app --reload"
start = "uvicorn api:app"

if len(argv) > 1:
    if argv[1] == "-dev":
        system(dev)
    elif argv[1] == "-start":
        system(start)
    else:
        print("Invalid argument.")
else:
    print("Using default: uvicorn api:app --reload")
    system(dev)
