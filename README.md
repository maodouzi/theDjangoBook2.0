theDjangoBook2.0
================

# Ref

	https://github.com/jacobian/djangobook.com.git
	https://github.com/maodouzi/theDjangoBook2.0.git

# Step

1.	Introduction to Django

1.	Getting Started
	
	1.	Init django project

		Commonds:
		
			sudo pip install django
			sudo chmod a+r -R /usr/local/lib/python2.7/dist-packages/
			django-admin.py startproject mysite
			cd mysite
			./manage.py runserver 0.0.0.0:8080			

			http://localhost:8080/

		Blue Welcome Page

1.	Views and URLconfs
	
	1.	Hello, world
		
		setting.py: ROOT_URLCONF = 'mysite.urls'

	1.	My home page view

		url(ctrl) & view

	1.	Dynamic Content: Time
	
		1.	offset is string, if be sent to datetime as int arg, exception raised
		
		1.	view use "try catch" double check even if url has already use regex: \d{1,2}, loosely coupled for reuse.

	1.	Dynamic Url

		1.	multi-url => view

1.	Templates
	
	1.	Overview

		Variable: 

			{{ var }}

		Tag: 
			
			{% if ordered_warranty %}
			{% else %}	# Optional, no elif
			{% endif %}

			{% for athlete in athlete_list %}
				<li>{{ athlete.name }}</li>
			{% endfor %}

			ifequal & comment & include & block

		Filter:

			{{ ship_date|date:"F j, Y" }}

	1.	Django Shell

			cd /windows/local/github/theDjangoBook2.0/mysite
			export DJANGO_SETTINGS_MODULE=mysite.settings
			from django.template import Template

		No error means you could use django shell with your django project setting

	1.	Variable

		Basic:

			>>> from django import template
			>>> t = template.Template('My name is {{ name }}.')
			>>> c = template.Context({'name': 'Adrian'})
			>>> print t.render(c)
			My name is Adrian.
			>>> c = template.Context({'name': 'Fred'})
			>>> print t.render(c)
			My name is Fred.

		Dict:

			>>> from django.template import Template, Context
			>>> person = {'name': 'Sally', 'age': '43'}
			>>> t = Template('{{ person.name }} is {{ person.age }} years old.')
			>>> c = Context({'person': person})
			>>> t.render(c)
			u'Sally is 43 years old.'

		Object Attribute:

			>>> from django.template import Template, Context
			>>> import datetime
			>>> d = datetime.date(1993, 5, 2)
			>>> d.year
			1993
			>>> d.month
			5
			>>> d.day
			2
			>>> t = Template('The month is {{ date.month }} and the year is {{ date.year }}.')
			>>> c = Context({'date': d})
			>>> t.render(c)
			u'The month is 5 and the year is 1993.'

		Object Function:

			>>> from django.template import Template, Context
			>>> t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
			>>> t.render(Context({'var': 'hello'}))
			u'hello -- HELLO -- False'
			>>> t.render(Context({'var': '123'}))
			u'123 -- 123 -- True'

		List Index:

			>>> from django.template import Template, Context
			>>> t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
			>>> t.render(Context({'var': 'hello'}))
			u'hello -- HELLO -- False'
			>>> t.render(Context({'var': '123'}))
			u'123 -- 123 -- True'

		Nested Dot:

			>>> from django.template import Template, Context
			>>> person = {'name': 'Sally', 'age': '43'}
			>>> t = Template('{{ person.name.upper }} is {{ person.age }} years old.')
			>>> c = Context({'person': person})
			>>> t.render(c)
			u'SALLY is 43 years old.'

		If, during the method lookup, a method raises an exception, the exception will be propagated, unless the exception has an attribute silent_variable_failure whose value is True. If the exception does have a silent_variable_failure attribute, the variable will render as an empty string, for example:

			>>> t = Template("My name is {{ person.first_name }}.")
			>>> class PersonClass3:
			...     def first_name(self):
			...         raise AssertionError, "foo"
			>>> p = PersonClass3()
			>>> t.render(Context({"person": p}))
			Traceback (most recent call last):
			...
			AssertionError: foo

			>>> class SilentAssertionError(AssertionError):
			...     silent_variable_failure = True
			>>> class PersonClass4:
			...     def first_name(self):
			...         raise SilentAssertionError
			>>> p = PersonClass4()
			>>> t.render(Context({"person": p}))
			u'My name is .'

		By default, if a variable doesn¡¯t exist, the template system renders it as an empty string, failing silently

			>>> from django.template import Template, Context
			>>> t = Template('Your name is {{ name }}.')
			>>> t.render(Context())
			u'Your name is .'

		alters_data=True make any function who wanting to modify rendering object be disabled. Say, for instance, you have a BankAccount object that has a delete() method. If a template includes something like {{ account.delete }}, where account is a BankAccount object, the object would be deleted when the template is rendered! To prevent this, set the function attribute alters_data on the method:

			def delete(self):
				# Delete the account
			delete.alters_data = True

		The template system won¡¯t execute any method marked in this way. Continuing the above example, if a template includes {{ account.delete }} and the delete() method has the alters_data=True, then the delete() method will not be executed when the template is rendered. Instead, it will fail silently.

		Context Objects use standard Python dictionary syntax:

			>>> from django.template import Context
			>>> c = Context({"foo": "bar"})
			>>> c['foo']
			'bar'
			>>> del c['foo']
			>>> c['foo']
			Traceback (most recent call last):
			  ...
			KeyError: 'foo'
			>>> c['newvariable'] = 'hello'
			>>> c['newvariable']
			'hello'
	
	1.	If tag

		False: [], (), {}, "", 0, None, False, (Custom objects that define their own Boolean context behavior)

		If tag: 

			{% if athlete_list and coach_list %}
				Both athletes and coaches are available.
			{% endif %}

			{% if not athlete_list %}
				There are no athletes.
			{% endif %}

			{% if athlete_list or coach_list %}
				There are some athletes or some coaches.
			{% endif %}

			{% if not athlete_list or coach_list %}
				There are no athletes or there are some coaches.
			{% endif %}

			{% if athlete_list and not coach_list %}
				There are some athletes and absolutely no coaches.
			{% endif %}

		{% if %} tags don¡¯t allow and and or clauses within the same tag

			{% if athlete_list or coach_list or parent_list or teacher_list %}

			{% if athlete_list %}
				<p>Here are the athletes: {{ athlete_list }}.</p>
			{% else %}
				<p>No athletes are available.</p>
				{% if coach_list %}
					<p>Here are the coaches: {{ coach_list }}.</p>
				{% endif %}
			{% endif %}

	1.	For tag

		Reversed for tag

			{% for athlete in athlete_list reversed %}
			...
			{% endfor %}

		Nested for tag

			{% for athlete in athlete_list %}
				<h1>{{ athlete.name }}</h1>
				<ul>
				{% for sport in athlete.sports_played %}
					<li>{{ sport }}</li>
				{% endfor %}
				</ul>
			{% endfor %}

		Empty for tag

			{% for athlete in athlete_list %}
				<p>{{ athlete.name }}</p>
			{% empty %}
				<p>There are no athletes. Only computer programmers.</p>
			{% endfor %}

		forloop: counter, counter0, revcounter, revcounter0, first, last, parentloop
			
			{% for item in todo_list %}
				<p>{{ forloop.counter }}: {{ item }}</p>
			{% endfor %}

			{% for object in objects %}
				{% if forloop.first %}<li class="first">{% else %}<li>{% endif %}
				{{ object }}
				</li>
			{% endfor %}

			{% for link in links %}{{ link }}{% if not forloop.last %} | {% endif %}{% endfor %}

			{% for country in countries %}
				<table>
				{% for city in country.city_list %}
					<tr>
					<td>Country #{{ forloop.parentloop.counter }}</td>
					<td>City #{{ forloop.counter }}</td>
					<td>{{ city }}</td>
					</tr>
				{% endfor %}
				</table>
			{% endfor %}

	1.	Ifequal Tag

		ifequal / endifequal

			{% ifequal var1 var2 %}
				<h1>Site News</h1>
			{% else %}
				<h1>No News Here</h1>
			{% endifequal %}

		Only template variables, strings, integers, and decimal numbers are allowed as arguments to {% ifequal %}. 
		
			{% ifequal variable 1 %}
			{% ifequal variable 1.23 %}
			{% ifequal variable 'foo' %}
			{% ifequal variable "foo" %}

	1.	Comment Tag

		Single line:

			{# This is a comment #}

		Multiple lines:

			{% comment %}
			This is a
			multi-line comment.
			{% endcomment %}

	1.	Filter

		Examples:

			{{ name|lower }}
			{{ my_list|first|upper }}
			{{ bio|truncatewords:"30" }}
			{{ pub_date|date:"F j, Y" }}

		More details, see appendix E

	1.	Template & Context

		http://localhost:8080/time/

	1.	Use template file by hand

		Should touch /home/djangouser/templates/mytemplate.html & fix it.

	1.	Use django template

		Notice: Don't forget to add comma in TEMPLATE_DIRS!
		Notice: '/home/django/mysite/templates', not good because of tight coupling
		Notice: Use '/' as path sep even in windows: 
			os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
		Without templates file, notice the TemplateDoesNotExist error in webpage.

	1. Shortcuts: render

		Storing templates in subdirectories of your template directory is easy. In your calls to get_template(), just include the subdirectory name and a slash before the template name, like so:

			t = get_template('dateapp/current_datetime.html')

		Because render() is a small wrapper around get_template(), you can do the same thing with the second argument to render(), like this:

			return render(request, 'dateapp/current_datetime.html', {'current_date': now})

	1.	Include Tag

			{% include "nav.html" %}
			{% include 'includes/nav.html' %}
			{% include template_name %}
			
			# mypage.html

			<html>
			<body>
			{% include "includes/nav.html" %}
			<h1>{{ title }}</h1>
			</body>
			</html>

			# includes/nav.html

			<div id="nav">
				You are in: {{ current_section }}
			</div>

	1.	Block Tag

		If you use {% extends %} in a template, it must be the first template tag in that template. Otherwise, template inheritance won¡¯t work.
	
		If you need to get the content of the block from the parent template, use {{ block.super }}

		http://localhost:8080/time/

		http://localhost:8080/time/plus/3/

1.	Model

	1.	DB Setting
	
			$ cd django_project_dir
			$ export DJANGO_SETTINGS_MODULE=mysite.settings
			>>> from django.db import connection
			>>> cursor = connection.cursor()
	
	1.	First App

			$ cd mysite
			$ python ../manage.py startapp books
			Modify books/model.py & Install app in settings.py
			$ cd ..
			$ python manage.py validate
			$ python manage.py sqlall books	=> show the create sql statements.
			$ python manage.py syncdb

			http://localhost:8080/first_app/

			>>> from mysite.books.models import Publisher
			>>> p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
			...     city='Berkeley', state_province='CA', country='U.S.A.',
			...     website='http://www.apress.com/')
			>>> p1.save()
			>>> p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',
			...     city='Cambridge', state_province='MA', country='U.S.A.',
			...     website='http://www.oreilly.com/')
			>>> p2.save()
			>>> publisher_list = Publisher.objects.all()
			>>> publisher_list
			[<Publisher: Publisher object>, <Publisher: Publisher object>]

		Init & Save at the same time, use create, Notice the last line, with __unicode__, change Publish instances output:

			>>> p1 = Publisher.objects.create(name='Apress',
			...     address='2855 Telegraph Avenue',
			...     city='Berkeley', state_province='CA', country='U.S.A.',
			...     website='http://www.apress.com/')
			>>> p2 = Publisher.objects.create(name="O'Reilly",
			...     address='10 Fawcett St.', city='Cambridge',
			...     state_province='MA', country='U.S.A.',
			...     website='http://www.oreilly.com/')
			>>> publisher_list = Publisher.objects.all()
			>>> publisher_list
			>>> [<Publisher: Apress>, <Publisher: O'Reilly>]

	1.	SQL translation

		Insert:

			>>> p = Publisher(name='Apress',
			...         address='2855 Telegraph Ave.',
			...         city='Berkeley',
			...         state_province='CA',
			...         country='U.S.A.',
			...         website='http://www.apress.com/')
			>>> p.save()

			INSERT INTO books_publisher
				(name, address, city, state_province, country, website)
			VALUES
				('Apress', '2855 Telegraph Ave.', 'Berkeley', 'CA', 'U.S.A.', 'http://www.apress.com/');

		Index 

			>>> p.id
			52    # this will differ based on your own data

		Update
		
			>>> p.name = 'Apress Publishing'	
			>>> p.save()

			UPDATE books_publisher SET
				name = 'Apress Publishing',
				address = '2855 Telegraph Ave.',
				city = 'Berkeley',
				state_province = 'CA',
				country = 'U.S.A.',
				website = 'http://www.apress.com'
			WHERE id = 52;

			UPDATE books_publisher SET
				name = 'Apress Publishing'
			WHERE id=52;

		Selecting Objects

			>>> Publisher.objects.all()
			[<Publisher: Apress>, <Publisher: O'Reilly>]

			SELECT id, name, address, city, state_province, country, website FROM books_publisher;

		Filter

			>>> Publisher.objects.filter(name='Apress')
			[<Publisher: Apress>]

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			WHERE name = 'Apress';

			>>> Publisher.objects.filter(country="U.S.A.", state_province="CA")
			[<Publisher: Apress>]

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			WHERE country = 'U.S.A.'
			AND state_province = 'CA';

			>>> Publisher.objects.filter(name__contains="press")
			[<Publisher: Apress>]

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			WHERE name LIKE '%press%';

		Retrieving Single Objects
			
			>>> Publisher.objects.get(name="Apress")
			<Publisher: Apress>

			>>> Publisher.objects.get(country="U.S.A.")
			Traceback (most recent call last):
				...
			MultipleObjectsReturned: get() returned more than one Publisher --
				it returned 2! Lookup parameters were {'country': 'U.S.A.'}

			>>> Publisher.objects.get(name="Penguin")
			Traceback (most recent call last):
				...
			DoesNotExist: Publisher matching query does not exist.

			The DoesNotExist exception is an attribute of the model¡¯s class ¨C Publisher.DoesNotExist. In your applications, you¡¯ll want to trap these exceptions, like this:

			try:
				p = Publisher.objects.get(name='Apress')
			except Publisher.DoesNotExist:
				print "Apress isn't in the database yet."
			else:
				print "Apress is in the database."

		
		Ordering Data

			>>> Publisher.objects.order_by("name")
			[<Publisher: Apress>, <Publisher: O'Reilly>]

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			ORDER BY name;

			>>> Publisher.objects.order_by("state_province", "address")
			[<Publisher: Apress>, <Publisher: O'Reilly>]

			>>> Publisher.objects.order_by("-name")
			[<Publisher: O'Reilly>, <Publisher: Apress>]

			class Publisher(models.Model):
				name = models.CharField(max_length=30)
				address = models.CharField(max_length=50)
				city = models.CharField(max_length=60)
				state_province = models.CharField(max_length=30)
				country = models.CharField(max_length=50)
				website = models.URLField()

				def __unicode__(self):
					return self.name

				class Meta:
					ordering = ['name']

		If you specify this, it tells Django that unless an ordering is given explicitly with order_by(), all Publisher objects should be ordered by the name field whenever they¡¯re retrieved with the Django database API.

		Chaining Lookups

			>>> Publisher.objects.filter(country="U.S.A.").order_by("-name")
			[<Publisher: O'Reilly>, <Publisher: Apress>]
			>>> Publisher.objects.order_by("-name").filter(country="U.S.A.")
			[<Publisher: O'Reilly>, <Publisher: Apress>]

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			WHERE country = 'U.S.A'
			ORDER BY name DESC;

		Slicing Data

			>>> Publisher.objects.order_by('name')[0]
			<Publisher: Apress>

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			ORDER BY name
			LIMIT 1;

			>>> Publisher.objects.order_by('name')[0:2]

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			ORDER BY name
			OFFSET 0 LIMIT 2;

			Note that negative slicing is not supported:

			>>> Publisher.objects.order_by('name')[-1]
			Traceback (most recent call last):
			  ...
			AssertionError: Negative indexing is not supported.

			This is easy to get around, though. Just change the order_by() statement, like this:

			>>> Publisher.objects.order_by('-name')[0]

		Updating Multiple Objects in One Statement

			>>> p = Publisher.objects.get(name='Apress')
			>>> p.name = 'Apress Publishing'
			>>> p.save()

			SELECT id, name, address, city, state_province, country, website
			FROM books_publisher
			WHERE name = 'Apress';

			UPDATE books_publisher SET
				name = 'Apress Publishing',
				address = '2855 Telegraph Ave.',
				city = 'Berkeley',
				state_province = 'CA',
				country = 'U.S.A.',
				website = 'http://www.apress.com'
			WHERE id = 52;

			(Note that this example assumes Apress has a publisher ID of 52.)

			>>> Publisher.objects.filter(id=52).update(name='Apress Publishing')

			UPDATE books_publisher
			SET name = 'Apress Publishing'
			WHERE id = 52;

			>>> Publisher.objects.all().update(country='USA')
			2

			The update() method has a return value ¨C an integer representing how many records changed. In the above example, we got 2.

		Deleting Objects

			>>> p = Publisher.objects.get(name="O'Reilly")
			>>> p.delete()
			>>> Publisher.objects.all()
			[<Publisher: Apress Publishing>]

			>>> Publisher.objects.filter(country='USA').delete()
			>>> Publisher.objects.all().delete()
			>>> Publisher.objects.all()
			[]

			>>> Publisher.objects.filter(country='USA').delete()

1. The Django Admin Site

	1.	Admin
		
			$ python manage.py syncdb
				amdin / admin
				If choose not create admin during syncdb, shouldrun: python manage.py createsuperuser
	
		http://localhost:8080/admin/

	1.	



		
