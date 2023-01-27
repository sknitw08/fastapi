from sqlalchemy import create_engine,MetaData
import os
import urllib

# conn = engine.connect()

host_server = os.environ.get('host_server')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port')))
database_name = os.environ.get('database_name')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password')))

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(db_username,db_password,host_server,db_server_port,database_name)
engine = create_engine(connect_string,connect_args=connect_args)
conn = engine.connect()

# conn.execute("CREATE DATABASE IF NOT EXISTS test")
# conn.execute("USE test")
meta = MetaData()