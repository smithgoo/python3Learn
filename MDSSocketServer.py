
# coding=utf-8
import socketserver



class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                data = str(conn.recv(1024),'ascii')
            except:
                print('error')

            if data and len(data)>0:
                print(data)
                temp = ('你输入的是' + data).encode()
                print(temp)
                conn.sendall(temp)



if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',7279),MyServer)
    server.serve_forever()
