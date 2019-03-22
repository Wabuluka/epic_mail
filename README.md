# epic_mail
[![Build Status](https://travis-ci.com/Wabuluka/epic_mail.svg?branch=develop)](https://travis-ci.com/Wabuluka/epic_mail) [![Maintainability](https://api.codeclimate.com/v1/badges/8e24e2c5b57349dfdee5/maintainability)](https://codeclimate.com/github/Wabuluka/epic_mail/maintainability) [![Coverage Status](https://coveralls.io/repos/github/Wabuluka/epic_mail/badge.svg?branch=develop)](https://coveralls.io/github/Wabuluka/epic_mail?branch=develop)

A web app that helps people exchange messages or information over the internet. Epicmail is an API that helps a developer implement the required features such that a frontend can communicate with the backend. In this API however, only the backend has been implemented and postman can be used to mimic the frontend.

## Getting Started
To get epicmail working there are two versions of requirements that am going going to breakdown.
* The API has been hosted with heroku so in case one can not get through it manually, it is already in demo mode.
* The other way of getting the Epicmail API to work is by configuring it manually. Here one clones the entire repository and runs the API locally

### Prerequisites
These are the requirements for the manual testing of the API

```
$ git clone https://github.com/Wabuluka/epic_mail.git
```
This clones the entire repository on to a local machine.

```
$ cd epic_mail
```
On a Linux machine, this command will move the working area of the terminal into the Epicmail folder. While in this folder's root, create a virtual environment to isolate the API dependencies from those of other apps running on the machine.

```
$ python3 -m venv venv
```
This one of the many ways in which a virtual environment can be created for the API to work in an isolated environment.

After the virtual environment is successfully created, it must be active before proceeding.
```
$ source venv/bin/activate
```
For Linux users
```
$ source venv/Scripts/activate
```
For users on Windows platforms

With an active environment, install all the the required dependencies
```
$ pip install -r requirements.txt
```
After installation, to run the API make sure you have Postman installed on your machines. This helps to simulate all the methods of the API
When all is set, run the API
```
$ python run.py
```
After successfully runing the API, you can now have the oppotunity to interract with the urls as specified in the table below.

### Table of endpoints and their descriptions as used in the API
|   METHODS     |   URL ENDPOINT                        |   DESCRIPTION                 |
|---------------|---------------------------------------|-------------------------------|
|   POST        |/epicmail/v2/api/auth/signup/          |Create a new user              |
|   POST        |/epicmail/v2/api/auth/signin/          |Signin a registered user       |
|   POST        |/epicmail/v2/api/messages/             |Create a new message           |
|   GET         |/epicmail/v2/api/messages/<int:id>     |Get a one message              |
|   GET         |/epicmail/v2/api/messages/unread       |Get unread messages            |
|   GET         |/epicmail/v2/api/messages/sent         |Get all sent messages          |
|   GET         |/epicmail/v2/api/messages/received     |Get all received messages      |
|   DELETE      |/epicmail/v2/api/messages/<int:id>     |Delete a messages              |

## Testing
To run the unittests
```
$ pytest --cov
```

## Deployment
This API has been deployed on Heroku for live viewing. The link can be found below
[epicmail on heroku](https://epicmailwabuluka.herokuapp.com/epicmail/api/v2/auth/signup) - Live demo

## Developer
**Davies Wabuluka**