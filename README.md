# CI/CD PIPELINE PROJECT
## Objective
Set up a CI/CD pipeline with GitHub Actions to deploy a code (could be the code from your previous task) from GitHub to a Minikube cluster running on an EC2 instance deployed using Terraform.

# Steps in Acheiving the Objectives
#  Prepare the Code Repository
## Create a Repository on GitHub:
  - Add your application code to the repository.
  - Ensure you have a Dockerfile for your application to containerize it
  - ![Screenshot from 2024-08-09 17-24-59](https://github.com/user-attachments/assets/d82a09c0-ca0f-45b3-8d05-99f650aeb2a9)
  - Push image to Docker image registry.
  - ![pics](https://github.com/user-attachments/assets/724ae57b-6408-4e65-9d08-55cf5969221e)
## Create Kubernetes Manifests:
  - Add the necessary Kubernetes manifests (e.g., deployment.yaml, service.yaml) to a k8s directory in your repository.
![Screenshot from 2024-08-09 17-41-44](https://github.com/user-attachments/assets/081e5440-f708-4074-973c-91250ccac95f)
# Set Up GitHub Actions
## Create a GitHub Actions Workflow:
  - In your repository, create a .github/workflows directory.
  - Create a YAML file (e.g., deploy.yml) inside this directory with the required configurations.
  - ![Screenshot from 2024-08-09 17-46-37](https://github.com/user-attachments/assets/fb00dc91-b36d-4265-8755-6d971480e184)
#  Set Up Terraform for EC2 and Minikube
## Create Terraform Module:
  - Create terraform modules for your EC2, VPC, and any other resources you would like to use (taking considerations of the cost)
  - 
