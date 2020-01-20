# UDN Developer Test
<hr/>

### Introduction 
At the Department of Biomedical Informatics the Data Core assists faculty members with the creation of tools to enable cutting edge research in multidisciplinary fields. Common tasks such as data warehousing, collection, or protection are not the expertise of the clinical faculty and it’s our job to be those specialists.

### Project Description 
A key project managed by DBMI is the Undiagnosed Diseases Network (UDN). The UDN platform is a web app that collects information about participants and allows hospitals, medical centers, and research staff share and review participant information.

For this test we would like you to create a small web app. Specifically you should create two views: 1) add a participant by presenting a form that gathers details about a participant and 2) display a list of all participants with their data in a table.

<hr/>

### Getting started 

<ol>
  <li>
    Start by creating an empty python3 enviornment <br/>
    `python3 -m venv <myenviornmentname> `
    
  </li>
  <li>
    Activate the enviornment <br/>
    `source <myenviornmentname>/bin/activate`
  
  </li>
  <li>
    Change into the root directory of the project and install the requirements file.
  </li>
  <li>
    Cd into the app directory and you can now make initial migrations with <br/>
    `python manage.py makemigrations` 
   
  </li>
  <li>
    Once migrations have been made you can start the application with <br/>
    `python manage.py runserver`
  </li>
</ol>
