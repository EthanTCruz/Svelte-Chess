from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Uncomment this connector to use a mariadb database
#connector = "mariadb+mariadbconnector"

#Uncomment this one to use a mysql database
connector = "mysql+pymysql"

engine = create_engine(
    f"{connector}://root:root@localhost/svelte-chess-db",connect_args= dict(host='localhost', port=3306)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
