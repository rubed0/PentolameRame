from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base
from .models import Listing


DATABASE_PATH = "~/.pentolamerame/listings.db"
engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)

def add_listing(listing: Listing):
    session = Session()
    try:
        session.add(listing)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def remove_listing(listing_id: int):
    session = Session()
    try:
        listing = session.query(Listing).get(listing_id)
        if listing:
            session.delete(listing)
            session.commit()
    except Exception as e:
        session.rollback()
        raise e:
    finally:
        session.close()

def find_listing_by_id(listing_id: int) -> Listing | None:
    session = Session()
    try:
        return session.query(Listing).get(listing_id)
    finally:
        session.close()

def update_listing(listing_id: int, new_data: dict):
    session = Session()
    try:
        listing = session.query(Listing).get(listing_id)
        if listing:
            for key, value in new_data.items():
                setattr(listing, key, value)
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


