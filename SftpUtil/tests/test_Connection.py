import pytest

from Connection import Connection
from SftpUtilException import SftpUtilException

def test_connect_password_passing():

    connect = Connection('192.168.50.168',22)
    client = connect.connect_password('sftpuser','sftpPassw0rd')
    assert client != None

def test_connect_password_connect_fail():

    connect = Connection('192.168.150.168',22)
    with pytest.raises(SftpUtilException) as ex:
        client = connect.connect_password('sftpuser','sftpPassw0rd')
    assert '接続エラー' in ex.value.getMessage()

def test_connect_password_connect_fail2():

    connect = Connection('192.168.50.168',122)
    with pytest.raises(SftpUtilException) as ex:
        client = connect.connect_password('sftpuser','sftpPassw0rd')
    assert '接続エラー' in ex.value.getMessage()

def test_connect_password_assert_fail():

    connect = Connection('192.168.50.168',22)
    with pytest.raises(SftpUtilException) as ex:
        client = connect.connect_password('sftpuser2','sftpPassw0rd')
    assert '認証エラー' in ex.value.getMessage()