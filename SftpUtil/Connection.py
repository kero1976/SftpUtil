import logging

import paramiko

from SftpUtilException import SftpUtilException

logger = logging.getLogger(__name__)

class Connection:
    """
    SFTPのコネクション作成用のクラス。
    ライブラリはparamikoを使用。
    接続エラーはSftpUtilExceptionでラップする。
    """
    def __init__(self, host='localhost', port=22):
        """
        HOST名とPORT番号を指定する。
        省略時はlocalhostと22を使用する。
        """
        self.host = host
        self.port = port
        logging.debug({'status' : 'init',
                   'param' : {'host' : host, 'port' : port}
        })

    def connect_password(self, name, passwd):
        """
        ユーザ名とパスワードでclientを生成する
        """
        logging.debug({'status' : 'run',
                   'param' : { 'name' : name, 'passwd' : passwd}
        })
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(self.host, port=self.port, username=name, password=passwd)
            logging.debug({'status' : 'success',
                   'param' : { 'name' : name, 'passwd' : passwd}
            })
            return client

        except paramiko.AuthenticationException as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'passwd' : passwd},
                   'message' : "認証エラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

        except paramiko.ssh_exception.NoValidConnectionsError as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'passwd' : passwd},
                   'message' : "接続エラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

        except TimeoutError as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'passwd' : passwd},
                   'message' : "接続エラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

        except Exception as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'passwd' : passwd},
                   'message' : "想定していないエラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

    def connect_keyfile(self,name, keyfile):
        """
        ユーザ名と秘密キーでclientを生成する
        """
        logging.debug({'status' : 'run',
                   'param' : { 'name' : name, 'keyfile' : keyfile}
        })
        try:
            rsa_private_key = paramiko.RSAKey.from_private_key_file(keyfile)
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(self.host, port=self.port, username=name, pkey=rsa_private_key)
            logging.debug({'status' : 'success',
                   'param' : { 'name' : name, 'keyfile' : keyfile}
            })
            return client

        except paramiko.AuthenticationException as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'keyfile' : keyfile},
                   'message' : "認証エラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

        except paramiko.ssh_exception.NoValidConnectionsError as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'keyfile' : keyfile},
                   'message' : "接続エラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

        except TimeoutError as ex:
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'keyfile' : keyfile},
                   'message' : "接続エラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)

        except Exception as ex:
            print(type(ex))
            msg = {'status' : 'fail',
                   'param' : { 'name' : name, 'keyfile' : keyfile},
                   'message' : "想定していないエラー:{}".format(ex)
            }
            logging.debug(msg)
            raise SftpUtilException(msg)