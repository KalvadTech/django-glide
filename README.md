# django-glide

This is a Django library to add support to Glide JS in your templates

It supports:

 * Django 3
 * Django 4
 * Django 5

## Installation

```sh
pip install django-glide
```

## Setup

Add "django_glide" to your list of `INSTALLED_APPS`, then either in your base template (to load on all pages) or just the template you need, add:

```html
{% load glide_tags %}
{% glide_assets %}
```

Then to actually use a glide based carousel, use this in your template:

```html
{% load glide_tags %}

...

{% glide_carousel items=my_images carousel_id="hero" type="carousel" perView=3 autoplay=3000 %}
```

And then in your view, return an object in the context following this format:

```python
my_images = [
    {"image": "/static/img/slide1.jpg", "alt": "Slide 1"},
    {"image": "/static/img/slide2.jpg", "alt": "Slide 2"},
    {"image": "/static/img/slide3.jpg", "alt": "Slide 3"},
]
```

By default, this library uses lastest Glide of the jsdelivr CDN, if you want to change this, you can modify one (or all) of the following settings:

```python
GLIDE_JS_URL = "my new URL to fetch the JS"
GLIDE_CSS_CORE_URL = "my new URL to fetch the core CSS"
GLIDE_CSS_THEME_URL = "my new URL to fetch the theme CSS"
```

## Development

Installing for development:

```sh
make install
```

Cleaning the installation:

```sh
make clean
```

Format the code:

```sh
make format
```

Check the code (for linting errors):

```sh
make check
```

Check the code (python type checker):

```sh
make static-check
```

Running all tests:

```sh
make test
```

Create a sdist+bdist package in dist/:

```sh
make package
```
