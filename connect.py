import datetime
from bson import ObjectId
from pymongo import MongoClient
from sqlalchemy import create_engine, Table, Column, MetaData, String
from sqlalchemy.orm import sessionmaker

config = {
    "mysql": {
        "host": "localhost",
        "user": "root",
        "password": "snoopy1230465",
        "database": "trial308"
    },
    "mongodb": {
        "host": "localhost",
        "port": 27017,
        "database": "Flight Database"
    }
}

def connectDB():
    connection_string = "mongodb+srv://asfafeeroze:1234@cluster0.zj78qtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_string)
    db = client.Cluster0
    print("Connection established to your db")
    return db

def connect_mysql():
    mysql_config = config['mysql']
    engine = create_engine(f'mysql+mysqlconnector://{mysql_config["user"]}:{mysql_config["password"]}@{mysql_config["host"]}/{mysql_config["database"]}')
    Session = sessionmaker(bind=engine)
    if Session: 
        print("Connection established to MySQL")
    return engine, Session()

def fetch_data_from_mongodb(db, collection_name):
    collection = db[collection_name]
    data = list(collection.find({}))
    print(f"Fetched {len(data)} records from MongoDB.")
    return data

def create_table_and_insert_data(engine, data, table_name):
    if not data:
        print("No data to insert.")
        return

    metadata = MetaData()
    first_record = data[0]

    # Define columns dynamically based on the first record
    columns = [Column('_id', String(255), primary_key=True)]  # Handle MongoDB ObjectId as primary key
    for key in first_record.keys():
        if key != '_id':  # Avoid redefining the primary key
            columns.append(Column(key, String(255)))  # Use String(255) for all other fields

    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)

    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            for record in data:
                # Convert all values to strings
                record = {k: str(v) for k, v in record.items()}
                
                # Debug: Print the record before insertion
                print(f"Inserting record: {record}")
                
                connection.execute(table.insert().values(**record))
            transaction.commit()
            print(f"Data inserted into MySQL table '{table_name}' successfully.")
        except Exception as e:
            print(f"Failed to insert data: {e}")
            transaction.rollback()

# def main():
#     db = connectDB()
#     engine, session = connect_mysql()
#
#     # Example: Transfer 'admins' from MongoDB to a new MySQL table 'admins_sql'
#     collection_name = 'passenger_info'  # Adjust the collection name as needed
#     data = fetch_data_from_mongodb(db, collection_name)
#     if data:
#         print(f"Fetched {len(data)} documents from MongoDB collection '{collection_name}'")
#         create_table_and_insert_data(engine, data, 'passengers_sql')  # Adjust the SQL table name as needed
#     else:
#         print(f"No data found in MongoDB collection '{collection_name}'")
#
# if __name__ == '__main__':
#     main()
