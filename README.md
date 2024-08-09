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
  - Create a YAML file (e.g., deploy.yml) inside this directory with the required configurations.( deployment.yaml will be explained in fig X for better understanding)
  - ![Screenshot from 2024-08-09 17-46-37](https://github.com/user-attachments/assets/fb00dc91-b36d-4265-8755-6d971480e184)
#  Set Up Terraform for EC2 and Minikube
## Create Terraform Module:
  - Create terraform modules for your EC2, VPC, and any other resources you would like to use (taking considerations of the cost)
  - minikube reqirement 
    - 2 CPUs or More
    -  2GB of free memory
    -  20GB of free disk spac
    -  container or vitual machine manager, such as docker (see: "https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download")
## Initialize and Apply Terraform Configuration:
  - Create root modules 
  - Run the appropriate Terraform commands in your terminal to create an EC2 instance with Minikube running on it.
  - ![Screenshot from 2024-08-09 18-03-42](https://github.com/user-attachments/assets/8def0580-5cb5-400e-8032-1324f7772c66)
### Note: to meet up with minikube Reqiurment ec2 instance used is set to "t2.medium"
  - ![Screenshot from 2024-08-09 18-05-23](https://github.com/user-attachments/assets/b25bd84c-7729-4c1d-b8ec-173edbc4ed29)
  - after all requirements have been met, lets run the  neccessary terraform commands.
  - ![Screenshot from 2024-08-08 20-47-32](https://github.com/user-attachments/assets/136cdf38-e000-4905-afb1-296a4ab7df34)
  - ![Screenshot from 2024-08-08 20-50-53](https://github.com/user-attachments/assets/e3012b2b-2679-4465-906b-9b944f92faaf)
## Access the Minikube Cluster:
### SSH into EC2 Instance:
  - SSH into the created EC2 instance using the public IP output from Terraform.
  - ![Screenshot from 2024-08-09 18-13-41](https://github.com/user-attachments/assets/6753ef3c-6acb-43e8-adc6-c6f4b43da3b9)
  - lets verify our installation.
  - systemctl status docker 
  - ![Screenshot from 2024-08-09 09-39-04](https://github.com/user-attachments/assets/43b0f4f2-ac27-4b43-a27f-e43e88613bb1)
  - minikube status
  - ![Screenshot from 2024-08-09 09-40-23](https://github.com/user-attachments/assets/61abcae6-a209-4043-a680-7ccde6080755)
## Automate Deployment with GitHub Actions
### Update GitHub Actions Workflow:
  - Update the GitHub Actions workflow to deploy to the Minikube cluster on the EC2 instance. Ensure the Minikube instance's IP and SSH keys are securely managed.
  - fig x
  - ![Screenshot from 2024-08-09 18-20-23](https://github.com/user-attachments/assets/015bc4f2-21db-48e6-90d3-7556e859af9e)
    -  This is a GitHub Actions workflow file that automates the CI/CD pipeline for a Docker application. Here's a brief breakdown:
    -  Trigger: The pipeline runs on push events to the main branch.
    -  Job: The pipeline has one job called build, which runs on an ubuntu-latest environment.
    -  steps:
      - Checkout code: Retrieves the repository code.
      - Set up Docker Buildx: Configures Docker Buildx for building and pushing Docker images.
      - Login to DockerHub: Logs in to Docker Hub using secrets.
      - Build and push Docker image: Builds and pushes the Docker image to Docker Hub with the tag lahteeph/kodecamp-app:latest.
      - SSH setup: Sets up an SSH agent using a private key from secrets.
      - Minikube Deployment: Deploys the application to a Minikube cluster on an EC2 instance using SSH and kubectl commands.
      - In summary, this pipeline automates building, pushing, and deploying a Docker application to a Minikube cluster on an EC2 instance whenever code is pushed to the main branch.
    - see https://docs.github.com/en/actions/using-workflows/about-workflows
    - Note: all variable use in the above deploy.yml should be stored in 
    - ![Screenshot from 2024-08-09 18-44-10](https://github.com/user-attachments/assets/d405e667-7197-4e3c-b91d-3d5d2a80fb50)
# verifying:
  - ![Screenshot from 2024-08-09 18-50-18](https://github.com/user-attachments/assets/13eea103-4bbf-492e-a2a7-61ab28b099f5)
  - ![Screenshot from 2024-08-09 16-50-31](https://github.com/user-attachments/assets/84cab2bc-9b1d-43ae-a7ec-87b6d22b5e76)
  - ![Screenshot from 2024-08-09 09-35-37](https://github.com/user-attachments/assets/0bd05c70-a018-430b-845b-e5dc70bbac1a)

    


