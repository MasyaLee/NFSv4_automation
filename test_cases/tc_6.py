from test_cases import *


class TC6(MainTc):
    """From client side execute a file in a share directory. Condition *(rw, sync)"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_tc():
        TC6.logger.info(cons.INFO_EXECUTE + cons.INFO_CONDITION_RW)
        step_1 = MainTc.change_directory(cons.CLIENT_PATH_TO_SHARE)
        Verification.check_change_dir(step_1, TC6, 1)
        Verification.check_work_dir(TC6)
        step_2 = MainTc.touch_file(cons.TEST_FILE_NAME)
        Verification.check_touch_file(step_2, TC6, 2)
        Verification.check_list_of_files(TC6)
        step_3 = MainTc.write_into_file(cons.TEST_FILE_NAME, cons.SCRIPT_DATA)
        Verification.check_write_into_file(step_3, TC6, 3)
        Verification.check_read_from_file(TC6, cons.TEST_FILE_NAME)
        step_4 = MainTc.run_script(cons.TEST_FILE_NAME)
        Verification.check_run_script(step_4, TC6, 4)
