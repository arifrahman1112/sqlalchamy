from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    details = relationship("ProductDetail", uselist=False, back_populates="product")

class ProductDetail(Base):
    __tablename__ = 'product_details'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="details")
