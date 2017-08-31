import os
import platform
import base64
import bcrypt
import configparser
from PIL import Image
from resizeimage import resizeimage

if platform.system() == 'Linux':
    import MySQLdb
else:
    import pymysql


def Q(action=None, kwargs=None):
    conf = configparser.RawConfigParser()
    conf.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../db.conf'))
    try:
        if platform.system() == 'Linux':
            conn = MySQLdb.connect(base64.b64decode(conf['Settings']['hostname'][2:-1]).decode('utf-8'),
                                   base64.b64decode(conf['Settings']['user'][2:-1]).decode('utf-8'),
                                   base64.b64decode(conf['Settings']['password'][2:-1]).decode('utf-8'),
                                   base64.b64decode(conf['Settings']['database'][2:-1]).decode('utf-8'))
        else:
            conn = pymysql.connect(base64.b64decode(conf['Settings']['hostname'][2:-1]).decode('utf-8'),
                                   base64.b64decode(conf['Settings']['user'][2:-1]).decode('utf-8'),
                                   base64.b64decode(conf['Settings']['password'][2:-1]).decode('utf-8'),
                                   base64.b64decode(conf['Settings']['database'][2:-1]).decode('utf-8'))
    except:
        return False
    cursor = conn.cursor()
    query = ''
    if action == 'AllClients':
        sql_ctx = "SELECT DISTINCT(client) FROM tbClient ORDER BY client ASC;"
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'AllHw':
        sql_ctx = "SELECT DISTINCT(hardware) FROM tbHardware, tbClient " \
                  "WHERE client='%s' AND tbClient.id_client=tbHardware.id_client " \
                  "ORDER BY hardware ASC;" % kwargs[0]

        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'AllItems':
        sql_ctx = "SELECT DISTINCT(items) FROM tbItems, tbHardware, tbClient " \
                  "WHERE tbHardware.id_hardware=tbItems.id_hardware " \
                  "AND tbClient.id_client=tbItems.id_client " \
                  "AND tbClient.client='%s' ORDER BY items ASC;" % kwargs[0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'tableView':
        sql_ctx = "SELECT tbData.data, tbData.hardware, tbData.item, tbData.it_data " \
                  "FROM tbData, tbClient " \
                  "WHERE tbClient.id_client=tbData.id_client " \
                  "AND client='%s';" % kwargs[0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'check_client':
        sql_ctx = "SELECT client FROM tbClient WHERE client='%s';" % kwargs[0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'new_client':
        sql_ctx = "INSERT INTO tbClient ( client ) VALUE ('%s');" % str(kwargs[0]).upper()
        cursor.execute(sql_ctx)
    if action == 'login':
        sql_ctx = "SELECT tbUser, hash, tbPass FROM tbUsers WHERE tbUser='%s' AND enable='2';" % kwargs[0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'new_line':
        sql_ctx = "SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[3]
        cursor.execute(sql_ctx)
        idclient = cursor.fetchall()
        sql_ctx = "INSERT INTO tbData (hardware, item, it_data, id_client) VALUES ('%s', '%s', '%s', '%s');" % \
                  (kwargs[0], kwargs[1], kwargs[2], idclient[0][0])
        cursor.execute(sql_ctx)
    if action == 'new_hw':
        query = "SELECT id_client from tbClient WHERE client='%s';" % kwargs[1]
        cursor.execute(query)
        idclient = cursor.fetchall()
        cursor.execute("INSERT INTO tbHardware (hardware, id_client) VALUES ('%s', '%s');" % (str(kwargs[0]), int(idclient[0][0])))
    if action == 'new_Item':
        query = "SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[2]
        cursor.execute(query)
        idclient = cursor.fetchall()
        query = "SELECT id_hardware FROM tbHardware WHERE hardware='%s' AND id_client='%s';" % (str(kwargs[1]), str(idclient[0][0]))
        cursor.execute(query)
        idhardware = cursor.fetchall()
        cursor.execute("INSERT INTO tbItems (items, id_hardware, id_client) VALUES ('%s', '%s', '%s');" % (str(kwargs[0]), int(idhardware[0][0]), int(idclient[0][0]),))
    if action == 'update_pwd':
        store_hash = bcrypt.gensalt(12)
        hash_pwd = bcrypt.hashpw(str(kwargs[0]).encode('utf-8'), store_hash)
        sql_ctx = "UPDATE tbUsers SET tbPass=%s, hash=%s WHERE tbUser=%s;"
        cursor.execute(sql_ctx, (hash_pwd.decode('utf-8'), store_hash.decode('utf-8'), kwargs[1]))
        query = cursor.fetchall()
    if action == 'deleteRow':
        query = "DELETE FROM tbData WHERE data='%s' AND hardware='%s' AND item='%s' AND it_data='%s';" % (kwargs[0], kwargs[1], kwargs[2], kwargs[3])
        cursor.execute(query)
    if action == 'deleteItem':
        query = "DELETE FROM tbItems WHERE id_client='%s';" % kwargs[0]
        cursor.execute(query)
    if action == 'deleteHardware':
        query = "DELETE FROM tbHardware WHERE id_client='%s';" % kwargs[0]
        cursor.execute(query)
    if action == 'deleteClient':
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        cursor.execute("DELETE FROM tbGallery WHERE id_client='%s';" % idclient[0][0])
        cursor.execute("DELETE FROM tbData WHERE id_client='%s';" % idclient[0][0])
        cursor.execute("DELETE FROM tbItems WHERE id_client='%s';" % idclient[0][0])
        cursor.execute("DELETE FROM tbHardware WHERE id_client='%s';" % idclient[0][0])
        cursor.execute("DELETE FROM tbClient WHERE client='%s';" % kwargs[0])
    if action == 'deleteItem':
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        query = cursor.execute("SELECT id_hardware FROM tbHardware WHERE hardware='%s' AND id_client='%s';" % (str(kwargs[1]), str(idclient[0][0])))
        idhardware = cursor.fetchall()
        cursor.execute("DELETE FROM tbItems WHERE id_client='%s' AND id_hardware='%s' AND items='%s';" % (idclient[0][0], idhardware[0][0], kwargs[2]))
    if action == 'deleteHardware':
        query = cursor.execute("SELECT id_hardware FROM tbHardware WHERE hardware='%s';" % kwargs[0])
        idhardware = cursor.fetchall()
        cursor.execute("DELETE FROM tbItems WHERE id_hardware='%s'" % (idhardware[0][0]))
        cursor.execute("DELETE FROM tbHardware WHERE hardware='%s'" % kwargs[0])
    if action == 'save_foto':
        conn.insert_id()
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        fd_img = open(kwargs[1], 'r')
        img = Image.open(kwargs[1])
        if int(str(os.stat(kwargs[1]).st_size).strip('L')) > 1048576:
            img = resizeimage.resize_contain(img, [1031, 591])
        img.save('tmp.png')
        fd_img.close()
        with open('tmp.png', "rb") as imageFile:
            image = base64.b64encode(imageFile.read())
        sql_ctx = "INSERT INTO tbGallery (id_client, image) VALUES (%s, %s);"
        cursor.execute(sql_ctx, (int(idclient[0][0]), image))
        os.remove('tmp.png')
    if action == 'load_foto':
        cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        sql_ctx = "SELECT image, id FROM tbGallery WHERE id_client='%s';" % idclient[0][0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'load_hw':
        cursor.execute("SELECT * FROM tbHw;")
        query = cursor.fetchall()
    if action == 'load_item':
        cursor.execute("SELECT * FROM tbIt;")
        query = cursor.fetchall()
    if action == 'load_users':
        cursor.execute("SELECT * FROM tbUsers;")
        query = cursor.fetchall()
    if action == 'load_user':
        cursor.execute("SELECT * FROM tbUsers WHERE tbUser='%s';" % kwargs[0])
        query = cursor.fetchall()
    if action == 'tableView_Img':
         sql_ctx = "SELECT image FROM tbGallery WHERE id=%s;" % kwargs[0]
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'delete_Img':
         sql_ctx = "DELETE FROM tbGallery WHERE id='%s';" % kwargs[0]
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'delete_hw_item':
         sql_ctx = "DELETE FROM tbHw WHERE hw = '%s';" % kwargs[0]
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'delete_it_item':
         sql_ctx = "DELETE FROM tbIt WHERE items = '%s';" % kwargs[0]
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'delete_user':
         sql_ctx = "DELETE FROM tbUsers WHERE tbUser = '%s';" % kwargs[0]
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'save_hw_new':
         sql_ctx = "INSERT INTO tbHw VALUE ('%s');" % str(kwargs[0]).upper()
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'save_it_new':
         sql_ctx = "INSERT INTO tbIt VALUE ('%s');" % str(kwargs[0]).upper()
         cursor.execute(sql_ctx)
         query = cursor.fetchall()
    if action == 'save_new_user':
        store_hash = bcrypt.gensalt(12)
        hash_pwd = bcrypt.hashpw(str(kwargs[1]).encode('utf-8'), store_hash)
        sql_ctx = "INSERT INTO tbUsers (tbUser, tbPass, enable, hash) VALUES (%s, %s, %s, %s);"
        cursor.execute(sql_ctx, (kwargs[0], hash_pwd, int(kwargs[2]), store_hash))
        query = cursor.fetchall()
    if action == 'update_user':
        sql_ctx = "UPDATE tbUsers SET enable='%s' WHERE tbUser='%s';" % (kwargs[1], kwargs[0])
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'log':
        sql_ctx = "INSERT INTO history (log_data, utente, azione) VALUES (now(), '%s', '%s');" % (str(kwargs[0]), str(kwargs[1]))
        cursor.execute(sql_ctx)
    if action == 'allLogs':
        cursor.execute("SELECT * FROM history WHERE log_data BETWEEN ('%s') AND ('%s') ORDER BY log_data DESC;" %
                       (str(kwargs[0]), str(kwargs[1])))
        query = cursor.fetchall()
    if action == 'logs_by':
        cursor.execute("SELECT * FROM history WHERE log_data BETWEEN ('%s') AND ('%s') AND utente='%s' ORDER BY log_data DESC;" %
                       (str(kwargs[0]), str(kwargs[1]), str(kwargs[2])))
        query = cursor.fetchall()
    if action == 'upload':
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        with open(kwargs[1], 'rb') as f:
            buffer = base64.b64encode(f.read())
        sql_ctx = "INSERT INTO tbfiles (id_client, name_file, buffer) VALUES (%s, %s, %s);"
        cursor.execute(sql_ctx, (int(idclient[0][0]), str(kwargs[1]).split('/')[-1], buffer))
    if action == 'files':
        cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        sql_ctx = "SELECT name_file FROM tbfiles WHERE id_client='%s';" % idclient[0][0]
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'load_file':
        cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        sql_ctx = "SELECT buffer FROM tbfiles WHERE id_client='%s' AND name_file='%s';" % (idclient[0][0], kwargs[1])
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
        return query
    if action == 'update_text':
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        buffer = base64.b64encode(str(kwargs[2]).encode('ascii'))
        sql_ctx = "UPDATE tbfiles set buffer=%s WHERE id_client=%s AND name_file=%s;"
        cursor.execute(sql_ctx, (buffer, idclient[0][0], kwargs[1]))
    if action == 'delete_file':
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[0])
        idclient = cursor.fetchall()
        sql_ctx = "DELETE FROM tbfiles WHERE id_client='%s' AND name_file='%s';" % (idclient[0][0], kwargs[1])
        cursor.execute(sql_ctx)
    if action == 'update_conf':
        query = cursor.execute("SELECT id_client FROM tbClient WHERE client='%s';" % kwargs[8])
        idclient = cursor.fetchall()
        sql_ctx = "UPDATE tbData set data=NOW(), hardware='%s', item='%s', it_data='%s' WHERE id_client='%s' AND data='%s' AND hardware='%s' AND item='%s' AND it_data='%s';" % \
                  (kwargs[1], kwargs[2], kwargs[3], idclient[0][0], kwargs[4], kwargs[5], kwargs[6], kwargs[7])
        cursor.execute(sql_ctx)
    if action == 'Total_Clients':
        sql_ctx = "SELECT count(DISTINCT(client)) FROM tbClient;"
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'Total_Images':
        sql_ctx = "SELECT count(DISTINCT(image)) FROM tbGallery;"
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'Total_Attachments':
        sql_ctx = "SELECT count(DISTINCT(name_file)) FROM tbfiles;"
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'license':
        sql_ctx = "SELECT client, name, email, qty_dev, active_date, exp_date, req, lic, server_id, active_lic FROM tbLicense;"
        cursor.execute(sql_ctx)
        query = cursor.fetchall()
    if action == 'insert_lic':
        sql_ctx = "INSERT INTO tbLicense (client, name, email, active_date, exp_date, req, lic, qty_dev) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(sql_ctx, (kwargs[0], kwargs[1], kwargs[2], kwargs[3][-4:]+'-'+kwargs[3][3:5]+'-'+kwargs[3][:2], kwargs[4][-4:]+'-'+kwargs[4][3:5]+'-'+kwargs[4][:2], kwargs[5], kwargs[6], int(kwargs[7])))
    if action == 'delete_lic':
        sql_ctx = "DELETE FROM tbLicense WHERE client=%s AND lic=%s;"
        cursor.execute(sql_ctx, (kwargs[0], kwargs[1]))
    conn.commit()
    conn.close()
    return query
