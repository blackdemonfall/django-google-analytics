# django-google-analytics
=====
Django Google Analytics Plugin
=====

Django Google Analytics Plugin is a django app who add the javascript ot activate the tarcker of  google analytics in the template with template tags.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add google_analytics to you INSTALLED_APPS settings like this:

	INSTALED_APPS = [
		...
		'google_analytics',
	]

2. Add to setings.py the Goole key for Analytics like this:
	
	GOOGLE_ANALYTICS_CODE = 'xxx-xxxxxx-xx'

3. Call the template tag to initiate the code {% load google_analytics %}

3. Add the {% googleanalytics %} into the base template to add the code
