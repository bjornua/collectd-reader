# -*- coding: utf-8 -*-
from app.utils.misc import template_response,local
import app.model.data as data
import json

import logging
log = logging.getLogger(__name__)

def viewer():
    template_response("/page/graphviewer.mako")

def metadatajson():
    local.response.data = json.dumps(list(data.itermetadata()))

def datajson():
    id_list = local.request.args.get("id", "")
    id_list = id_list.split(",")

    try:
        id_list = [int(x) for x in id_list]
    except ValueError:
        id_list = []
    
    try:
        start = float(local.request.args.get("start", ""))
        start /= 1000
    except ValueError:
        start = None
    
    try:
        end = float(local.request.args.get("end", ""))
        end /= 1000
    except ValueError:
        end = None
    
    log.info(start)
    log.info(end)

    local.response.data = json.dumps(data.getdata(id_list, start=start, end=end))
