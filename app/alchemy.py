from sqlalchemy import create_engine
from sqlalchemy import text

URL = 'postgresql://postgres:T-Mobile01@localhost/fastapi'

engine = create_engine(URL, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select * from posts"))
    print(result.all())