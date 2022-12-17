### <center>MLZC Capstone Project 1 - Q4/2022<img align="right" src="media\insulina_124.jpg">
  
# <center> Diabetes Health Indicators Dataset  


# Purpose and context:

Diabete is a growing concern in many countries.  
The idea of the project is to try to predict the probablility of a patient, in certain conditions, to be diagnozed with diabete.   

In USA, the "Behavioral Risk Factor Surveillance System" (BRFSS https://www.cdc.gov/brfss/index.html) conduct each year an intensive survey to collect indicator around diabete.    

Original dataset contains about 330 features but various contributions have builded in Kaggle a simplified dataset with the 22 main features for year 2015:  

- https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset


For this project, the biggest file (253k records) has been selected:
- **diabetes _ binary _ health _ indicators _ BRFSS2015.csv** :      
    - *"This is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015.* 
    - *The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes.* 
    - *This dataset has 21 feature variables and is not balanced."*


# Project:

- Data were analysed to identify the main features, importance, correlation...
- Several models of Binary classification (LR, Tree, RandomForest, xgboost) have been developed and tested (parameters tuning).
- Best model (xgboost) after re-trained was exported and containerized using bentoml/docker.
- Docker image has been pushed to DockerHub and implemented in the cloud as a service (Kubernetes in mogenius).

- Progress are detailled in jupyter notebooks:
    - Installation: [cp1-01-installation.md](cp1-01-installation.md) 
    - EDA and training: [cp1-10-EDA and Training.ipynb](cp1-10-EDA%20and%20Training.ipynb) 
    - Deployment: [cp1-50-Deplyment.ipynb](cp1-50-Deplyment.ipynb)


# Features:
Source: https://www.kaggle.com/code/alexteboul/diabetes-health-indicators-dataset-notebook/notebook   

The 21 features selected as the most important risks factors (between 330) are:
- blood pressure (high)
- cholesterol (high)
- smoking
- diabetes
- obesity
- age
- sex
- race
- diet
- exercise
- alcohol consumption
- BMI
- Household Income
- Marital Status
- Sleep
- Time since last checkup
- Education
- Health care coverage
- Mental Health 

# Data Download:

- Use Kaggle dataset:
    - https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv
  
<p> <img align="center" src="media\2022-12-17 15_58_02-Diabetes Health Indicators Dataset _ Kaggle.jpg" , width="800" >



- Or csv from this repository:
    - [/data/diabetes_binary_health_indicators_BRFSS2015.csv](/data/diabetes_binary_health_indicators_BRFSS2015.csv)

# Repository Content:
git: https://github.com/AlainDot/mlzc-cp1 

In addition to readme and notebooks:
- [bentoml folder](/bentoml/): copy of saved models (to dockerize without training)
- [data folder](/data/): source dataset
- [media folder](/media/): some images
- [Pipfile file](/Pipfile): project is based on pipenv
- [bentofile.yaml file](/bentofile.yaml) to dockerize saved model
- [train_patient_diabete_risk.py](/train_patient_diabete_risk.py) to train final xgboost model and save it to bentoml

# Rebuild/Test project:

- Clone the git repository (https://github.com/AlainDot/mlzc-cp1)   
<br>    
- Create a dedicated folder and pipenv environment (see [Pipfile file](/Pipfile))   
    - See [cp1-01-installation.md](/cp1-01-installation.md) for how to use "pipenv" and install packages     
<br>    
- Run the notebooks or directly train the model using the script [train_patient_diabete_risk.py](/train_patient_diabete_risk.py)   
<br>    
- Dockerize the model and deploy it to the Cloud following [cp1-50-Deplyment.ipynb](cp1-50-Deplyment.ipynb)    
    - bentoml image deployed here (includes trained model) is available in [bentoml folder](/bentoml/)   
    - Free account has to be created at https://studio.mogenius.com/     
<br>    
- Or using swagger, test the model deployed (if running!):        
    - https://alaindut-patie-prod-patient-death-risk-service-xejta4.mo5.mogenius.io/    
