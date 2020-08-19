# aws-soundclound-clone

This project, aws-soundcloud-clone, is a web service designed to 
host music files and user account information.

It was designed as a proof-of-concept for a future project.

The application is uses AWS serverless services, which are 
cloud-based.  It is a rest api that stores data in a sql database, 
and files on a cloud server. It is the backend for music 
social media site, using aws gateway, lambda, rds, s3.


## Rest API

```
GET /services/audio/getaudiosample?key=FILEKEY

GET /services/audio/verifyclip&key=FILEKEY

GET /services/audio/getdefaultaudiotags

GET /services/audio/getdefaultaudiofolders

GET /services/audio/getuseraudiofolders?username=USER

GET /services/users/getlicenses

POST /services/getuserinfo, username=USER, password=PASS
```


## AWS Serverless Services Setup

1. Create S3 bucket for audio samples

2. Create RDS database, mysql

3. Create Gateway api project

4. Create Lambda function

    - With lambda integration, there is only 1 function for he whole app

5. Configure gateway api project to use lambda function integration

6. Review any IAM roles with permissions
