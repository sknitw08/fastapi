from sqlalchemy import create_engine,MetaData
# Orig:
engine = create_engine('mysql+pymysql://root:password@localhost:3306/text')
# engine = create_engine('mysql+pymysql://admin01:Magicevents01@azdbmysqlpoc.mysql.database.azure.com:3306/test')

conn = engine.connect()

# connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
# connect_string = 'mysql+pymysql://{}:{}@{}/{}'.format("admin01","Magicevents01","azdbmysqlpoc.mysql.database.azure.com:3306","test")
# engine = create_engine(connect_string,connect_args=connect_args)
# conn = engine.connect()
# conn.execute("CREATE DATABASE IF NOT EXISTS test")
# conn.execute("USE test")
meta = MetaData()