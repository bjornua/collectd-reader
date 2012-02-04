# -*- coding: utf-8 -*-
from app.utils.misc import sqlitedb

import logging

log = logging.getLogger(__name__)

def itermetadata():
    for x in sqlitedb().execute("""
        SELECT
            "host", "plugin", "plugin_instance", "type",
            "type_instance", "dsname", "dstype", "id"
        FROM "metadata"
        ORDER BY
            "host", "plugin", "plugin_instance", "type",
           "type_instance", "dsname", "dstype"
        """
    ):
        doc = {
            "host"           : x[0],
            "plugin"         : x[1],
            "plugin_instance": x[2],
            "type"           : x[3],
            "type_instance"  : x[4],
            "dsname"         : x[5],
            "dstype"         : x[6],
            "id"             : x[7]
        }
        yield doc

def getdata(metadata_ids, *args, **kwargs):
    out = []
    for metadata_id in metadata_ids:
        out.append(list(iterdata(metadata_id, *args,**kwargs)))
    return out

def iterdata(metadata_id, resolution=200, start=None, end=None):
    timesql = ''
    timeparams = []
    if start != None:
        timeparams.append(start)
        timesql += 'and "time" >= ?'
    if end != None:
        timeparams.append(end)
        timesql += 'and "time" <= ?'

    timeparams = tuple(timeparams)
    
    if resolution != None:
        sql = 'SELECT max("time")-min("time")'
        sql += 'FROM "data" where "metadata" = ?'
        sql += timesql
        for row in sqlitedb().execute(sql, (metadata_id,)+timeparams):
            timediff = row[0]
        
        timediff = timediff/resolution
        
        sql = 'SELECT avg("time")*1000, avg("value")'
        sql += 'FROM "data"'
        sql += 'WHERE "metadata" = ?'
        sql += timesql
        sql += 'GROUP BY round("time"/?)'
        sql += 'ORDER BY "time"'

        for row in sqlitedb().execute(sql, (metadata_id,)+timeparams+(timediff,)):
            yield row[0],row[1]
    else:
        sql = 'SELECT "time"*1000, "value" FROM "data" WHERE "metadata" = ?'
        sql += timesql
        sql += 'ORDER BY "time"'
        for row in sqlitedb().execute(sql, (metadata_id,)+timeparams):
            yield row[0],row[1]
