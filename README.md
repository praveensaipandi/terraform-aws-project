# AWS DevOps Project - Terraform, EKS, Docker & Kubernetes

## Project Overview

This project demonstrates an end-to-end AWS DevOps deployment using Terraform, Docker, Amazon ECR, Amazon EKS, and Kubernetes.

The infrastructure was provisioned using Terraform, an application was containerized using Docker, the image was stored in Amazon ECR, and the application was deployed to an Amazon EKS cluster using Kubernetes.

The application is exposed externally using a Kubernetes `LoadBalancer` service.

---

## Architecture

```text
                         Developer
                            |
                            |
                     Git / GitHub
                            |
                            v
                    Terraform Configuration
                            |
                            v
                    +------------------+
                    |       AWS VPC    |
                    |                  |
                    |  Public Subnets  |
                    |       |          |
                    |       v          |
                    |   NAT Gateway    |
                    |       |          |
                    |       v          |
                    | Private Subnets  |
                    +--------+---------+
                             |
                             v
                     Amazon EKS Cluster
                             |
                    +--------+---------+
                    |                  |
                    v                  v
               EKS Node Group     Kubernetes
                                  Deployment
                                      |
                                      v
                                Docker Container
                                      |
                                      v
                                   Service
                                      |
                                      v
                              AWS Load Balancer
                                      |
                                      v
                                  End User
