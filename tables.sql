CREATE TABLE IF NOT EXISTS job_win_db.Users(
user_id int,
name varchar(255),
last_name varchar(255),
username varchar(255),
passwd varchar(255),
birth varchar(255),
email varchar(255),
type varchar(255),
pic varbinary(5000),
status varchar(255),
gender varchar(255),
PRIMARY KEY(user_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Category(
cat_id int PRIMARY KEY,
name varchar(255)
);

CREATE TABLE IF NOT EXISTS job_win_db.Interview(
int_id int PRIMARY KEY,
status varchar(255),
submit_date date,
type varchar(255),
user_id int,
cat_id int,
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(user_id),
FOREIGN KEY (cat_id) REFERENCES job_win_db.Category(cat_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Subcategory(
sub_id int PRIMARY KEY,
name varchar(255),
cat_id int,
FOREIGN KEY (cat_id) REFERENCES job_win_db.Category(cat_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Post(
post_id int PRIMARY KEY,
created_at date,
updated_at date,
content varchar(255),
sub_id int,
u_id int,
cat_id int,
FOREIGN KEY(u_id) REFERENCES job_win_db.Users(user_id),
FOREIGN KEY(sub_id) REFERENCES job_win_db.Subcategory(sub_id),
FOREIGN KEY(cat_id) REFERENCES job_win_db.Category(cat_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Comments(
com_id int PRIMARY KEY,
created_at date, 
updated_at date,
user_id int,
post_id int,
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(user_id),
FOREIGN KEY (post_id) REFERENCES job_win_db.Post(post_id)
);


CREATE TABLE IF NOT EXISTS job_win_db.Question(
q_id int PRIMARY KEY,
text varchar(255),
type varchar(255),
sub_id int,
FOREIGN KEY (sub_id) REFERENCES job_win_db.Subcategory(sub_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Answer(
a_id int PRIMARY KEY,
text varchar(255),
audio varbinary(5000),
int_id int,
FOREIGN KEY (int_id) REFERENCES job_win_db.Interview(int_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Correction(
c_id int PRIMARY KEY,
c_date date,
text varchar(255),
feedback varchar(255),
int_id int,
user_id int,
coach_id int,
FOREIGN KEY (int_id) REFERENCES job_win_db.Interview(int_id),
FOREIGN KEY (coach_id) REFERENCES job_win_db.Users(user_id)
);


CREATE TABLE IF NOT EXISTS job_win_db.Relation(
user_id int PRIMARY KEY,
dat date
);

CREATE TABLE IF NOT EXISTS job_win_db.Sub_follow(
user1_id int,
user2_id int,
FOREIGN KEY (user1_id) REFERENCES job_win_db.Users(user_id),
FOREIGN KEY (user2_id) REFERENCES job_win_db.Users(user_id),
dat date
);

CREATE TABLE IF NOT EXISTS job_win_db.Comm_like(
user_id int,
com_id int,
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(user_id), 
FOREIGN KEY (com_id) REFERENCES job_win_db.Comments(com_id)
);

CREATE TABLE IF NOT EXISTS job_win_db.Post_like(
user_id int,
post_id int,
FOREIGN KEY (user_id) REFERENCES job_win_db.Users(user_id),
FOREIGN KEY (post_id) REFERENCES job_win_db.Post(post_id)
);

