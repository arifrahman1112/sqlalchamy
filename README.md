# Simple CRUD for products and product details using SQLAlchemy ORM,
## How to User it- Download the code and run as a python Script


## Create an engine and bind it to the base class with Mysql

mysql+pymysql://UID:PASSWORD@HOST:PORT/SCHEMA?charset=utf8mb4
engine = create_engine('your_database_connection_string')
Base.metadata.create_all(engine)

## Create a session
Session = sessionmaker(bind=engine)
session = Session()

## Create a product and its details
product = Product(name='Example Product')
product.details = ProductDetail(description='Example Description')

## Add the product to the session
session.add(product)
session.commit()

## Query the products and their details
products = session.query(Product).all()
for product in products:
    print("Product Name:", product.name)
    print("Product Detail:", product.details.description)

## Update a product's details
product.details.description = 'New Description'
session.commit()

## Delete a product
session.delete(product)
session.commit()
```
