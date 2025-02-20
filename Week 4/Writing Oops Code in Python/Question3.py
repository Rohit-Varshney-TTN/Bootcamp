class Database:
    instance=None
    def __new__(cls):
        if cls.instance is None:
            cls.instance=super(Database,cls).__new__(cls) 
        return cls.instance

    def connect(self):
        return "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)

print(db1.connect())
print(db2.connect())