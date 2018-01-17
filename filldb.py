from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('postgresql://postgres:postgres@localhost/sportsapp')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Esraa Qandeel", email="esraamedhatesamir@gmail.com",
             picture="https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg")
session.add(User1)
session.commit()

# Items for Soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

Item1 = Item(user_id=1, name="Jersery", description="Jersery's dummy description and so on, so read it!",category=category1)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Real Madried", description="Real Madried's dummy description and so on, so read it!",category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Barcelona", description="Barcelona's dummy description and so on, so read it!",category=category1)

session.add(Item3)
session.commit()


# Items for Basketball
category2 = Category(user_id=1, name="Basketball")

session.add(category2)
session.commit()

Item1 = Item(user_id=1, name="Basketball team1", description="Basketball team1's dummy description and so on, so read it!",category=category2)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Basketball team2", description="Basketball team2's dummy description and so on, so read it!",category=category2)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Basketball team3", description="Basketball team3's dummy description and so on, so read it!",category=category2)

session.add(Item3)
session.commit()


# Items for Baseball
category3 = Category(user_id=1, name="Baseball")

session.add(category3)
session.commit()

Item1 = Item(user_id=1, name="Baseball team1", description="Baseball team1's dummy description and so on, so read it!",category=category3)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Baseball team2", description="Baseball team2's dummy description and so on, so read it!",category=category3)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Baseball team3", description="Baseball team3's dummy description and so on, so read it!",category=category3)

session.add(Item3)
session.commit()

# Items for Hockey
category4 = Category(user_id=1, name="Hockey")

session.add(category4)
session.commit()

Item1 = Item(user_id=1, name="Hockey team1", description="Hockey team1's dummy description and so on, so read it!",category=category4)

session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Hockey team2", description="Hockey team2's dummy description and so on, so read it!",category=category4)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Hockey team3", description="Hockey team3's dummy description and so on, so read it!",category=category4)

session.add(Item3)
session.commit()

print ("added items!")
