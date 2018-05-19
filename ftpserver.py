from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345",r"D:\Masa Masa Kuliah\Semester 6\KIJ\FTP\FTP Client Server RSA in C\upload", perm="elradfmw")
authorizer.add_anonymous(r"D:\Masa Masa Kuliah\Semester 6\KIJ\FTP\FTP Client Server RSA in C", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()