#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# autor: Carlos Rueda
# fecha: 2015-12-04
# mail: carlos.rueda@deimos-space.com

import datetime
import time
import os
import sys

import MySQLdb as mdb

import logging, logging.handlers

########################################################################
# configuracion y variables globales
from configobj import ConfigObj
config = ConfigObj('./check_distance.properties')

LOG = config['directory_logs'] + "/check.log"
LOG_FOR_ROTATE = 10

DB_IP = config['mysql_host']
DB_PORT = config['mysql_port']
DB_NAME = config['mysql_db_name']
DB_USER = config['mysql_user']
DBPASSWORD = config['mysql_passwd']

########################################################################
# definicion y configuracion de logs
try:
    logger = logging.getLogger('check_distance')
    loggerHandler = logging.handlers.TimedRotatingFileHandler(LOG , 'midnight', 1, backupCount=LOG_FOR_ROTATE)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    loggerHandler.setFormatter(formatter)
    logger.addHandler(loggerHandler)
    logger.setLevel(logging.DEBUG)
except Exception, error:
    logger.error( '------------------------------------------------------------------')
    logger.error( '[ERROR] Error writing log at ' + str(error))
    logger.error( '------------------------------------------------------------------')
    exit()
########################################################################

def main():
	con = mdb.connect(DB_IP, DB_USER, DB_PASSWORD, DB_NAME)

	cur = con.cursor()
	cur.execute("select TRACKING_1.VEHICLE_LICENSE,HEADING,GPS_SPEED,POS_LATITUDE_DEGREE,POS_LATITUDE_MIN,POS_LONGITUDE_DEGREE,POS_LONGITUDE_MIN,POS_DATE from TRACKING_1, HAS where TRACKING_1.VEHICLE_LICENSE = HAS.VEHICLE_LICENSE and HAS.FLEET_ID="+FLEET_ID)

	objects_list = []

	numrows = int(cur.rowcount)
	for i in range(numrows):
		row = cur.fetchone()


		

if __name__ == '__main__':
    main()
