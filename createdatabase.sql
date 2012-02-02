CREATE TABLE IF NOT EXISTS "metadata"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "host" TEXT,
    "plugin" TEXT,
    "plugin_instance" TEXT,
    "type" TEXT,
    "type_instance" TEXT,
    "dsname" TEXT,
    "dstype" TEXT,
    UNIQUE ("host", "type", "type_instance", "plugin","plugin_instance","dsname","dstype")
);

CREATE TABLE IF NOT EXISTS "data" (
    "metadata" INTEGER,
    "time" REAL,
    "value" REAL,
    PRIMARY KEY ("metadata", "time")
);
