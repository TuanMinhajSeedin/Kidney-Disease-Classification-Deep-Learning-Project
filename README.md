# Kidney-Disease-Classification-Deep-Learning-Project

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/TuanMinhajSeedin/Kidney-Disease-Classification-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney-user python=3.9 -y
```

```bash
conda activate kidney-user
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
streamlit run streamlitapp.py
```

Now,
```bash
open up you local host and port
```

### Dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI="https://dagshub.com/TuanMinhajSeedin/Kidney-Disease-Classification-Deep-Learning-Project.mlflow"\
MLFLOW_TRACKING_USERNAME="github-user-name"\
MLFLOW_TRACKING_PASSWORD="mlflow-password"

```bash
Run this as environment variables

export MLFLOW_TRACKING_URI=https://dagshub.com/TuanMinhajSeedin/Kidney-Disease-Classification-Deep-Learning-Project.mlflow
export MLFLOW_TRACKING_USERNAME=github-user
export MLFLOW_TRACKING_PASSWORD=github-password