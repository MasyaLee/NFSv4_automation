import paramiko
import subprocess


class Precondition(object):

    @staticmethod
    def put_file(machine_name, user_name, dir_name, filename, data):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(machine_name, username=user_name)
        sftp = ssh.open_sftp()
        try:
            sftp.mkdir(dir_name)
        except IOError:
            pass
        f = sftp.open(dir_name + '/' + filename, 'w')
        f.write(data)
        f.close()
        ssh.close()

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
