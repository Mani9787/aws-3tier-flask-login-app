# AWS Three-Tier Secure Web Application Architecture
## Objective

The objective of this project was to design and deploy a secure three-tier web application architecture on AWS using public and private subnets, EC2 instances, Amazon RDS, and Nginx reverse proxy while following cloud security best practices.
## Skills Demonstrated

- AWS EC2 Deployment
- VPC Configuration
- Public and Private Subnet Design
- Security Group Configuration
- Amazon RDS Management
- Linux Administration
- Nginx Reverse Proxy Setup
- Flask Application Deployment
- Network Troubleshooting
Project Overview

This project demonstrates the implementation of a secure 3-tier web architecture on AWS. The application is built using Flask and MySQL and was deployed using EC2 instances within a custom VPC setup including public and private subnets.

## Architecture

User
   |
Internet
   |
Web Server (Public EC2 + Nginx)
   |
Application Server (Private EC2 + Flask)
   |
Amazon RDS MySQL Database

Infrastructure:
- Custom VPC
- Public Subnet
- Private App Subnet
- Private DB Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups

  ## AWS Services Used

- Amazon EC2
- Amazon VPC
- Amazon RDS MySQL
- Internet Gateway
- NAT Gateway
- Elastic IP
- Route Tables
- Security Groups
- Public & Private Subnets

  ## Security Features

- Private application deployment
- Database isolation in private subnet
- Security Group based access control
- Password hashing using Werkzeug
- Reverse Proxy using Nginx
- Environment variable configuration

  ## Challenges Solved

- NAT Gateway configuration
- Route Table association
- EC2 to EC2 SSH connectivity
- Flask to MySQL connectivity
- Nginx reverse proxy setup
- Security Group troubleshooting
## VPC and Subnets

![VPC](screenshots/vpc-subnets.png)

## Internet Gateway

![IGW](screenshots/internet-gateway.png)

## Elastic IP

![Elastic IP](screenshots/elastic-ip.png)

## Route Table Association

![Route Table](screenshots/route-table.png)

## Security Groups

![Security Groups](screenshots/security-groups.png)

## EC2 Instances

![EC2](screenshots/ec2-instances.png)

## SSH Access to Web Server

![SSH Web](screenshots/ssh-webserver.png)

## SSH Access to Application Server

![SSH App](screenshots/ssh-appserver.png)

## Signup Page

![Signup](screenshots/signup-page.png)

## Dashboard

![Dashboard](screenshots/dashboard.png)

##Learning Outcomes

Implemented 3-tier architecture with network isolation

Debugged real-world issues including SSH access, NAT routing, reverse proxy errors, and database authentication problems

Followed security best practices by avoiding hardcoded credentials and using environment variables
