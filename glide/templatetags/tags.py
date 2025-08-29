from django import template

register = template.Library()

@register.inclusion_tag("template.html")
def glide_carousel(items, glide_id="glide1", **options):
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
