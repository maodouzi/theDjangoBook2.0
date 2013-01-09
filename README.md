theDjangoBook2.0
================

# Ref

	git://github.com/jacobian/djangobook.com.git
	git://github.com/maodouzi/theDjangoBook2.0.git

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

		Filter:

			{{ ship_date|date:"F j, Y" }}

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

		silent_variable_failure=True make render empty string scliently if couldn't find attribute

		By default, if a variable doesn¡¯t exist, the template system renders it as an empty string, failing silently

			>>> from django.template import Template, Context
			>>> t = Template('Your name is {{ name }}.')
			>>> t.render(Context())
			u'Your name is .'

		alters_data=True make any function who wanting to modify rendering object be disabled

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

	1.	Filter
