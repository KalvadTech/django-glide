# django-glide

A Django library that provides a simple and flexible way to render JavaScript carousels in Django templates.
It supports multiple carousel engines (currently Glide.js and Swiper) and allows full template overriding.

The library handles:
 * Loading engine-specific JS and CSS assets
 * Rendering carousels directly from Django templates
 * Template override priority per carousel, per engine, or globally
 * Optional slide templates
 * Automatic normalization of options passed from Django to JavaScript

This makes it easy to add carousels to a Django project without manually wiring JS code.

It works with the following Django versions:

 * Django 3
 * Django 4
 * Django 5

## Installation

```sh
pip install django-glide
```

Then, add the app to your list of `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    "django_glide",
]
```

By default glide JS is used, but the library can be configured to use the engine of your choice by setting the following:

```python
DG_ENGINE = "swiper" # or "glide"
```

## Usage

Then either in your base template (to load on all pages) or just in the template you need, add:

```html
{% load glide_tags %}

{% glide_assets %}
```

Then to actually use a glide based carousel, use this in your template:

```html
{% load glide_tags %}

...

{% glide_carousel my_images carousel_id="hero" type="carousel" perView=3 autoplay=3000 %}
```

All the options listed on the example above can be found here for Glide JS: https://glidejs.com/docs/options/ or here for Swiper: https://github.com/nolimits4web/swiper/tree/master/demos.
Note that all options are using basic types such as integer, boolean, float or string, at the exception of the `breakpoints`, `peek` and `classes` fields which are a complex object. Here is an example on how you can use it:

```html
{% glide_carousel events carousel_id="events" type="carousel" perView=3.5 breakpoints='{"600": {"perView": 2.5}}' %}
```

And then in your view, return an object in the context following this format:

```python
my_images = [
    {"image": "/static/img/slide1.jpg", "alt": "Slide 1"},
    {"image": "/static/img/slide2.jpg", "alt": "Slide 2"},
    {"image": "/static/img/slide3.jpg", "alt": "Slide 3"},
]
```

## Using custom template

By default, the template shipped with the library is basic, it can either load an image or some text.

This library uses 2 templates per engine, one for the carousel itself and one for each individual slides.

### Slide template

You can set a global slide template by creating an HTML jinja file and referencing it in your settings like so:

```python
DG_DEFAULT_SLIDE_TEMPLATE = "myapp/slide.html"
```

Or you can set a slide template for a given carousel like so:


```html
{% glide_carousel my_custom_data carousel_id="hero" slide_template="myapp/slide.html" type="carousel" perView=3 autoplay=3000 %}
```

### Carousel template

You can set a global carousel template by creating an HTML jinja file and referencing it in your settings like so:

```python
DG_DEFAULT_CAROUSEL_TEMPLATE = "myapp/carousel.html"
```

Or you can set a carousel template for a given carousel like so:


```html
{% glide_carousel my_custom_data carousel_id="hero" carousel_template="myapp/carousel.html" type="carousel" perView=3 autoplay=3000 %}
```

## Glide JS specifics

### Arrows

You can use the [arrows control](https://glidejs.com/docs/setup#arrows) either by:

 * Passing `arrows="true"`
 * Passing `arrows_template="xxx"`

### Bullets

You can use the [bullets control](https://glidejs.com/docs/setup#bullets) either by:

 * Passing `bullets="true"`
 * Passing `bullets_template="xxx"`

### Changing the way GlideJS is loaded

By default, this library uses lastest Glide of the jsdelivr CDN, if you want to change this, you can modify one (or all) of the following settings:

```python
DG_GLIDE_JS_URL = "my new URL to fetch the JS"
DG_GLIDE_CSS_CORE_URL = "my new URL to fetch the core CSS"
DG_GLIDE_CSS_THEME_URL = "my new URL to fetch the theme CSS, if you set as None, it won't be loaded"
```

## Swiper specifics

### Changing the way Swiper is loaded

By default, this library uses lastest Swiper of the jsdelivr CDN, if you want to change this, you can modify one (or all) of the following settings:

```python
DG_SWIPER_JS_URL = "my new URL to fetch the JS"
DG_SWIPER_CSS_URL = "my new URL to fetch the CSS"
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
