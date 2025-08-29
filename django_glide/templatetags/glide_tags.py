from django import template
from django.template.loader import get_template
from django_glide.config import Config

register = template.Library()


@register.simple_tag(takes_context=True)
def glide_carousel(context, items, carousel_id="glide1", template_name=None, **options):
    """
    Render a Glide.js carousel.
    """
    config = Config()
    template_name = template_name or config.default_template
    template = get_template(template_name)

    ctx = {
        **context.flatten(),
        "items": items,
        "carousel_id": carousel_id,
        "options": options,
    }

    return template.render(ctx)


@register.inclusion_tag("assets.html")
def glide_assets():
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
