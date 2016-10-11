import pg
from sys import exit

db = pg.DB(dbname="phonebook_db")

def phoneapp():
    running = "N"
    while running == "N":
        entries()
        running = str.upper(raw_input("Are you finished using Phonebook (Y or N)? "))
    print "Bye."

def entries():

    print """

    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """
    option = raw_input("What do you want to do (1 - 5)? ")
    if option == "1":
        search()

    elif option == "2":
        enterNew()

    elif option == "3":
        deleteEntry()

    elif option == "4":
        listEntries()

    elif option == "5":
        print "Bye."
        exit(0)

    else:
        print "Ivalid entry."

def search():
    search = str.upper(raw_input("\nWho are you searching for? "))
    query = db.query("select name, phone_number, email from phonebook where name = '" + search + "'").namedresult()
    if len(query) == 0:
        print "Sorry, I could not find that name.\n"
    else:
        print "%s \n Phone number: %s \n Email: %s \n" % (search, query[0].phone_number, query[0].email)

def enterNew():
    name = str.upper(raw_input("What's your name? "))
    phone = str(raw_input("What's your phone number (xxx-xxx-xxx)? "))
    email = str(raw_input("What's your email address? "))
    db.insert('phonebook', name=name, phone_number=phone, email=email)
    print "Entry created for %s.\n" % name

def deleteEntry():
    name = str.upper(raw_input("What entry would you like to delete? "))
    query = db.query("select id from phonebook where name = '" + name + "'").namedresult()
    if len(query) > 0:
        db.delete('phonebook', {'id': query[0].id})
        print "\n %s's entry has been deleted." % name
    else:
        print "\nSorry, I could not find that name in the phonebook.\n"

def listEntries():
    query = db.query('select name, phone_number, email from phonebook order by phonebook.name').namedresult()
    for result in query:
        print "%s's phonenumber is %s and their email is %s.\n" % (result.name, result.phone_number, result.email)

phoneapp()
