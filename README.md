<H1>Expense traker api source code</H1>


Endpoints:

admin/ - admin panel

Head to the root web address. A swagger module will guide you trough all the possible API endpoints with examples as in the image below:
<img src="images/swagger.png">





Useful commands:

docker-compose build . -> build the dependencies and docker image

docker-compose up -> start the server

docker-compose run --rm app sh -c "python manage.py createsuperuser" -> create superuser

docker-compose run --rm app sh -c "python manage.py test" -> run the tests


docker-compose -f docker-compose-deploy.yml up --build -> run the server in production mode with nginx proxy if Alpine