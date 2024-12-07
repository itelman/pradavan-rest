from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///storage/storage.db"
engine = create_engine(DATABASE_URL)


@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def NewSQL() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
