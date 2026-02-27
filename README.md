AWS 3-Tier Secure Login Application
Project Overview

This project demonstrates the implementation of a secure 3-tier web architecture on AWS. The application is built using Flask and MySQL and was deployed using EC2 instances within a custom VPC setup including public and private subnets.

Architecture

Public EC2 (Web Tier) – Nginx Reverse Proxy

Private EC2 (Application Tier) – Flask Backend

Amazon RDS (Database Tier) – MySQL

VPC with Public & Private Subnets

Internet Gateway and NAT Gateway

Security Group based access control

Features

User registration and storage in MySQL database

Password hashing using Werkzeug for secure credential storage

Reverse proxy configuration using Nginx

Secure communication between Web, App, and DB tiers

Environment variable based configuration management

Technologies Used

AWS (EC2, VPC, RDS, NAT Gateway)

Python (Flask)

MySQL

Nginx

Linux

Learning Outcomes

Implemented 3-tier architecture with network isolation

Debugged real-world issues including SSH access, NAT routing, reverse proxy errors, and database authentication problems

Followed security best practices by avoiding hardcoded credentials and using environment variables
