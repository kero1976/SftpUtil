import pytest

from SftpUtilException import SftpUtilException

def test_getMessage():

    msg = {'status' : 'fail',
            'param' : 'ABC',
            'message' : "認証エラー"
    }
    ex = SftpUtilException(msg)

    assert ex.getMessage() == "認証エラー"
