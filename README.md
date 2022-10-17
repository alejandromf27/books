Ergeon Home Challenge Rest API is a Django

Authors:
    
    Angel Garcia alejandromf27@gmail.com

REST API Functionalities:

    {
        "books": "http://localhost:8000/books/",
        "authors": "http://localhost:8000/authors/",
        "authors_books": "http://localhost:8000/authors_books/"
    }   


You can deploy the project with Docker following the steps below (recommended):

DEPLOY 

    Docker set up:
    
        1. Install Docker (https://docs.docker.com/install/linux/docker-ce/ubuntu/)
        
            Warning: On Ubuntu 20.04 Focal Fossa install docker from: (https://linuxconfig.org/how-to-install-docker-on-ubuntu-20-04-lts-focal-fossa)
        
        2. Check docker version
        
            $ docker --version    
            
        3. Install docker-compose (https://docs.docker.com/compose/install/)
        
        4. Check docker compose version
        
            $ docker-compose --version
        
        5. Check docker services status        
        
            $ sudo systemctl status docker
            
    Launch Django project
    
       1. Move to project dir
        
           $ cd books/

       3. Create environment variables:

           $ nano env

       4 Inside paste this:

            DB_SERVICE=books_psql
            DB_PORT=5432
            POSTGRES_USER=postgres
            POSTGRES_DB=books_db
            POSTGRES_PASSWORD=mysecretpassword
            SECRET_KEY=bookssecretkey
            DEBUG=1
            ALLOWED_HOSTS=127.0.0.1,localhost
    
       5. Build containers and run project with docker compose
        
           $ docker-compose build (use this option the first time to build the containers)

           $ docker-compose up -d

       6. Stop docker container: 

           $ docker-compose down (-v optional to destroy container and data)
            
       7. Launch Django static
        
           $ docker-compose run books_app python3 manage.py collectstatic

       8. Execute migrations:
        
           $ docker-compose run books_app python3 manage.py migrate
            
       9. Create Django superuser
        
               $ docker-compose run books_app python3 manage.py createsuperuser

       10. Load initial data (apps fixtures)
           $ docker-compose run books_app python3 manage.py loaddata */fixtures/*.json
                
   Running Tests Code Coverage:

       $ docker-compose run books_app coverage run --source='.' manage.py test (the-app-you-want-to-test) # optional

       $ docker-compose run books_app coverage report
