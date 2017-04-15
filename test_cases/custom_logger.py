from test_cases import *


class CustomLogger(MainTc):
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    file_handler = logging.FileHandler(cons.PATH_TO_LOGGER + '/logger.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

