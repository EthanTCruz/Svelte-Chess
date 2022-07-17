from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1/svelte-chess-db?host=localhost?port=3306"
#mysql+mysqlconnector://root@localhost:3306/svelte-chess-db
engine = create_engine(
    "mysql+pymysql://root:root@localhost/svelte-chess-db",connect_args= dict(host='localhost', port=3306)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
