# Google Cloud Endpoints & App Engine Flex & Connexion Sample Application

This sample demonstrates how to use Google Cloud Endpoints for a Connexion based Python API hosted on Google App Engine Flexible environment.

It's basically the "curated" mix of three other repos:
1. [Google Cloud Endpoints Client Samples](https://github.com/GoogleCloudPlatform/endpoints-samples).
1. [Google Cloud Endpoints Python Getting Started](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/endpoints/getting-started).
1. [Connexion Example REST Service](https://github.com/hjacobs/connexion-example).

This sample consists of two parts:

1. The backend code and configuration
1. A frontend application to showcase web clients authentication options: Firebase Auth and Google Accounts

## Set up your project
The first thing to do is create a project in the Google Cloud console. Take note of your project ID and replace all the `[PROJECT_ID]` placeholders with your actual project ID, that you assigned while creating the project.

In order to use Firebase Auth you need to also create a Project in the Firebase Console [follow the instructions here](https://github.com/GoogleCloudPlatform/endpoints-samples/tree/master/clients/firebase-js) in this sample I used the same project ID for both. Paste the initialization code snippet into `/frontend/firebase.html`

Also make sure to generate an OAuth client ID [follow the instructions here](https://github.com/GoogleCloudPlatform/endpoints-samples/tree/master/clients/google-js) and replace the placeholder `[GOOGLE_OAUTH_CLIENT_ID]` inside `/frontend/google.html` and in `/backend/openapi.yaml` with it. 

## Running locally

### Running the backend

```bash
$ cd backend
```

Install all the dependencies:
```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Run the application:
```bash
$ python app.py
```

### Running the frontend
```bash
$ cd frontend
```
To launch the frontend you can install and use `serve` 
```bash
$ npm install -g serve
$ serve .
```
## Deploying to Production

### Deploying the Endpoints configuration
Deploy the Open API spec file to Google Cloud Endpoints services management using the Gcloud CLI
```bash
$ gcloud endpoints services deploy openapi.yaml
```

After the deployment finish, take note of the assigned version and replace the `[API_VERSION]` placeholder inside of `/backend/app.yaml`.

### Deploying the backend to App Engine
```bash
$ gcloud app deploy
```
With that you are ready to access the API using this URL:
[https://[PROJECT_ID].appspot.com](https://[PROJECT_ID].appspot.com)

### Deploying the Frontend to Firebase Hosting
Go to the frontend folder
```bash
$ cd frontend
```
Install Firebase command line tools and authenticate and setup the project ID
```bash
$ npm install -g firebase-tools
$ firebase login
$ firebase use [PROJECT_ID]
```
With that you are ready to deploy
```bash
$ firebase deploy
```
With that you are ready to access the app in this URL:
[https://[PROJECT_ID].firebaseapp.com](https://[PROJECT_ID].firebaseapp.com)
