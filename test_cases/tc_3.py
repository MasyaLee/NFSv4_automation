from test_cases import *


class TC3(MainTc):
    """From client side remove a file in a share directory. Condition *(rw, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC3.logger.info(cons.INFO_REMOVE + cons.INFO_CONDITION_RW)
        step_1 = MainTc.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_TOUCH +
                                      cons.SERVER_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Verification.check_ssh_to_server(step_1, TC3, 1)
        step_2 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_2, TC3, 2)
        Verification.check_work_dir(TC3)
        step_3 = MainTc.remove_file(cons.TEST_FILE_NAME)
        Verification.check_remove(step_3, TC3, 3)
        Verification.check_list_of_files(TC3)
