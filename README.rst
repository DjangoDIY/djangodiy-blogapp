djangodiy_blog_app
=================

djangodiy_blog_app is a Django app that provides a full-featured blogging system, allowing users to create posts, categories, tags, and manage comments.

Features
--------
- Create and manage blog posts.
- Organize posts with categories and tags.
- Commenting system to engage with visitors.
- Easy to integrate into any Django project.

Getting Started
=========================

To use the djangodiy-blogapp in your Django project, follow these steps:

1. **Clone the Repository**

   First, you need to download your repository from GitHub. Open your terminal and run the following command:

   .. code:: bash

      git clone https://github.com/DjangoDIY/djangodiy-blogapp.git

   This will create a directory named `djangodiy-blogapp` containing your project files.

2. **Navigate to the Directory**

   Change into the cloned repository directory:

   .. code:: bash

      cd djangodiy-blogapp

3. **Add the App to Your Project**

   In your Django project's `settings.py`, add `'djangodiy_blog_app'` to the `INSTALLED_APPS` list:

   .. code:: python

      INSTALLED_APPS = [
          ...
          'djangodiy_blog_app',
      ]

4. **Run Migrations**

   After adding the app, you need to apply the migrations. Run the following command:

   .. code:: bash

      python manage.py migrate

5. **Run the Development Server**

   Finally, start the Django development server to see your app in action:

   .. code:: bash

      python manage.py runserver

6. **Update Project's urls.py file**

   Finally, start the Django development server to see your app in action:

   .. code:: python

        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('blog/', include('djangodiy_blog_app.urls'))
        ]


if you see an error related to models then paste the below code in Project/settings.py

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

Usage
-----
Once installed, you can start adding posts, categories, tags, and comments from your Django admin panel.

License
-------
This project is licensed under the BSD License - see the `LICENSE` file for details.

Contributing
------------
If you want to contribute to this project, feel free to fork the repository and submit a pull request!
