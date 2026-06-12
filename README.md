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

Public EC2 (Nginx Reverse Proxy)
        │
        ▼
Private EC2 (Flask Backend)
        │
        ▼
Amazon RDS (MySQL)

VPC
├── Public Subnet
├── Private Subnet
├── Internet Gateway
└── NAT Gateway

Linux

Learning Outcomes

Implemented 3-tier architecture with network isolation

Debugged real-world issues including SSH access, NAT routing, reverse proxy errors, and database authentication problems

Followed security best practices by avoiding hardcoded credentials and using environment variables
