import subprocess
import constants as cons


class Annihilator(object):
    @staticmethod
    def clear_share_dir():
        command = subprocess.Popen(["ssh -T " + cons.SERVER_NAME + '@' + cons.SERVER_IP + ' ' +
                                    cons.ANNIHILATE_ON_SERVER], shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            error = command.stderr.readlines()
            print >> command.stderr, "ERROR: %s" % error
        else:
            print result

    @staticmethod
    def remove_test_dir():
            subprocess.call([cons.ANNIHILATE_TEST_DIR], shell=True)
