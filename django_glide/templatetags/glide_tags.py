import json
from django import template
from django.template.context import Context
from django.template.loader import get_template
from typing import Dict, List, Any
from django_glide.config import Config

register = template.Library()


def prepare_options(**options: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check for the presence of the breakpoints field to parse it properly. Will throw an exception if invalid.
    """
    for key, value in options.items():
        if key == "breakpoints":
            try:
                options[key] = json.loads(str(value))
            except json.JSONDecodeError:
                raise ValueError("breakpoints must be valid JSON")
        else:
            options[key] = value

    return options


@register.simple_tag(takes_context=True)
def glide_carousel(
    context: Context,
    items: List[Any],
    carousel_id: str = "glide1",
    carousel_template: str | None = None,
    slide_template: str | None = None,
    **options: Dict[str, Any],
) -> str:
    """
    Render a Glide.js carousel.
    """
    config = Config()

    carousel_template_name = carousel_template or config.default_carousel_template
    slide_template_name = slide_template or config.default_slide_template

    carousel_template = get_template(carousel_template_name)

    ctx = {
        **context.flatten(),
        "items": items,
        "carousel_id": carousel_id,
        "options": prepare_options(**options),
        "slide_template": slide_template_name,
    }

    return carousel_template.render(ctx)


@register.inclusion_tag("assets.html")
def glide_assets() -> Dict[str, Any]:
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
