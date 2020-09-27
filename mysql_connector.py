import mysql.connector
from mysql_creds import speedsniper
import time
import datetime


def getTimestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def upload_scans(plates):
    cnx = mysql.connector.connect(**speedsniper)
    cursor = cnx.cursor()

    query = ("INSERT INTO `speedsniper`.`scans` (`id`,`time`,`plate`,`speed`) VALUES (%s, %s, %s, %s)")

    for plate in plates:
        print("plate: " + plate)
        cursor.execute(query, (0, getTimestamp(), plate, 0))

    cnx.commit()
    cnx.close()


def upload_home_string(message):
    cnx = mysql.connector.connect(**speedsniper)
    cursor = cnx.cursor()

    query = ("""
UPDATE `speedsniper`.`messages`
SET
`message` = %s,
`updated` = %s
WHERE `id` = "Home"
""")

    cursor.execute(query, (message, getTimestamp()))

    cnx.commit()
    cnx.close()


def upload_business_string(message):
    cnx = mysql.connector.connect(**speedsniper)
    cursor = cnx.cursor()

    query = ("""
UPDATE `speedsniper`.`messages`
SET
`message` = %s,
`updated` = %s
WHERE `id` = "Business"
""")

    cursor.execute(query, (message, getTimestamp()))

    cnx.commit()
    cnx.close()


if __name__ == "__main__":
    upload_home_string("Testing")
    upload_business_string("Testing")