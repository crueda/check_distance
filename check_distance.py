#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# autor: Carlos Rueda
# fecha: 2015-12-04
# mail: carlos.rueda@deimos-space.com

import datetime
import time
import os
import sys
from scipy import spatial
import numpy as np

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
DB_PASSWORD = config['mysql_passwd']

def main():    
    con = mdb.connect(DB_IP, DB_USER, DB_PASSWORD, DB_NAME)

    cur = con.cursor()
    cur.execute("select LATITUDE, LONGITUDE from STAGE_ROUTE")

    print "paso 1:" + str(datetime.datetime.utcnow())
    L = []
    numrows = int(cur.rowcount)
    for i in range(numrows):
        row = cur.fetchone()
        L.append(row)

    pt = [47, 5] 
    print "paso 2:" + str(datetime.datetime.utcnow())
    L[spatial.KDTree(L).query(pt)[1]]  
    distance,index = spatial.KDTree(L).query(pt)

    #print distance 
    #print index
    #print L[index]

    print "paso 3:" + str(datetime.datetime.utcnow())


if __name__ == '__main__':
    main()
