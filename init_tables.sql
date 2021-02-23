
-- CONTAINS ALL INFO FOR A URL TO A STORY
CREATE TABLE story_urls (
	story_id integer PRIMARY KEY,
	media_id integer NOT NULL,
	title TEXT,
	url TEXT NOT NULL UNIQUE,
	collect_date TEXT NOT NULL,
	publish_date TEXT
);

-- CONTAINS ALL INFO FOR A MEDIA SOURCE
CREATE TABLE media_sources (
	media_id integer PRIMARY KEY,
	media_name TEXT,
	media_url TEXT
);

-- CONTAINS ALL FULL STORIES
CREATE TABLE story_full (
	story_id integer PRIMARY KEY,
	text_full TEXT NOT NULL
);
