import mysql.connector
from mysql_creds import speedsniper
import time
import datetime


def upload_scans(plates):
    cnx = mysql.connector.connect(**speedsniper)
    cursor = cnx.cursor()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    query = ("INSERT INTO `speedsniper`.`scans` (`id`,`time`,`plate`,`speed`) VALUES (%s, %s, %s, %s)")

    for plate in plates:
        print("plate: " + plate)
        cursor.execute(query, (0, timestamp, plate, 0))

    cnx.commit()

    cnx.close()


