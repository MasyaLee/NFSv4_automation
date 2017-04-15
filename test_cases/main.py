from test_cases import *

if __name__ == '__main__':

    '''primary condition'''
    Precondition.put_file(cons.SERVER_IP, cons.SERVER_NAME, cons.DIR_FOR_CONDITION, cons.FILE_FOR_CONDITION,
                          cons.CHANGE_PRECONDITION_TO_RW)
    Precondition.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_RERUN_NFS)

    TC1.run_tc()
    Annihilator.clear_share_dir()
    TC2.run_tc()
    Annihilator.clear_share_dir()
    TC3.run_tc()
    Annihilator.clear_share_dir()
    TC4.run_tc()
    Annihilator.clear_share_dir()
    Annihilator.remove_test_dir()
    TC5.run_tc()
    Annihilator.clear_share_dir()
    Annihilator.remove_test_dir()
    TC6.run_tc()
    Annihilator.clear_share_dir()

    '''change condition'''
    Precondition.put_file(cons.SERVER_IP, cons.SERVER_NAME, cons.DIR_FOR_CONDITION, cons.FILE_FOR_CONDITION,
                          cons.CHANGE_PRECONDITION_TO_RO)
    Precondition.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_RERUN_NFS)

    TC7.run_tc()
    Annihilator.clear_share_dir()
    Annihilator.remove_test_dir()
    TC8.run_tc()
    Annihilator.clear_share_dir()
    TC9.run_tc()
    Annihilator.clear_share_dir()
    TC10.run_tc()
    Annihilator.clear_share_dir()

    '''return to primary condition'''
    Precondition.put_file(cons.SERVER_IP, cons.SERVER_NAME, cons.DIR_FOR_CONDITION, cons.FILE_FOR_CONDITION,
                          cons.CHANGE_PRECONDITION_TO_RW)
    Precondition.ssh_to_server(cons.SERVER_NAME, cons.SERVER_IP, cons.REMOTE_RERUN_NFS)
