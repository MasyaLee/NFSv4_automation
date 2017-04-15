CLIENT_PATH_TO_SHARE = '/mnt/share/'
SERVER_PATH_TO_SHARE = '/share/'
PATH_TO_LOGGER = '/home/masya/Masyalee/PyCharm_projects/NFSv4_share/'
PATH_TO_TEST_DIR = '/home/masya/Masyalee/PyCharm_projects/NFSv4_share/'

TEST_FILE_NAME = 'TESTFILE'
TEST_FILE_2_NAME = 'TESTFILE_2'
TEST_DIR_NAME = 'TESTDIR'
SCRIPT_DATA = 'echo "May_the_force_be_with_you!"'

SERVER_NAME = 'root'
SERVER_IP = '192.168.0.106'

REMOTE_TOUCH = 'touch '
CHANGE_PRECONDITION_TO_RO = '/share *(ro,sync)'
CHANGE_PRECONDITION_TO_RW = '/share *(rw,sync)'
REMOTE_RERUN_NFS = 'exportfs -arv'
DIR_FOR_CONDITION = '/etc'
FILE_FOR_CONDITION = '/exports'

ANNIHILATE_ON_SERVER = 'rm -f /share/*'
ANNIHILATE_TEST_DIR = 'rm -rf /home/masya/Masyalee/PyCharm_projects/NFSv4_share/TESTDIR'

INFO_CONDITION_RO = 'Condition *(ro, sync)'
INFO_CONDITION_RW = 'Condition *(rw, sync)'
INFO_CREATE = 'Create a file in a share directory. '
INFO_RENAME = 'Rename a file from a share directory. '
INFO_REMOVE = 'Remove a file from a share directory. '
INFO_COPY = 'Copy a file to a share directory. '
INFO_MOVE = 'Move a file into a share directory. '
INFO_EXECUTE = 'Execute a file from a share directory. '
INFO_WRITE_DATA = 'Write data into a file from a share directory. '

