import main_tc


class Verification(object):

    @staticmethod
    def check_change_dir(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("You changed a directory")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_work_dir(class_name):
        class_name.logger.info(main_tc.MainTc.pwd())

    @staticmethod
    def check_touch_file(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("A file has been created ")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_list_of_files(class_name):
        class_name.logger.info(main_tc.MainTc.ls())

    @staticmethod
    def check_cat_file(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("You look at a file via cat ")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_ssh_to_server(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("Remote command has been successful")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_make_dir(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("The directory has been created ")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_copy(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("The file was copied ")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_rename(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("The file was renamed")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_remove(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("The file was removed")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_move(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("The file was moved ")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_write_into_file(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("Record data into the file has been completed ")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)

    @staticmethod
    def check_read_from_file(class_name, file_name):
        class_name.logger.info('Data inside file is {}'.format(main_tc.MainTc.read_from_file(file_name)))

    @staticmethod
    def check_run_script(step, class_name, number_of_step):
        if not step:
            class_name.logger.debug("Step %d is passed" % number_of_step)
            class_name.logger.info("The file was executed")
        else:
            class_name.logger.debug("Step %d is failed" % number_of_step)
            class_name.logger.error(step)
