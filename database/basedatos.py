from sqlalchemy import create_engine,MetaData

motorBD=create_engine("mysql+pymysql://root@localhost:3306/firulaisdb")

metaDatos=MetaData()

conexion=motorBD.connect()

