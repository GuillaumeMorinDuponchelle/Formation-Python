# -*- coding. utf-8 -*-
import argparse
import configparser
import logging
import logging.config
import mysql.connector 

if __name__ == "__main__":
    logging.warning("start")
    parser = argparse.ArgumentParser()
    config = configparser.ConfigParser()
    
    parser.add_argument('-c','--conf', help="database configuration file",default="config.ini")
    args = parser.parse_args()
    
    #log
    logging.config.fileConfig(args.conf)
    logger = logging.getLogger('theLogger')
    logger.debug("ok chargement logger")
    #print(args.conf)
    
    config.read(args.conf)
    host = config['database']['host']
    port=config['database']['port']
    username=config['database']['username']
    password=config['database']['password']
    database=config['database']['database']

    logger.debug("ok chargement config")
    logger.debug("database host"+host)
    print(username,host,port,database)

    theConf = {
            'user':username,
            'password':password,
            'port':port,
            'host':host,
            'database':database
    }

    cnx = mysql.connector.connect(**theConf)
    logger.debug("ok connexion db")
    cursor = cnx.cursor()
    sql= "SELECT * FROM todos.tasks"
    cursor.execute(sql)
    for (id,action,done) in cursor:
        print(id,action,done)
    cnx.close()