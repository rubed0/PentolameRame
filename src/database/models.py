from sqlalchemy import Column, String, Float, Text, create_engine
from sqlalchemy.orm import declarative_base
from pathlib import Path


Base = declarative_base()


class Listing(Base):
    __tablename__ = 'listings'

    id = Column(String, primary_key = True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    location = Column(String)
    url = Column(String, nullable=False)
    platform = Column(String)
    photos = Column(JSON, nullable=False, default=list)
    price_history = Column(JSON, default=list)

    def add_price(self, price: float):
        timestamp = datetime.utcnow().isoformat()
        self.price_history.append({"price": price, "timestamp": timestamp})

    def add_photo(self, photo_path: str):
        self.photos.append(photo_path)

    def get_latest_price(self):
        if not self.price_history:
            return None
        return self.price_history[-1]["price"]

    def __repr__(self):
        return f"<Listing {self.title} - {self.price}€>"
