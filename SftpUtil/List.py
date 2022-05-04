import logging

import paramiko

from SftpUtilException import SftpUtilException

logger = logging.getLogger(__name__)

class List:
    """
    SFTPでサーバ上のファイルを取得するクラス。
    ライブラリはparamikoを使用。
    接続エラーはSftpUtilExceptionでラップする。
    """
    def __init__(self, client):
        """
        サーバに接続できる状態のクライアントを指定する
        """
        self.client = client
        logging.debug({'status' : 'init',
                   'param' : {'client' : client}
        })

    def ls(self, path='.'):
        """
        フォルダ内のファイルの一覧を取得する
        """
        logging.debug({'status' : 'run',
            'param' : None
        })
        sftp_connection = self.client.open_sftp()

        # ファイル一覧の取得
        entries = sftp_connection.listdir(path)
        logging.debug({'status' : 'success',
            'param' : None,
            'result' : entries
        })
        return entries