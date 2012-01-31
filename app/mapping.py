# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.index
import app.controllers.error

endpts = {
# Normal endpoints
    "index": app.controllers.index.index,
    "testpage0": app.controllers.index.testpage0,
    "testpage1": app.controllers.index.testpage1,
    "testpage2": app.controllers.index.testpage2,
    "testpage3": app.controllers.index.testpage3,

# System endpoints
    "notfound": app.controllers.error.notfound,
    "error": app.controllers.error.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "index"),
        ("GET", "/testpage0", "testpage0"),
        ("GET", "/testpage1", "testpage1"),
        ("GET", "/testpage2", "testpage2"),
        ("GET", "/testpage3", "testpage3"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
