### EXAMPLE 1

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debuf message")
logging.info("Loading configuration")
logging.warning("This is a warning message")
logging.error("This is an error message")


### EXAMPLE 2

import logging

logging.basicConfig(
    filename='my_log.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("This is a debuf message")
logging.info("Loading configuration")
logging.warning("This is a warning message")
logging.error("This is an error message")


### EXAMPLE 3

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

def check_password(password):
    if len(password) < 8:
        logging.warning("Password too short!")
        return False
    else:
        logging.info("Password is valid.")
        return True

check_password("12345")
check_password("mojehaslo123")

