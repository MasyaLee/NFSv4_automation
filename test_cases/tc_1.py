from test_cases import *


class TC1(MainTc):
    """From client side create a file in a share directory. Condition *(rw, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC1.logger.info(cons.INFO_CREATE + cons.INFO_CONDITION_RW)
        step_1 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_1, TC1, 1)
        Verification.check_work_dir(TC1)
        step_2 = MainTc.touch_file(cons.TEST_FILE_NAME)
        Verification.check_touch_file(step_2, TC1, 2)
        step_3 = MainTc.cat_file(cons.TEST_FILE_NAME)
        Verification.check_cat_file(step_3, TC1, 3)
        Verification.check_list_of_files(TC1)
