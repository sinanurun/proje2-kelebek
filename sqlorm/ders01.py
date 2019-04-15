import sqlalchemy as db #kütüphane dahil etme işlemi
import pandas as pd

engine = db.create_engine('sqlite:///census.sqlite') #veri tabanı arıyor
connection = engine.connect()    #varsa bağlanıyor yoksa oluşturuyor
metadata = db.MetaData()    # bir nevi cursor işaretçi oluşturuyor işlem yapabilemeyi sağlıyor

emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )

metadata.create_all(engine)

query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True)
ResultProxy = connection.execute(query)


#Inserting many records at ones
query = db.insert(emp)
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)

results = connection.execute(db.select([emp])).fetchall()
print(results[0])
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(4))