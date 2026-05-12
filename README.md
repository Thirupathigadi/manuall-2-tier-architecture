📘 Student App – AWS Cloud Deployment Workflow Document
📌 Overview

This document explains the end-to-end workflow of a Student Management Application built using Flask, MySQL (AWS RDS), and AWS EC2. It is designed for students to understand cloud deployment, backend development, and DevOps basics.

🎯 Objective

The main goal of this project is to:

Build a REST API using Flask
Connect the application to AWS RDS MySQL database
Deploy the application on AWS EC2
Understand basic cloud deployment workflow
🏗️ System Architecture
Client (Browser / Postman)
          ↓
Flask Application (AWS EC2)
          ↓
AWS RDS MySQL Database
🧰 Technology Stack
Python 3
Flask (Backend Framework)
PyMySQL (Database connector)
SQLAlchemy (ORM)
Gunicorn (Production server)
AWS EC2 (Compute service)
AWS RDS (Database service)
Git & GitHub (Version control)
⚙️ Project Setup Steps
1️⃣ Clone the Project
git clone https://github.com/<your-username>/<repo-name>.git
cd student-app
2️⃣ Create Virtual Environment
python3 -m venv myenv
source myenv/bin/activate
3️⃣ Install Dependencies
pip install flask pymysql sqlalchemy gunicorn cryptography
4️⃣ Configure Environment Variables

Set database credentials:

export DB_HOST="your-rds-endpoint"
export DB_USER="admin"
export DB_PASSWORD="your-password"
export DB_NAME="studentdb"
🗄️ AWS RDS Database Setup
Step 1: Login to MySQL
mysql -h <rds-endpoint> -u admin -p
Step 2: Create Database
CREATE DATABASE studentdb;
Step 3: Grant Permissions
GRANT ALL PRIVILEGES ON studentdb.* TO 'admin'@'%';
FLUSH PRIVILEGES;
▶️ Run Application (Development Mode)
python app.py

Access application:

http://localhost:5000
🚀 Run Application (Production Mode)

Using Gunicorn:

gunicorn -w 4 -b 0.0.0.0:5000 app:app
☁️ AWS EC2 Deployment Steps
Step 1: Launch EC2 Instance
Ubuntu Server
Allow ports: 22, 80, 5000/8000
Step 2: Install Required Packages
sudo apt update
sudo apt install python3-pip python3-venv -y
Step 3: Run Application
source myenv/bin/activate
gunicorn -w 4 -b 0.0.0.0:5000 app:app
📡 API Endpoints
➕ Add Student

Endpoint:

POST /students

Request Body:

{
  "name": "Alice Kumar",
  "email": "alice@example.com",
  "course": "Cloud Computing"
}
🔐 Common Errors & Solutions
Error	Cause	Solution
Access Denied (MySQL)	Wrong permissions	Grant privileges
Cryptography error	Missing package	pip install cryptography
Connection error	Security Group issue	Open port 3306
Git push failed	Password auth disabled	Use GitHub token
📊 Learning Outcomes

After completing this project, students will understand:

Flask API development
AWS EC2 deployment process
AWS RDS database integration
Linux server management
Production deployment using Gunicorn
Git & GitHub workflow
👨‍🏫 Instructor Note

This project is part of the AWS Cloud Training Program. Students are expected to:

Complete daily tasks
Understand deployment workflow
Practice hands-on AWS services
📌 End of Document
