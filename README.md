# drf_react_crud

Steps:-
1.  pip install django
2.  pip install djangorestframework
3.  pip install django-cors-headers
    Because we will be sending requests from the front-end side of our application to our API, we will install the django-cors-headers. This is a Django        application that handles server headers to responses for Cross-Origin Resource Sharing (CORS).
    
4.  django-admin startproject backend_project 
5.  python manage.py startapp backend_api
6.  then install in setting.py
7.    INSTALLED_APPS = [
                            #own
                            'backend_api',

                            #third_party
                            'rest_framework',
                            'corsheaders',
                            ]
                            
8.  Now, add the middleware CORS in settings.py

        MIDDLEWARE = [
                          . . .,
                          'corsheaders.middleware.CorsMiddleware',
                          'django.middleware.common.CommonMiddleware',
                          . . .,

                      ]
                      
                      
9.  Finally, add the React’s port through which requests will come be served, to the CORS_ORIGIN_WHITELIST.
   This code snippet is added to the backend_project/settings.py file.
          CORS_ORIGIN_WHITELIST = [
                                      'http://localhost:3000',
                                  ]
                                  
                                  
Creating the API:-
10. creating models in models.py
11. Creating serializer in serializers.py
12. Define viewsets.
13. creating urls.py file in application folder(backend_api)

      from backend_api.views import MovieViewSet
      from rest_framework.routers import DefaultRouter
      from backend_api import views

      router = DefaultRouter()
      router.register(r'movies', views.MovieViewSet, basename='movie')
      urlpatterns = router.urls
      
      
Creating the application’s front-end using React 
1.  The react application needs to be installed via this command. Where frontend is our app’s name.
        npx create-react-app frontend
        
2.  After you install the app, run the following. The project’s local server will start on a port and the browser will render the first react app.

      cd frontend
      npm start

   
   
   
   
