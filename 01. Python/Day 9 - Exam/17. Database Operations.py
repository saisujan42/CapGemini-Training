from abc import ABC, abstractmethod

class DatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass 

class SQLDatabase(DatabaseOperations):
    def insert(self, str):
        print(f"{str} has been Inserted into SQL Database.")
    def update(self, str):
        print(f"{str} has been Updated in SQL Database.")
    def delete(self, str):
        print(f"{str} has been Deleted from SQL Database.")

class NoSQLDatabase(DatabaseOperations):
    def insert(self, str):
        print(f"{str} has been Inserted into NoSQL Database.")
    def update(self, str):
        print(f"{str} has been Updated in NoSQL Database.")
    def delete(self, str):
        print(f"{str} has been Deleted from NoSQL Database.")

def main():
    sql = SQLDatabase()
    nosql = NoSQLDatabase()

    sql.insert("John")
    sql.update("Jack")
    sql.delete("Jack")

    nosql.insert("John")
    nosql.update("Jack")
    nosql.delete("Jack")
main()