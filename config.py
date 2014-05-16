import os
basedir=os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED=True
SECRET_KEY='this is i am many times to check the test but alives fialed'

OPENID_PROVIDERS=[{'name':'Google','url':'https://www.google.com/accounts/o8/id'},
		{'name':'Yahoo','url':'https://me.yahoo.com'},
		{'name':'AOL','url':'https://openid.aol.com/<username>'},
		{'name':'MyOpenID','url':'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI='sqlite:////' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir,'db_repository')
WHOOSH_BASE = os.path.join(basedir,'search.db')

#mail server settings
MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME='tonytan748'
MAIL_PASSWORD='violin1981'

#available languages
LANGUAGES={
	'en':'English',
	'es':'Espanol'
}

#administrator list
ADMINS=['tonytan748@gmail.com']

#pageination
POSTS_PER_PAGE=3
MAX_SEARCH_RESULTS=50

