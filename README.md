# Job-Intelligence

## Contents
- Overview
- Datasets
- Repository Structure

## Overview

The purpose of this analysis is to recommend people to jobs based on their resumes. The datasets used are a resume dataset with sample resumes and a job posting dataset. This repository contains notebooks for data preprocessing, eda, modeling, and an app with the goal of recommending jobs.

## Datasets

- https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset
- https://huggingface.co/datasets/jacob-hugging-face/job-descriptions

## Repository Structure
```
└── 📁Job-Intelligence
    └── 📁data
        ├── job_clean.csv
        ├── resume_clean.csv
        ├── Resume.csv
        ├── training_data.csv
    └── 📁deliverable
        ├── app.py
        ├── app.txt
        ├── job_clean.csv
    └── 📁notebooks
        └── 📁.ipynb_checkpoints
            ├── Data_Preprocessing-checkpoint.ipynb
            ├── EDA-checkpoint.ipynb
        ├── data_modeling.ipynb
        ├── Data_Preprocessing.ipynb
        ├── EDA.ipynb
        ├── ML - Baseline Model.ipynb
    ├── gitignore.txt
    └── README.md
```