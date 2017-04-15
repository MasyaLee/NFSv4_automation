import subprocess
import os


class MainTc(object):

    @staticmethod
    def change_directory(path):
        str_path = str(path)
        try:
            os.chdir(str_path)
            return 0
        except StandardError as Error:
            return str(Error)

    @staticmethod
    def pwd():
        command = subprocess.check_output(["pwd"], shell=True)
        return "Your work directory is {} ".format(command)

    @staticmethod
    def ls():
        command = subprocess.check_output(["ls"], shell=True)
        return "A list of files in current directory: \n {} ".format(command)

    @staticmethod
    def make_dir(dir_name):
        str_dir_name = str(dir_name)
        try:
            subprocess.check_output(["mkdir " + str_dir_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def remove_dir(dir_name):
        str_dir_name = str(dir_name)
        try:
            subprocess.check_output(["rmdir ./" + str_dir_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def touch_file(file_name):
        str_file_name = str(file_name)
        try:
            subprocess.check_output(["touch ./" + str_file_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def write_into_file(file_name, data):
        str_data = str(data)
        try:
            with open(file_name, 'w') as _:
                subprocess.call(['echo', str_data], stdout=_)
            return 0
        except StandardError as Error:
            return str(Error)

    @staticmethod
    def read_from_file(file_name):
        list_data = []
        with open(file_name, 'r') as _:
            for line in _:
                list_data.append(line)
        return list_data

    @staticmethod
    def cat_file(file_name):
        str_path_to_file = str(file_name)
        try:
            subprocess.check_output(["cat " + str_path_to_file], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def copy_file(file_name, path_for_copy):
        str_file_name = str(file_name)
        str_path_for_copy = str(path_for_copy)
        try:
            subprocess.check_output(["cp " + str_file_name + " " + str_path_for_copy], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def move_file(file_name, path_for_move):
        str_file_name = str(file_name)
        str_path_for_move = str(path_for_move)
        try:
            subprocess.check_output(["mv " + str_file_name + " " + str_path_for_move], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def rename_file(file_name, new_file_name):
        return MainTc.move_file(file_name, new_file_name)

    @staticmethod
    def remove_file(file_name):
        str_file_name = str(file_name)
        str_without_asterisk = (str_file_name.replace('*', ''))
        try:
            subprocess.check_output(["rm -f ./" + str_without_asterisk], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def run_script(name_scr):
        str_name_scr = str(name_scr)
        try:
            subprocess.check_output(["sh " + str_name_scr], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def ssh_to_server(server_name, server_ip, remote_command):
        str_server_ip = str(server_ip)
        str_server_name = str(server_name)
        command = subprocess.Popen(["ssh -T " + str_server_name + '@' + str_server_ip + ' ' + remote_command],
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            print >> command.stderr, "ERROR: %s" % error
        else:
            print result
