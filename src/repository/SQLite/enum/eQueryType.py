import enum


class eQueryType(enum.Enum):
    INS = "INSERT"
    SEL = "SELECT"
    UPD = "UPDATE"
    DEL = "DELETE"
    ALT_TBL = "ALTER TABLE"
    ALT_COL = "ALTER COLUMN"