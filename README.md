🎯 **Goal**

This project demonstrates integration of security into CI/CD pipelines (DevSecOps) including SAST, DAST, and container scanning.

# DevSecOps-Pipeline
Build a CI/CD pipeline with built-in security checks.  

 **Architecture Overview**
   
   Your pipeline will look -:
   * Code Push → GitHub Actions → Build → Test → Security Scan → Deploy
  
   We’ll use:
      * CI/CD: GitHub Actions
      * Containerization: Docker
      * Security Scan: Trivy
      * Deployment: AWS EC2 / S3 / or Docker Hub

🧰 **Tools**  
  * GitHub  
  * Jenkins / GitHub Actions  
  * Docker
  * SonarQube  
  * OWASP ZAP  
  * Trivy (container scanner)

**Project Structure**  

      project/  
       ├── app.py  
       ├── requirements.txt  
       ├── Dockerfile  
       ├── tests/  
       │    └── test_app.py  
       └── .github/  
            └── workflows/  
                 └── devsecops.yml  
  
🪜 Step-by-step  

STEP 1: Create simple web app  

* Use Python Flask
* Push to GitHub

STEP 2: Setup CI/CD pipeline  

* Use GitHub Actions
* Pipeline stages:
  * Build
  * Test
  * Security scan
  * Deploy
  
STEP 3: Create Dockerfile (Build Stage)  

      FROM python:3.10 
   
      WORKDIR /app  
      COPY . .  
   
      RUN pip install -r requirements.txt  
   
      CMD ["python", "app.py"]   

STEP 4 — GitHub Actions Workflow  
      .github/workflows/devsecops.yml  

      FULL PIPELINE  
      name: DevSecOps Pipeline
      on:
        push:
          branches: [ "main" ]

      jobs:

        build:
          runs-on: ubuntu-latest

       steps:
          - name: Checkout Code
            uses: actions/checkout@v3

          - name: Build Docker Image
            run: docker build -t myapp .

        test:
          runs-on: ubuntu-latest
          needs: build

          steps:
             - uses: actions/checkout@v3

             - name: Install Dependencies
               run: pip install -r requirements.txt

             - name: Run Tests
               run: pytest

        security_scan:
          runs-on: ubuntu-latest
          needs: test

          steps:
             - uses: actions/checkout@v3

             - name: Install Trivy
               run: |
                 sudo apt-get install wget apt-transport-https gnupg lsb-release -y
                 wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
                 echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee                                     /etc/apt/sources.list.d/trivy.list
                 sudo apt-get update
                 sudo apt-get install trivy -y

             - name: Scan Docker Image
               run: trivy image myapp

           deploy:
             runs-on: ubuntu-latest
             needs: security_scan

             steps:
                - name: Deploy to Server
                  run: echo "Deploying app..."

STEP 5 — Deployment to DockerHub

            - name: Login to DockerHub
              run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

            - name: Push Image
              run: |
                docker tag myapp username/myapp
                docker push username/myapp  
 
 Deployment to AWS EC2 Deployment  
 
       - name: Deploy via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ubuntu
          key: ${{ secrets.SSH_KEY }}
          script: |
            docker pull username/myapp
            docker stop myapp || true
            docker run -d -p 80:5000 username/myapp  

STEP 6 — Add Advanced Security for DevSecOps  

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2

STEP 7 - Dependency Scan  

   - name: Dependency Check
     run: pip install safety && safety check

## Author
Amandeep Singh
