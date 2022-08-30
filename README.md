# Overview

The second project of DevOps Udacity Nanodegree was focused on building CI/CD pipelines in a machine learning project. The goal was to automatically integrate and deploy changes in the project.

## Project Plan
The project plan expects to deliver the machine learning application in one year. So, from a basic idea until the go-live, it should take approximately one year including the training the prediction model, analysing its results and implementing front-end and back-end.

* The week-by-week plan can be found in the online spreadsheet: [https://docs.google.com/spreadsheets/d/1NQyCdQkhMzS_OXzM_0zBACwfOxT06Md75_RDT5klGmc/edit#gid=1348135932](Project Plan spreadsheet)
* Trello board for the project with main tasks: [https://trello.com/b/14yYiJMS/project-tasks](Trello board)

## Instructions

* Architectural Diagram
* 



* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>




[![Python application test with Github Actions](https://github.com/lengyellukas/devops_nano_pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/lengyellukas/devops_nano_pipeline/actions/workflows/pythonapp.yml)

