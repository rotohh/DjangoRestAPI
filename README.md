# DjangoRestAPI

QUESTION\
Company needs internal service for its’ employees which helps them to make a decision
on lunch place.
Each restaurant will be uploading menus using the system every day over API
Employees will vote for menu before leaving for lunch on mobile app for whom backend has to be
implemented
There are users which did not update app to the latest version and backend has to support both
versions.
Mobile app always sends build version in headers.
Needed API’s:\
o Authentication
o Creating restaurant
o Uploading menu for restaurant (There should be a menu for each day)
o Creating employee
o Getting current day menu
o Voting for restaurant menu (Old version api accepted one menu, New one accepts top three
menus with respective points (1 to 3)
o Getting results for current day

TECHNOLOGIES\
Python3\
DRF\
SQLite\

RUNNING THE PROJECT\
sudo docker-compose down\
$ sudo docker-compose build\
$ sudo docker-compose up --detach\


DOCUMENTATION OF API

I have Created API Documentation with Swagger:\

After launch of the api, to view the documentation\
     go to: http://localhost:8000/swagger/\

Default admin\

username: admin\

password: lunchapi\

username : mindtale\

password : lunchapi\


All Employees\
username:  employee1\
password:   lunchapi\

username:  employee2\
password:   lunchapi\

username:  employee3\
password:   lunchapi\
         |  \
         upto\
         |\
         
username:  employee10\
password:   lunchapi\
