from app import database


def get_session():
    session = database.SessionLocal()
    try:
        yield session
    finally:
        session.close()
