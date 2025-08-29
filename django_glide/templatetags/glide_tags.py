from django import template
from django_glide.config import Config

register = template.Library()


@register.inclusion_tag("template.html")
def glide_carousel(items, carousel_id="glide1", **options):
    """
    Render a Glide.js carousel.

    Args:
        items (list): list of dicts or strings to display as slides
        carousel_id (str): unique id for this carousel instance
        options (dict): extra options passed to JS init
    """
    return {
        "items": items,
        "carousel_id": carousel_id,
        "options": options,
    }


@register.inclusion_tag("assets.html", takes_context=True)
def glide_assets(context):
    """
    Render Glide.js assets (CSS + JS).
    Should be called once, usually in the <head> or before </body>.
    """
    config = Config()
    return {
        "js_url": config.js_url,
        "css_core_url": config.css_core_url,
        "css_theme_url": config.css_theme_url,
    }
