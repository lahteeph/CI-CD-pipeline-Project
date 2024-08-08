# containerization-project
# Objectives
## Create a simple web application:
  - Use Python Programming Language to create your simple application
  - The application should display a simple message like "Hello, Welcome to KodeCamp DevOps Bookcamp!"
  - You can give your app more features if you choose to.
## Dockerize the application:
  - Write a Dockerfile to containerize the application.
  - Build the Docker image and run it locally to ensure it works correctly.
  - Tag it and Push the Docker image to a container registry (e.g., Docker Hub).
## Deploy the application to a Kubernetes cluster:
  - Create a Kubernetes manifest file for a Deployment to deploy the Docker image.
  - Deploy the app to your minikube cluster
  - Create a Kubernetes Service of type ClusterIP to expose the application.
## Test the deployment:
  - Port-forward your service to a localhost port and access it through your web browser.
  - Verify that the application displays the expected message.

# Steps in Achieving the above objectives
## Directory and file structure for the project.
  -  ![Screenshot from 2024-08-03 12-38-57](https://github.com/user-attachments/assets/b6bd610f-1108-40e4-8554-ce4bfc9ded61)

## Requirements
  - docker
  - docker compose
  - linux host
  - see https://docs.docker.com/manuals/
    
to make the project more realistic lets use a web template.
log-on to https://templatemo.com to download any template of ur choice.
in my case i chose the bellow template.
unzip it, in my case i also made some changes.
  - ![Screenshot from 2024-08-01 21-07-00](https://github.com/user-attachments/assets/f04ba16a-f7cb-4f96-8ccf-ba54b4092d6f)
  - create a directory "kodecamp-web", cd into the directory and create file with respect to the above project structure
  - unzip the downloaded template and place it in the directory.
  - ![Screenshot from 2024-08-01 21-07-00](https://github.com/user-attachments/assets/ae776bd1-cc7c-4bb1-8e42-d29c2fa8dc86)
  - lets edit file created and explain.
  - .....
## app.py
  - ![Screenshot from 2024-08-02 21-15-42](https://github.com/user-attachments/assets/9e90db1b-e281-4e0b-830c-c992a8dc4fed)
  - .....
## requirments.txt
  - ![Screenshot from 2024-08-03 17-31-03](https://github.com/user-attachments/assets/d27a77b0-fa9a-44c6-b687-41f68ce25356)

  - "Flask" as said earlier is a web framework for phython
  - .....
## Dockerfile
  - ![Screenshot from 2024-08-02 21-39-59](https://github.com/user-attachments/assets/f7f0a52b-e0a6-4981-bae4-5c7432ceea84)

  - NOTE: "Dockerfile" does not have any extension.
  - see https://docs.docker.com/compose/gettingstarted/ for more understanding

# Build the Docker image and run it locally to ensure it works correctly.
  - Run "Docker build -t kodecamp-web . (to build the image created)
  - ![Screenshot from 2024-08-02 22-14-54](https://github.com/user-attachments/assets/68190030-1dfe-4c09-851d-ae003fb785e1)

  - Our image is successfully build, lets verify by running "docker images".
  - ![Screenshot from 2024-08-02 22-37-02](https://github.com/user-attachments/assets/028b903c-b4c5-49c5-acc7-a8811dd9cb20)

## testing the build image
  - Run "docker run --name kodecamp-web -p 8000:5000 kodecamp-web (for spining up our build image and port forwarding)
  - ![Screenshot from 2024-08-02 22-46-31](https://github.com/user-attachments/assets/93581f19-8244-4249-bd45-93bbdda598ec)

  - visit http://yourhostip:8000 on your browser to test ur container.
  - ![Screenshot from 2024-08-02 20-46-02](https://github.com/user-attachments/assets/6668d909-b3cb-4e09-90c3-f4eeffe2cc1a)

  - while on your browser you can also check your backend host, you should be seeing the request sent to the front end and the ip the request is coming from.
  - !![Screenshot from 2024-08-02 23-01-06](https://github.com/user-attachments/assets/81bca0ea-6a64-4744-a85e-56ca0f43dc19)

  - Note: the container can also be runing in backgroud by add "-d" to the comand.
  - "docker run --name kodecamp-web -d -p 8000:5000 kodecamp-web (for runing container at first)
  - "docker run -d -p 8000:5000 kodecamp-web (for starting already provisioned container)
  - run "docker ps -a" to check the processess runing in background.
  - ![Screenshot from 2024-08-02 23-05-37](https://github.com/user-attachments/assets/61937c6f-5d34-4586-80b1-e90cc6f9861e)
  - to stop your container, run "docker stop (your container id)
    
# Tag it and Push the Docker image to a container registry
  - i need to open an account on https://hub.docker.com and login your account details to link your host.
  - ![Screenshot from 2024-08-02 23-09-25](https://github.com/user-attachments/assets/5534239a-cfd5-4821-aae7-dd2adacab643)

  - tag and push to docker hub
  - ![Screenshot from 2024-08-02 23-39-17](https://github.com/user-attachments/assets/1ec16a68-06f3-47c1-9019-951b9f9ab395)

  - log into your git hub account to verify if the repository was successfully push.
  - ![Screenshot from 2024-08-03 00-14-53](https://github.com/user-attachments/assets/d614164f-1022-4709-819a-6dff5ce9d508)


# dockerhub link
https://hub.docker.com/repositories/lahteeph


# Deploy the application to a Kubernetes cluster:
## Deploy the app to your minikube cluster
  ## requirements
  - install minikube (see https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)
  - install kubernet (see https://kubernetes.io/docs/tasks/tools/)
## Create a Kubernetes manifest file for a Deployment to deploy the Docker image.
  -![Screenshot from 2024-08-03 11-54-51](https://github.com/user-attachments/assets/77869313-005d-4928-a247-226bdc12efc5)
  - see (https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
  - run "minikube start".
  - ![Screenshot from 2024-08-03 11-53-21](https://github.com/user-attachments/assets/fc8bc204-7d94-4048-a9b5-81efe2d26352)

  - Create the Deployment by running the following command: kubectl apply -f kuber_deployment.yaml or kubectl create -f kuber_deployment.yaml
  - Run "kubectl get pod" to veruty if the pod is created
  - Run "kubectl get deployments" to check if the Deployment is created.
  - ![Screenshot from 2024-08-03 12-06-47](https://github.com/user-attachments/assets/00b8e1a7-9739-422d-ad81-e3b0c41f036b)
 
  - Create a Kubernetes Service of type ClusterIP to expose the application.
  - ![Screenshot from 2024-08-03 12-07-45](https://github.com/user-attachments/assets/b3de9371-86ab-47ae-ba4c-d33425cb743d)
  - run "kubectl apply -f cluster_service.yaml" to use the service created.
  - run "kuberctl get service" to verify.
  - ![Screenshot from 2024-08-03 12-09-31](https://github.com/user-attachments/assets/17888dff-de4a-44cc-bd19-00689afde073)

# Test the deployment:
  - port forward To access the application from within the cluster
  - run "kubectl port-forward service/kodecamp-app 8000:8080"
  - ![Screenshot from 2024-08-03 12-13-14](https://github.com/user-attachments/assets/d6fa9b7f-40d7-4b9a-a1b0-0bebca7a5699)
  ## to verify, 
  - since we are using a live server to this project, we test it by  "curl -v http://127.0.0.1:8000/ping"
  - ![Screenshot from 2024-08-03 12-19-47](https://github.com/user-attachments/assets/706390d3-b901-4684-a506-f2d5838e2f16)

# Additional Configuration
## Configure a ConfigMap to externalize the message "Hello, Kubernetes!" and update your application to read this message from the ConfigMap.
## Create a Secret to store a sensitive piece of information (e.g., a password) and update your application to use this Secret.
  - create a configMap.yaml file:
  - ![Screenshot from 2024-08-03 18-51-30](https://github.com/user-attachments/assets/d22dede1-772f-495d-a30b-2ae0c5d034bc)
  - create a secret.yaml file
  - ![Screenshot from 2024-08-03 18-45-06](https://github.com/user-attachments/assets/406a6622-ec16-4959-8688-6d987aaa92f0)
  - Note: the password was encoded for security purposes.
  - up date "kuber_deployment.yaml":
  - ![Screenshot from 2024-08-03 18-41-12](https://github.com/user-attachments/assets/2414b9eb-773e-4bff-843e-110e71296bc9)
  - apply all the file created using
    -  kuberctl apply -f (filename)
    -  ![Screenshot from 2024-08-03 19-01-48](https://github.com/user-attachments/assets/15282d4f-7ba0-4a57-ac11-01ab33d494e9)

   

    




 




  









 

