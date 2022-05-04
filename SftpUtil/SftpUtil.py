import logging

import paramiko

from Connection import Connection
from List import List
from Put import Put
from SftpUtilException import SftpUtilException

logger = logging.getLogger(__name__)

formatter = "%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter)

try:
    logging.debug('client作成')
    #client = Connection('192.168.50.168',22).connect_password('sftpuser','sftpPassw0rd')
    keyfile = 'C:\\Users\\kero\\.ssh\\SFTP\\id_rsa'
    client = Connection('13.113.153.47',22).connect_keyfile('sftp-user',keyfile)
    list = List(client)
    files = list.ls('sftp-work-dir')

    print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
    for e in files:
        print(e)
    print('↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑')

    # ファイルのアップロード
    put = Put(client).put('D:\\test\\aaa.txt','sftp-work-dir/aaa.txt')
except Exception as ex:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(ex)
finally:
    client.close()