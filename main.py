from subprocess import call
import datetime
import os

import download as dl
import reddit as rd


def main():
    # Download Reddit videos
    print('Fetching Reddit videos...')
    rd.reddit()
    # Download videos
    print('Downloading videos...')
    # dl.download()


if __name__ == '__main__':
    try:
        location = (os.getcwd())
        start = datetime.datetime.now()
        main()
        # Execute compile.sh from get cwd
        rc = call("sudo " + location+"/compile.sh", shell=True)
        end = datetime.datetime.now()
        print(f"Total time: {end - start}")
    except Exception as e:
        print(f"Error: {e}")
        # Exit with error
        exit(1)
