============
Installation
============

Installing django-active
~~~~~~~~~~~~~~~~~~~~~~~

#. Install using pip::

    pip install git+https://github.com/bbrik/django-active.git

#. Add ``active`` to your ``INSTALLED_APPS`` in settings.py:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'active',
    )

#. Add ``django.core.context_processors.request`` to ``TEMPLATE_CONTEXT_PROCESSORS`` in
settings.py:

.. code-block:: python

    from django.conf import global_settings as DEFAULT_SETTINGS

    TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    )


active_url and active_url_start
*******************************

Used to style a link as active based on the current request's path.
The syntax is the similar as django's ``url`` tag.

Considering this ``urls.py``:

.. code-block:: python

    ...
    url(
       regex=r'^weekdays/$',
       view='weekday_list_view',
       name='weekday_list'
    ),
    url(
       regex=r'^weekdays/(?P<slug>[\w_-]+)/$',
       view=weekday_detail_view,
       name='weekday_detail'
    ),


To match only the start of the url:

.. code-block:: python

    ...
    <li class="{% active_url_start 'weekday_list' %}">
      <a href="{% url 'weekday_list %}">
        Weekdays
      </a>
    </li>

To match an exact url:

.. code-block:: python

    <li class="{% active_url 'weekday_detail' slug=weekday.slug %}">
      <a href="{% url 'weekday_detail' slug=weekday.slug %}">
        {{ weekdays.name}}
      </a>
    </li>

active_query and replace_in_query
*********************************

``active_query`` is used to style a link as active based on the request's GET.

``replace_in_query`` returns the current request's GET as url encoded, replacing
only specified arguments, keeping all other query parameters unchanged.

Those are useful for links that filter a query::

    <li class="{% active_query fruit='' %}">
      <a href="?{% replace_in_query fruit='' %}">
        All fruits
      </a>
    </li>
    <li class="{% active_query fruit='apple' %}">
      <a href="?{% replace_in_query fruit='apple' %}">
        Apple
      </a>
    </li>
    <li class="{% active_query fruit='orange' %}">
      <a href="?{% replace_in_query fruit='orange' %}">
        Orange
      </a>
    </li>

For example, the above code will render this html if the current url is ``/?fruit=apple&q=test``::

    <li class="">
      <a href="?fruit=&q=test">
        All fruits
      </a>
    </li>
    <li class="active">
      <a href="?fruit=apple&q=test">
        Apple
      </a>
    </li>
    <li class="">
      <a href="?fruit=orante&q=test">
        Orange
      </a>
    </li>

So, you get each link pointing to its query filter,
both keeping the other parameter ``q`` intact.