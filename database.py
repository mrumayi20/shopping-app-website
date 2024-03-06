from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_clothing_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from duse.clothing"))
    clothings = []
    for row in result.all():
      clothings.append(row._mapping)
  return clothings


# print("type(result): ", type(result))
# result_all = result.all()
# print("type(result_all): ", type(result_all))
# print("result_all: ", result_all)
# print("type(result_all[0]): ", type(result_all[0]))
# first_result_dict = result_all[0]._mapping
# print('first_result_dict: ', type(first_result_dict))
# print(first_result_dict)

# If in section 2.4 of this video is not working for you and you are getting errors like 'Type Error: cannot convert dictionary update sequence element #0 to a sequence,', that just means that you are using SQL Alchemy 1.4 and greater, and dict(result_all[0]) doesn't work in that case, you have to use 'first_result_dict = result_all[0]._mapping'. Hope it will save you sometime. I wasted 2.5 hours on this :))
