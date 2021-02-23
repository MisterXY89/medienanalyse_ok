
import psycopg2

from settings import POSTGRES_USER, POSTGRES_PASSWORD

def write_url(story_id, media_id, title, url, collect_date, publish_date):
    connection = psycopg2.connect(database="medienanalyse_ok",
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host="127.0.0.1",
                        port="5432"
                    )
    cur = connection.cursor()

    cur.execute(f"INSERT INTO story_urls (story_id, media_id, title, url, collect_date, publish_date) \
      VALUES ({story_id}, {media_id}, '{title}', '{url}', '{collect_date}', '{publish_date}');")
    connection.commit()
    connection.close()

def write_text():
    pass

def read_urls():
    pass
