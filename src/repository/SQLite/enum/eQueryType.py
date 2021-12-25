import enum


class eQueryType(enum.Enum):
    INS = "INSERT INTO"
    SEL = "SELECT"
    UPD = "UPDATE TABLE"
    DEL = "DELETE"
    ALT_TBL = "ALTER TABLE"
    ALT_COL = "ALTER COLUMN"