from test_cases import *


class TC2(MainTc):
    """From client side rename a file from a share directory. Condition *(rw, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC2.logger.info(cons.INFO_RENAME + cons.INFO_CONDITION_RW)
        step_1 = MainTc.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_TOUCH +
                                      cons.SERVER_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Verification.check_ssh_to_server(step_1, TC2, 1)
        step_2 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_2, TC2, 2)
        Verification.check_work_dir(TC2)
        step_3 = MainTc.rename_file(cons.TEST_FILE_NAME, cons.TEST_FILE_2_NAME)
        Verification.check_rename(step_3, TC2, 3)
        Verification.check_list_of_files(TC2)
