from test_cases import *


class TC10(MainTc):
    """From client side write data into a file in a share directory. Condition *(ro, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC10.logger.info(cons.INFO_WRITE_DATA + cons.INFO_CONDITION_RO)
        step_1 = MainTc.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_TOUCH +
                                      cons.SERVER_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Verification.check_ssh_to_server(step_1, TC10, 1)
        step_2 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_2, TC10, 1)
        Verification.check_work_dir(TC10)
        step_3 = MainTc.write_into_file(cons.TEST_FILE_NAME, cons.SCRIPT_DATA)
        Verification.check_write_into_file(step_3, TC10, 3)
        Verification.check_read_from_file(TC10, cons.TEST_FILE_NAME)
