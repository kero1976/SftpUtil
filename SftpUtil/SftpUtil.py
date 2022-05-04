import logging

import paramiko

from Connection import Connection
from List import List
from SftpUtilException import SftpUtilException

logger = logging.getLogger(__name__)

formatter = "%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"
logging.basicConfig(level=logging.DEBUG, format=formatter)

try:
    logging.debug('client作成')
    client = Connection('192.168.50.168',22).connect_password('sftpuser','sftpPassw0rd')

    list = List(client)
    files = list.ls()

    for e in files:
        print(e)

    # ファイルのダウンロード
    sftp_connection.get('sample.txt', 'sample.txt')
except Exception as ex:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(ex)
finally:
    client.close()