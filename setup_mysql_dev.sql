CREATE DATABASE IF NOT EXISTS job_win_db;
CREATE USER IF NOT EXISTS 'job_dev'@'localhost' IDENTIFIED BY 'job_dev_pwd';
GRANT ALL PRIVILEGES ON job_win_db.* TO 'job_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'job_dev'@'localhost';
