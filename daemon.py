#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socketserver
import MySQLdb

HOST = 'IP.ADDRESS.SERVER.DB'
PORT = 9999

conn = MySQLdb.connect('IP.ADDRESS.SERVER.DB', 'USER_DB', 'PASSWORD_DB', 'NAME_DB')


def query(action=None, kwargs=None):
    cursor = conn.cursor()
    query = ''
    if action == 'check_req':
        sql_ctx = "SELECT req FROM tbLicense WHERE lic='%s';" % kwargs[0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'check_lic':
        sql_ctx = "SELECT lic FROM tbLicense WHERE req='%s';" % kwargs[0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'active':
        sql_ctx = "SELECT active_lic, client, name, qty_dev, exp_date FROM tbLicense WHERE req='%s' AND lic='%s';" % (kwargs[0], kwargs[1])
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'register':
        sql_ctx = "UPDATE tbLicense SET active_lic='1', server_id='%s', pwd_client='%s' WHERE req='%s' and lic='%s';" \
                  % (kwargs[2], kwargs[3], kwargs[0], kwargs[1])
        cursor.execute(sql_ctx)
    conn.commit()
    return query


class Service(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            self.data = self.request.recv(1024).strip()
            req = str(self.data, 'utf-8').split("/")[2]
            lic = str(self.data, 'utf-8').split("/")[3]
            pwd = str(self.data, 'utf-8').split("/")[4]
            srv_id = str(self.data, 'utf-8').split("/")[5][:32]
            check_req = query(action="check_req", kwargs=[lic])
            check_lic = query(action="check_lic", kwargs=[req])
            active = query(action='active', kwargs=[req, lic])
            print("\nReceived license:\nReq: %s\nLic: %s\nServer ID: %s\nPwd: %s\n" % (req, lic, srv_id, pwd))
            if len(check_req) is 0 or len(check_lic[0][0]) is None:
                self.request.sendall(bytes('1'.encode('utf-8')))
            else:
                if active[0][0] is 1:
                    self.request.sendall(bytes('2'.encode('utf-8')))
                else:
                    if check_lic[0][0] == lic and check_req[0][0] == req:
                        query(action='register', kwargs=[req, lic, srv_id, pwd])
                        ctx = '0,%s,%s,%s,%s' % (active[0][1], active[0][2], active[0][3], active[0][4])
                        self.request.sendall(bytes(ctx.encode('utf-8')))
                    else:
                        self.request.sendall(bytes('1'.encode('utf-8')))
        except:
            print("Nothing to do... {}".format(str(self.data, 'utf-8')))

if __name__ == "__main__":
    try:
        server = socketserver.TCPServer((HOST, PORT), Service)
        print("Service starting at %s listening port %s" % (HOST, PORT))
        server.serve_forever()
    except:
        print("The port is already in use, stop or kill the other process")
