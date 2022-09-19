# Charlene's Project 1
IDS 706 project 1.

## Introduction
The project converts an NBA player statistics dataset from Kaggle to make it run on Dask.

Diagram below shows how data in the selected dataset being transferred from original source (Kaggle) to user.

![Untitled Diagram drawio](https://user-images.githubusercontent.com/45677438/190946610-d380f723-a5ea-4c92-afac-600c04174480.png)

## How to Run 
```./query_sql_db.py cli-query --query YOUR_SQL_QUERY```  

Fastapi:
```python fastapi-app.py```
then add ```/query``` after the address

## To check databricks connection
```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```
