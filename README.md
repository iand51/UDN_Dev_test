# UDN Developer Test
<hr/>

### Introduction 
At the Department of Biomedical Informatics the Data Core assists faculty members with the creation of tools to enable cutting edge research in multidisciplinary fields. Common tasks such as data warehousing, collection, or protection are not the expertise of the clinical faculty and it’s our job to be those specialists.

### Project Description 
A key project managed by DBMI is the Undiagnosed Diseases Network (UDN). The UDN platform is a web app that collects information about participants and allows hospitals, medical centers, and research staff share and review participant information.

For this test we would like you to create a small web app. Specifically you should create two views: 1) add a participant by presenting a form that gathers details about a participant and 2) display a list of all participants with their data in a table.

<hr/>

### Getting started 
  
   1. Start by creating an empty python3 enviornment <br/>
    `python3 -m venv <myenviornmentname> `
    

   2. Activate the enviornment <br/>
    `source <myenviornmentname>/bin/activate`

   3. Change into the root directory of the project and install the requirements file.


   4. Cd into the app directory and you can now make initial migrations with <br/>
    `python manage.py makemigrations` 
   
   5. Once migrations have been made you can start the application with <br/>
    `python manage.py runserver`

<hr/>

### Using the application

1. The home page of the application will promt you with a basic sign in form like any application that requires a unique user to sign in and use. If a user already has an account then sign in with their username and password, if not click on the "sign up now" button which will bring you to a sign up form. 

2. The form will ask for the following entries 
  - Username 
  - First Name 
  - Age 
  - Does the participant have any siblings?
  - Any known Enviormental Exposures?
  - Any Known Genetic Mutations?
  - Passwords 
  
  Fill out the form and click sign up. If all the information validates then it will redirect you to the inital login page so you can now sign up with your new account!
  
3. Upon sign in you will be brought to the participant home page where you will see a table of all the users information with the columns 
  |Name|age|siblings|genetic mutations|env exposures|  
  
4. Note to add information to the column one must sign up under a new user, or the admin can add one on the admin panel. 

<hr/>

### Running the tests

- To run the applications test simply run <br/>
 `python manage.py test` in the app directory 
 
- I did my best to have the tests cover as much of the application as possible given the time frame. They cover 
  1. Models 
  2. Views 
  3. Forms 

<hr/>

### Additional Information 
- to create a superuser simply cd into the app directory and run the command<br/>
`python manage.py createsuperuser` 
