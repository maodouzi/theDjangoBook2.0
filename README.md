theDjangoBook2.0
================

# Ref

	git://github.com/jacobian/djangobook.com.git
	git://github.com/maodouzi/theDjangoBook2.0.git

# Step

1.	Getting Started
	
	1.	Init django project

		Commonds£º
		
			sudo pip install django
			sudo chmod a+r -R /usr/local/lib/python2.7/dist-packages/
			django-admin.py startproject mysite
			cd mysite
			./manage.py runserver 0.0.0.0:8080			

			http://localhost:8080/

		Blue Welcome Page
	
	1.	Hello£¬world
		
		setting.py: ROOT_URLCONF = 'mysite.urls'

	1.	My home page view

		url(ctrl) & view

	1.	Dynamic Content: Time
	
		1.	offset is string, if be sent to datetime as int arg, exception raised
		
		1.	view use "try catch" double check even if url has already use regex: \d{1,2}, loosely coupled for reuse.

1. 


Dynamic urls
Dynamic Content: Time
My home page view
hello, world!
Init django project

