# DjangoRestAPI

QUESTION


Company needs internal service for its’ employees which helps them to make a decision
on lunch place.
Each restaurant will be uploading menus using the system every day over API
Employees will vote for menu before leaving for lunch on mobile app for whom backend has to be
implemented
There are users which did not update app to the latest version and backend has to support both
versions.
Mobile app always sends build version in headers.


Needed API’s:


     o Authentication
     o Creating restaurant
     o Uploading menu for restaurant (There should be a menu for each day)
     o Creating employee
     o Getting current day menu
     o Voting for restaurant menu (Old version api accepted one menu, New one accepts top three
     menus with respective points (1 to 3)
     o Getting results for current day

TECHNOLOGIES


     Python3

     
     DRF


     SQLite



RUNNING THE PROJECT


     docker pull rotohh/mydjangoapi (pull image from repository at https://hub.docker.com/r/rotohh/mydjangoapi/tags to your own computer)
     
     
     docker-compose up     (Then run this)




DOCUMENTATION OF API

     I have Created API Documentation with Swagger:



     After launch of the api, to view the documentation
     go to: http://localhost:8000/swagger/
     
     

Default admin Authentication credentials



     username: admin



     password: lunchapi



     username : mindtale



     password : lunchapi




All Employees Authentication credentials


     username:  employee1


     password:   lunchapi



     username:  employee2


     password:   lunchapi



     username:  employee3


     password:   lunchapi


         |  
         
         
         upto
         
         
         |
         
         
         
     username:  employee10
     
     
URL ACTIONS
     
     
     http://localhost:8000/admin/     (login as admin page)


     http://localhost:8000/api/v1/employee/   (login as employee)


     http://localhost:8000/api/v1/logout      (logout users)
     
     
     http://localhost:8000/api/v1/employee-profile/ (look at employee profile)
     
     
     http://localhost:8000/api/v1/employee/3/ (look at employee detail with 3 being identifier id)
     
     
     http://localhost:8000/api/v1/employee-profile/3/ (look at employee profile detail)
     
     
     http://localhost:8000/api/v1/employee-get-menu/ (get menu list)
     
     
     http://localhost:8000/api/v1/restaurant/   (get restaurant names in the list)
     
     
     http://localhost:8000/api/v1/restaurant/1/ (get restaurant detail with 1 being the restaurant identifier)
     
     
     http://localhost:8000/api/v1/restaurant-profile/ (gets restaurant profile list)
     
     
     http://localhost:8000/api/v1/restaurant-menu/1/ (gets menu instances with 1 being the menu identifier)

     http://localhost:8000/swagger/ (The api documentation )
     
     
     http://localhost:8000/redoc/ (Complete project documentation)
