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

CREATE SCHEMA COMMUNITY_DATA;

drop table if exists COMMUNITY_DATA.answer_info;

drop table if exists COMMUNITY_DATA.location_survey;

drop table if exists COMMUNITY_DATA.question_info;

drop table if exists COMMUNITY_DATA.question_options;

drop table if exists COMMUNITY_DATA.student_location_info;


drop table if exists COMMUNITY_DATA.student_survey_info;

drop table if exists COMMUNITY_DATA.survey_info;


CREATE TABLE COMMUNITY_DATA.answer_info (
	student_id varchar(255) NOT NULL,
	survey_id varchar(255) NOT NULL,
	question_id varchar(255) NOT NULL,
	answer text NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_answer_info ON COMMUNITY_DATA.answer_info USING btree (student_id, survey_id, question_id);
CREATE UNIQUE INDEX idx_answer_info_unique ON COMMUNITY_DATA.answer_info USING btree (student_id, survey_id, question_id, created_at);



CREATE TABLE COMMUNITY_DATA.location_survey (
	locname varchar(255) NOT NULL,
	survey_id varchar(255) NOT NULL,
	lat float8 NULL,
	lng float8 NULL,
	created_at timestamptz NULL,
	CONSTRAINT location_survey_pkey PRIMARY KEY (locname)
);




CREATE TABLE COMMUNITY_DATA.question_info (
	question_id varchar(255) NOT NULL,
	question text NULL,
	created_at timestamptz NULL,
	CONSTRAINT question_info_pkey PRIMARY KEY (question_id)
);
CREATE INDEX idx_question_info ON COMMUNITY_DATA.question_info USING btree (question_id, question);
CREATE UNIQUE INDEX idx_question_info_unique ON COMMUNITY_DATA.question_info USING btree (question_id, question);


CREATE TABLE COMMUNITY_DATA.question_options (
	question_id varchar(255) NOT NULL,
	"options" _text NOT NULL,
	CONSTRAINT question_options_pkey PRIMARY KEY (question_id)
);




CREATE TABLE COMMUNITY_DATA.student_location_info (
	student_id varchar(255) NOT NULL,
	lat float8 NOT NULL,
	lng float8 NOT NULL,
	present_time timestamp NOT NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_student_location_info ON COMMUNITY_DATA.student_location_info USING btree (student_id, present_time);
CREATE UNIQUE INDEX idx_student_location_info_unique ON COMMUNITY_DATA.student_location_info USING btree (student_id, present_time);


CREATE TABLE COMMUNITY_DATA.student_survey_info (
	student_id varchar(255) NOT NULL,
	survey_id varchar(255) NOT NULL,
	status varchar(10) NULL,
	updated_at timestamp NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_student_survey_info ON COMMUNITY_DATA.student_survey_info USING btree (student_id, survey_id);
CREATE UNIQUE INDEX idx_student_survey_info_unique ON COMMUNITY_DATA.student_survey_info USING btree (student_id, survey_id);



CREATE TABLE COMMUNITY_DATA.survey_info (
	survey_id varchar(255) NOT NULL,
	question_id varchar(255) NOT NULL,
	created_at timestamptz NULL
);
CREATE INDEX idx_survey_info ON COMMUNITY_DATA.survey_info USING btree (survey_id, question_id);
CREATE UNIQUE INDEX idx_unique_survey_info ON COMMUNITY_DATA.survey_info USING btree (survey_id, question_id);






          """)
    conn.commit()

def insert_questions():
    print("Adding questions")
    cursor.execute("""
    INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('1', 'I feel a connection with the CU Boulder community.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('2', 'I feel like I fit in at CU Boulder.', now());


INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('3', 'I feel that I belong at CU Boulder.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('4', 'I view CU Boulder as my home during my undergraduate years.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('5', 'People on campus are generally supportive of my individual needs.', now());




INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('6', 'There are people on campus who are genuinely interested in me as a person.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('7', 'There are people on campus who care about my future.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('8', ' At CU, I’m treated like I belong.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('9', ' I have a sense of community at CU.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('10', 'I feel valued.', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('11', 'There are people on campus who care about my future.', now());




INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('12', ' I am proud to be a student at CU.', now());


INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('13', ' I feel supported.', now());


INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('14', 'Did you borrow any book in libraray', now());



INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('15', 'Did you go to library to study with friends', now());


INSERT INTO community_data.question_info (question_id, question, created_at)
VALUES('16', 'Did you go to Rec to hangout with friends', now());

    """)
    conn.commit()


def insert_options():
    print("Adding Options")
    cursor.execute("""
    INSERT INTO community_data.question_options (question_id, "options")
VALUES('1', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);

INSERT INTO community_data.question_options (question_id, "options")
VALUES('2', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('3', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);

INSERT INTO community_data.question_options (question_id, "options")
VALUES('4', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);

INSERT INTO community_data.question_options (question_id, "options")
VALUES('5', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('6', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('7', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('8', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('9', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('10', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);

INSERT INTO community_data.question_options (question_id, "options")
VALUES('11', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('12', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('13', ARRAY ['strongly disagree', 'disagree', 'somewhat disagree', 'somewhat agree', 'agree', 'strongly agree']);

INSERT INTO community_data.question_options (question_id, "options")
VALUES('14', ARRAY ['Yes', 'No']);

INSERT INTO community_data.question_options (question_id, "options")
VALUES('15', ARRAY ['Yes', 'Looking for study space', 'Checking library', 'Other']);


INSERT INTO community_data.question_options (question_id, "options")
VALUES('16', ARRAY ['Yes', 'No']);
""")
    conn.commit()

#create_db()

import random

def random_questions_survey():
    survey = 4
    for i in range(1, survey):
        q = random.sample(range(1,17), 6)
        for j in q:
            cursor.execute("""
            INSERT INTO community_data.survey_info (survey_id, question_id, created_at)
    VALUES(%s, %s, now()); """,((i, q)))
            conn.commit()  


#insert_questions()

#insert_options()

random_questions_survey()

conn.close()