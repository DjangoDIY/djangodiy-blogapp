djangodiy_blog_app
=================

**djangodiy-blogapp** is a Django app that provides a full-featured blogging system, allowing users to create posts, categories, tags, and manage comments.

Features
--------
- Create and manage blog posts.
- Organize posts with categories and tags.
- Commenting system to engage with visitors.
- Easy to integrate into any Django project.

Installation
------------
To install the app, run the following command:

.. code-block:: bash

    pip install djangodiy-blogapp

After installation, add `'djangodiy_blogapp'` to your `INSTALLED_APPS` in your Django project settings:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'djangodiy_blogapp',
        ...
    ]

Then, run migrations to create the necessary database tables:

.. code-block:: bash

    python manage.py migrate

if you see an error then paste the below code in Project/settings.py

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
