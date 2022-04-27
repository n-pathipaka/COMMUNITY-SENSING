import psycopg2
from psycopg2.extras import Json, DictCursor
import time
from sqlalchemy import create_engine


conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="neerab")

cursor = conn.cursor()



engine = create_engine('postgresql://postgres:neerab@localhost:5432/postgres',
                      pool_pre_ping=True,
        connect_args={
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 5,
        })



#### push data ###
def create_db():
    print("Hello")
    cursor.execute("""

CREATE SCHEMA COMMUNITY_DATA_2;

drop table if exists COMMUNITY_DATA_2.answer_info;

drop table if exists COMMUNITY_DATA_2.location_survey;

drop table if exists COMMUNITY_DATA_2.question_info;

drop table if exists COMMUNITY_DATA_2.question_options;

drop table if exists COMMUNITY_DATA_2.student_location_info;


drop table if exists COMMUNITY_DATA_2.student_survey_info;

drop table if exists COMMUNITY_DATA_2.survey_info;


CREATE TABLE COMMUNITY_DATA_2.answer_info (
	student_id varchar(255) NOT NULL,
	survey_id varchar(255) NOT NULL,
	question_id varchar(255) NOT NULL,
	answer text NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_answer_info ON COMMUNITY_DATA_2.answer_info USING btree (student_id, survey_id, question_id);
CREATE UNIQUE INDEX idx_answer_info_unique ON COMMUNITY_DATA_2.answer_info USING btree (student_id, survey_id, question_id, created_at);



CREATE TABLE COMMUNITY_DATA_2.location_survey (
	locname varchar(255) NOT NULL,
	survey_id varchar(255) NOT NULL,
	lat float8 NULL,
	lng float8 NULL,
	created_at timestamptz NULL,
	CONSTRAINT location_survey_pkey PRIMARY KEY (locname)
);




CREATE TABLE COMMUNITY_DATA_2.question_info (
	question_id varchar(255) NOT NULL,
	question text NULL,
	created_at timestamptz NULL,
	CONSTRAINT question_info_pkey PRIMARY KEY (question_id)
);
CREATE INDEX idx_question_info ON COMMUNITY_DATA_2.question_info USING btree (question_id, question);
CREATE UNIQUE INDEX idx_question_info_unique ON COMMUNITY_DATA_2.question_info USING btree (question_id, question);


CREATE TABLE COMMUNITY_DATA_2.question_options (
	question_id varchar(255) NOT NULL,
	"options" _text NOT NULL,
	CONSTRAINT question_options_pkey PRIMARY KEY (question_id)
);




CREATE TABLE COMMUNITY_DATA_2.student_location_info (
	student_id varchar(255) NOT NULL,
	lat float8 NOT NULL,
	lng float8 NOT NULL,
	present_time timestamp NOT NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_student_location_info ON COMMUNITY_DATA_2.student_location_info USING btree (student_id, present_time);
CREATE UNIQUE INDEX idx_student_location_info_unique ON COMMUNITY_DATA_2.student_location_info USING btree (student_id, present_time);


CREATE TABLE COMMUNITY_DATA_2.student_survey_info (
	student_id varchar(255) NOT NULL,
	survey_id varchar(255) NOT NULL,
	status varchar(10) NULL,
	updated_at timestamp NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_student_survey_info ON COMMUNITY_DATA_2.student_survey_info USING btree (student_id, survey_id);
CREATE UNIQUE INDEX idx_student_survey_info_unique ON COMMUNITY_DATA_2.student_survey_info USING btree (student_id, survey_id);



CREATE TABLE COMMUNITY_DATA_2.survey_info (
	survey_id varchar(255) NOT NULL,
	question_id varchar(255) NOT NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_survey_info ON COMMUNITY_DATA_2.survey_info USING btree (survey_id, question_id);
CREATE UNIQUE INDEX idx_unique_survey_info ON COMMUNITY_DATA_2.survey_info USING btree (survey_id, question_id);






          """)
    conn.commit()




create_db()