import os
basedir=os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI='sqlite:////' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir,'db_repository')


CSRF_ENABLED=True
SECRET_KEY='this is i am many times to check the test but alives fialed'

OPENID_PROVIDERS=[{'name':'Google','url':'https://www.google.com/accounts/o8/id'},
		{'name':'Yahoo','url':'https://me.yahoo.com'},
		{'name':'AOL','url':'https://openid.aol.com/<username>'},
		{'name':'MyOpenID','url':'https://www.myopenid.com'}]

#mail server settings
MAIL_SERVER='loaclhost'
MAIL_PORT=25
MAIL_USERNAME=None
MAIL_PASSWORD=None

#administrator list
ADMINS=['tonytan748@gmail.com']

#pageination
POSTS_PER_PAGE=3

WHOOSH_BASE = os.path.join(basedir,'search.db')
