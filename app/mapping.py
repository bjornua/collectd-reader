# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.collector
import app.controllers.viewer
import app.controllers.error

endpts = {
# Normal endpoints
    "viewer": app.controllers.viewer.viewer,
    "metadatajson": app.controllers.viewer.metadatajson,
    "datajson": app.controllers.viewer.datajson,
    "collect": app.controllers.collector.collect,

# System endpoints
    "notfound": app.controllers.error.notfound,
    "error": app.controllers.error.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "viewer"),
        ("POST", "/collect", "collect"),
        ("GET", "/metadata.json", "metadatajson"),
        ("GET", "/data.json", "datajson"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
