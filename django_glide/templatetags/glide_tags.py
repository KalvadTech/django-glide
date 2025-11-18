import json
from django import template
from django.template.context import Context
from django.template.loader import get_template
from typing import Dict, List, Any
from django_glide.config import Config

register = template.Library()


def normalize_value(value: Any) -> Any:
    """
    Convert string template args into proper Python types.
    Not the best code, but it will do the trick.
    """
    if isinstance(value, str):
        val = value.strip().lower()
        if val == "true":
            return True
        if val == "false":
            return False
        if val == "null" or val == "none":
            return None
        # try to parse numbers
        try:
            if "." in val:
                return float(val)
            return int(val)
        except ValueError:
            return value  # fallback: leave as string
    return value


def prepare_options(**options: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check for the presence of the breakpoints field to parse it properly. Will throw an exception if invalid.
    """
    for key, value in options.items():
        if key in ("breakpoints", "peek", "classes"):
            try:
                options[key] = json.loads(str(value))
            except (TypeError, json.JSONDecodeError):
                options[key] = normalize_value(value)
        else:
            options[key] = normalize_value(value)

    return options


def get_carousel_template(config: Config, carousel_template: str | None = None) -> str:
    """
    Loads the right carousel template based on an order of priority as follow:
    template param > config default carousel > engine default carousel
    """
    if carousel_template is not None:
        return carousel_template

    if config.default_carousel_template is not None:
        return config.default_carousel_template

    return f"{config.engine}/carousel.html"


def get_slide_template(config: Config, slide_template: str | None = None) -> str:
    """
    Loads the right slide template based on an order of priority as follow:
    template param > config default slide > engine default slide
    """
    if slide_template is not None:
        return slide_template

    if config.default_slide_template:
        return config.default_slide_template

    return f"{config.engine}/slide.html"


@register.simple_tag(takes_context=True)
def glide_carousel(
    context: Context,
    items: List[Any],
    carousel_id: str = "glide1",
    carousel_template: str | None = None,
    slide_template: str | None = None,
    arrows: bool = False,
    arrows_template: str | None = None,
    bullets: bool = False,
    bullets_template: str | None = None,
    **options: Dict[str, Any],
) -> str:
    """
    Render a carousel.
    """
    config = Config()

    carousel_template_name = get_carousel_template(config, carousel_template)
    slide_template_name = get_slide_template(config, slide_template)

    carousel_template = get_template(carousel_template_name)

    ctx = {
        **context.flatten(),
        "items": items,
        "carousel_id": carousel_id,
        "options": json.dumps(prepare_options(**options)),
        "arrows": normalize_value(arrows),
        "arrows_template": arrows_template,
        "bullets": normalize_value(bullets),
        "bullets_template": bullets_template,
        "slide_template": slide_template_name,
    }

    return carousel_template.render(ctx)


@register.inclusion_tag("assets.html")
def glide_assets() -> Dict[str, Any]:
    """
    Render carousel assets (CSS + JS) based on the selected engine
    Should be called once, usually in the <head> or before </body>.
    """
    config = Config()

    if config.engine == "glide":
        return {
            "js_url": config.glide_js_url,
            "css_core_url": config.glide_css_core_url,
            "css_theme_url": config.glide_css_theme_url,
        }

    return {
        "js_url": config.swiper_js_url,
        "css_core_url": config.swiper_css_url,
        "css_theme_url": None,
    }
