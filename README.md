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

3.  Then Follows the App.js in (src folder)

4.  Using the Axios API: - 
    the Axios API will be used here to make requests to the backend
        npm install axios
        
5.  To style the app, we will install and use the React-Bootstrap framework using the npm package.
        npm install react-bootstrap bootstrap@5.1.3
        
6.  This bootstrap framework requires a stylesheet for some components. Therefore, include this line of code in your src/index.js or App.js file
        import 'bootstrap/dist/css/bootstrap.min.css';
        
7.  We will separate the Axios configuration logic in a separate component file and just import it into our application component which we will name        AddMovie.js. This is always a cleaner, readable and simple way of implementing the Axios API and our code in general. Therefore, create a file named      API.js within the src directory and add this code.

        import axios from 'axios';

        export default axios.create({
            baseURL: "http://127.0.0.1:8000/backend_api/movies",    # This is drf url 
            headers: {
                'Accept':'application/json',
                'Content-Type':'application/json',
            }
        }
   
8.  Do not forget to import the AddMovie.js component to the App.js file. This is the only way it can be rendered to the browser.

        import './App.css';
        import AddMovie from './AddMovie'

        function App() {

          return (
            <div className="App">
              <AddMovie/>           #this line

            </div>
          );
        }

        export default App;
        
10. Don't forgot to add fontawasome link to delete and update operation to the AddMovies.js into head.
                    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" />

