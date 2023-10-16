# Kidney_Diseease_Classification


## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


# How to run?


### STEPS:

Clone the repository

```bash
https://github.com/hamzajakouk/Kidney_Diseease_Classification_MLFLOW_DVC.git
```

### STEP 01 : Createa conda environment after opening the repository

```bash
conda create -n "name of the environment" python=3.8 -y
```

``` 
conda activate (name of the environment) 
```

### STEP 02 : install requirements from the repository

```bash
pip install -r requirements.txt
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/hamzajakouk/Kidney_Diseease_Classification_MLFLOW_DVC.mlflow 
MLFLOW_TRACKING_USERNAME=hamzajakouk 
MLFLOW_TRACKING_PASSWORD=29cfead8f9e5f527b1c0652a73c807159f5ea80b 
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/hamzajakouk/Kidney_Diseease_Classification_MLFLOW_DVC.mlflow

export MLFLOW_TRACKING_USERNAME=hamzajakouk 
export MLFLOW_TRACKING_PASSWORD=29cfead8f9e5f527b1c0652a73c807159f5ea80b 