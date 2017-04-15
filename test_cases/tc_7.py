from test_cases import *


class TC7(MainTc):
    """From a test directory on client side move a file into a share directory. Condition *(ro, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC7.logger.info(cons.INFO_MOVE + cons.INFO_CONDITION_RO)
        step_1 = MainTc.make_dir(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Verification.check_make_dir(step_1, TC7, 1)
        step_2 = MainTc.change_directory(cons.PATH_TO_TEST_DIR + cons.TEST_DIR_NAME)
        Verification.check_change_dir(step_2, TC7, 2)
        Verification.check_work_dir(TC7)
        step_3 = MainTc.touch_file(cons.TEST_FILE_NAME)
        Verification.check_touch_file(step_3, TC7, 3)
        step_4 = MainTc.move_file(cons.TEST_FILE_NAME, cons.CLIENT_PATH_TO_SHARE)
        Verification.check_move(step_4, TC7, 4)
        Verification.check_list_of_files(TC7)
        step_5 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_5, TC7, 5)
        Verification.check_work_dir(TC7)
        Verification.check_list_of_files(TC7)
