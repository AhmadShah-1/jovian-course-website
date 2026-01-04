from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ['DB_CONNECTION_STRING'], pool_size=1, max_overflow=0, pool_recycle=1000, pool_pre_ping=True)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()