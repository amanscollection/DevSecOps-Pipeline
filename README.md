🎯 Goal

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

🧰 Tools  
  * GitHub  
  * Jenkins / GitHub Actions  
  * Docker
  * SonarQube  
  * OWASP ZAP  
  * Trivy (container scanner)

  
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
  



## Author
Amandeep Singh
