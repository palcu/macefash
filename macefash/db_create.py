from app import db
from models import Person, Vote, Message

#create the database and the db tables
#db.create_all()

#insert entries

added = 0
with open("friendScraper/friendlist", "r") as f:
  for line in f:
    s = line[:-1]

    if s:
      #print "trying to add {%s}" % s

      if Person.query.filter_by(username=s).first() is None:
        db.session.add(Person(s))
        added += 1
      else:
        print "%s is already in db." % s

if raw_input("added %i entries. commit? (y/n) " % added) == 'y':
  #commit the changes
  db.session.commit()
  db.session.close()
  print "changes committed. done."
else:
  print "ok. changes not saved."
