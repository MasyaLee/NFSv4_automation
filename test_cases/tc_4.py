from test_cases import *


class TC4(MainTc):
    """Copy a file from server side into a test directory on client side. Condition *(rw, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC4.logger.info(cons.INFO_COPY + cons.INFO_CONDITION_RW)
        step_1 = MainTc.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_TOUCH +
                                      cons.SERVER_PATH_TO_SHARE + cons.TEST_FILE_NAME)
        Verification.check_ssh_to_server(step_1, TC4, 1)
        step_2 = MainTc.make_dir(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Verification.check_make_dir(step_2, TC4, 2)
        step_3 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_3, TC4, 3)
        Verification.check_work_dir(TC4)
        step_4 = MainTc.copy_file(cons.TEST_FILE_NAME, cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Verification.check_copy(step_4, TC4, 4)
        '''verification of a file in test directory'''
        step_5 = MainTc.cat_file(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME + '/' + cons.TEST_FILE_NAME)
        Verification.check_cat_file(step_5, TC4, 5)
        Verification.check_list_of_files(TC4)
