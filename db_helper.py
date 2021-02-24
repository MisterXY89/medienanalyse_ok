
import psycopg2

from settings import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST

def write_url(story_id, media_id, title, url, collect_date, publish_date):
    try:
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
    except Exception as e:
        print(e)
        return False

def write_text(story_id, text_full):
    text_full = text_full.replace("'", "''")
    try:
        connection = psycopg2.connect(database="medienanalyse_ok",
                            user=POSTGRES_USER,
                            password=POSTGRES_PASSWORD,
                            host="127.0.0.1",
                            port="5432"
                        )
        cur = connection.cursor()

        cur.execute(f"INSERT INTO story_full (story_id, text_full) \
          VALUES ({story_id}, '{text_full}');")
        connection.commit()
        connection.close()
    except Exception as e:
        print(e)
        return False


def read_urls():
    try:
        connection = psycopg2.connect(database="medienanalyse_ok",
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host=POSTGRES_HOST,
                        port="5432"
                    )
        cur = connection.cursor()
        cur.execute("SELECT story_id, url FROM story_urls;")
        rows = cur.fetchall()
        all_urls = []
        for row in rows:
            all_urls.append({
                "id": row[0],
                "url": row[1],
            })

        connection.close()
        return all_urls
    except Exception as e:
        print(e)
        return False


us = read_urls()
