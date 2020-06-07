CREATE TABLE IF NOT EXISTS job_win_db.Users(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
name varchar(255),
last_name varchar(255),
username varchar(255),
passwd varchar(255),
birth varchar(255),
email varchar(255),
type varchar(255),
pic varbinary(5000),
status varchar(255),
gender varchar(255)
);

CREATE TABLE IF NOT EXISTS job_win_db.Category(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
name varchar(255)
);

CREATE TABLE IF NOT EXISTS job_win_db.Interview(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
status varchar(255),
submit_date date,
type varchar(255),
user_id varchar(60),
cat_id varchar(60),
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(id),
FOREIGN KEY (cat_id) REFERENCES job_win_db.Category(id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Subcategory(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
name varchar(255),
cat_id varchar(60),
FOREIGN KEY (cat_id) REFERENCES job_win_db.Category(id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Post(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
content varchar(255),
sub_id varchar(60),
u_id varchar(60),
cat_id varchar(60),
FOREIGN KEY(u_id) REFERENCES job_win_db.Users(id),
FOREIGN KEY(sub_id) REFERENCES job_win_db.Subcategory(id),
FOREIGN KEY(cat_id) REFERENCES job_win_db.Category(id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Comments(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
user_id varchar(60),
post_id varchar(60),
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(id),
FOREIGN KEY (post_id) REFERENCES job_win_db.Post(id)
);


CREATE TABLE IF NOT EXISTS job_win_db.Question(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
text varchar(255),
type varchar(255),
sub_id varchar(60),
FOREIGN KEY (sub_id) REFERENCES job_win_db.Subcategory(id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Answer(
id int PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
text varchar(255),
audio varbinary(5000),
int_id varchar(60),
FOREIGN KEY (int_id) REFERENCES job_win_db.Interview(id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Correction(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
c_date date,
text varchar(255),
feedback varchar(255),
int_id varchar(60),
user_id varchar(60),
coach_id varchar(60),
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(id),
FOREIGN KEY (int_id) REFERENCES job_win_db.Interview(id),
FOREIGN KEY (coach_id) REFERENCES job_win_db.Users(id)
);


CREATE TABLE IF NOT EXISTS job_win_db.Relation(
id_1 varchar(60),
id_2 varchar(60),
created_at DATETIME,
updated_at DATETIME,
FOREIGN KEY (id_1) REFERENCES job_win_db.Users(id),
FOREIGN KEY (id_2) REFERENCES job_win_db.Users(id),
PRIMARY KEY (id_1, id_2)
);

CREATE TABLE IF NOT EXISTS job_win_db.Sub_follow(
id_1 varchar(60),
id_2 varchar(60),
created_at DATETIME,
updated_at DATETIME,
FOREIGN KEY (id_1) REFERENCES job_win_db.Users(id),
FOREIGN KEY (id_2) REFERENCES job_win_db.Users(id),
PRIMARY KEY (id_1, id_2)
);

CREATE TABLE IF NOT EXISTS job_win_db.Comm_like(
id_1 varchar(60),
id_2 varchar(60),
created_at DATETIME,
updated_at DATETIME,
FOREIGN KEY (id_1) REFERENCES job_win_db.Users(id), 
FOREIGN KEY (id_2) REFERENCES job_win_db.Comments(id),
PRIMARY KEY (id_1, id_2)
);

CREATE TABLE IF NOT EXISTS job_win_db.Post_like(
id_1 varchar(60),
id_2 varchar(60),
created_at DATETIME,
updated_at DATETIME,
FOREIGN KEY (id_1) REFERENCES job_win_db.Users(id),
FOREIGN KEY (id_2) REFERENCES job_win_db.Post(id),
PRIMARY KEY (id_1, id_2)
);

