import logging

import paramiko

from SftpUtilException import SftpUtilException

logger = logging.getLogger(__name__)

class Put:
    """
    SFTPでファイルを送信するクラス。
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

    def put(self, localpath, remotepath):
        """
        ファイルをPUTする。
        """
        logging.debug({'status' : 'run',
            'param' : {'localpath' : localpath,
                       'remotopath' : remotepath}
        })
        session = self.client.open_sftp()

        # ファイルを一時ファイル名で送信する
        self.__tmpput(session, localpath, remotepath)

        # ファイル名を変更する
        self.__rename(session, remotepath)

        logging.debug({'status' : 'success',
            'param' : {'localpath' : localpath,
                       'remotopath' : remotepath}
        })

    def __tmpput(self, session, localpath, remotepath):
        """
        privateメソッド
        一時的な名前として末尾に.tmpを付けてPUTする
        """
        logging.debug({'status' : 'run',
            'param' : {'session' : session,
                       'localpath' : localpath,
                       'remotopath' : remotepath}
        })
        try:
            session.put(localpath, remotepath + '.tmp')
            logging.debug({'status' : 'success',
                'param' : {'localpath' : localpath,
                           'remotopath' : remotepath}
            })

        except Exception as ex:
            msg = {'status' : 'fail',
                   'param' : {'localpath' : localpath,
                              'remotopath' : remotepath},
                   'message' : "一時ファイルのPUT処理でエラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

    def __rename(self, session, remotepath):
        """
        privateメソッド
        リモート上のファイル名からtmpを削除する
        """
        logging.debug({'status' : 'run',
            'param' : {'session' : session,
                       'remotopath' : remotepath}
        })
        try:
            session.rename(remotepath + '.tmp', remotepath)
            logging.debug({'status' : 'success',
                'param' : {'session' : session,
                           'remotopath' : remotepath}
            })

        except Exception as ex:
            msg = {'status' : 'fail',
                   'param' : {'session' : session,
                              'remotopath' : remotepath},
                   'message' : "リネーム処理でエラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)