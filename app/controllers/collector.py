# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect, sqlitedb

import pprint
import logging
import json

log = logging.getLogger(__name__)


def collect():
    entries = json.loads(local.request.data)
    
    for entry in entries:
        dsnames         = entry["dsnames"]
        dstypes         = entry["dstypes"]
        host            = entry["host"]
        plugin          = entry["plugin"]
        plugin_instance = entry["plugin_instance"]
        type_           = entry["type"]
        type_instance   = entry["type_instance"]

        time = entry["time"]
        values = entry["values"]
        
        if len(dsnames) != len(dstypes) or len(dstypes) != len(values):
            error.log("Length mismatch (dsname, dstype, value): %s", repr(data))
        
        for dstype, dsname, value in zip(dstypes,dsnames,values):
            metadata_id = None
            with sqlitedb() as db:
                for row in db.execute("""
                    SELECT "id" FROM "metadata" WHERE
                        "dsname" = ? and
                        "dstype" = ? and
                        "host" = ? and
                        "plugin" = ? and
                        "plugin_instance" = ? and
                        "type" = ? and
                        "type_instance" = ?
                        LIMIT 1
                """, (
                        dsname, dstype, host, plugin, plugin_instance, type_,
                        type_instance
                )):
                    metadata_id = row[0]

                if metadata_id == None:
                    metadata_id = db.execute("""
                        INSERT INTO "metadata" (
                            "dsname", "dstype", "host", "plugin",
                            "plugin_instance", "type", "type_instance"
                        ) VALUES(?,?,?,?,?,?,?)
                    """, (
                        dsname, dstype, host, plugin, plugin_instance, type_,
                        type_instance
                    )).lastrowid
                    
                db.execute("""
                    INSERT INTO "data" (
                        "metadata", "time", "value"
                    ) VALUES(?,?,?)
                """, (
                    metadata_id, time, value
                ))

    
    

#    db().save_doc(metadata)


def testpage0():
    template_response("/error/notyet.mako")
