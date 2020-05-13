from config import huey
from tasks import startjob

if __name__ == '__main__':
    startjob('bird', 5, 5)