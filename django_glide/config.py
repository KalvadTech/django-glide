"""
Contains the config for the library
"""

from django.conf import settings


class Config:
    """
    Configuration taken from Django's settings
    """

    @property
    def js_url(self) -> str:
        """
        Returns the URL to load glide javascript
        """
        return (
            settings.GLIDE_JS_URL
            if hasattr(settings, "GLIDE_JS_URL")
            else "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/glide.min.js"
        )

    @property
    def css_core_url(self) -> str:
        """
        Returns the URL to load glide core CSS
        """
        return (
            settings.GLIDE_CSS_CORE_URL
            if hasattr(settings, "GLIDE_CSS_CORE_URL")
            else "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.core.min.css"
        )

    @property
    def css_theme_url(self) -> str:
        """
        Returns the URL to load glide theme CSS
        """
        return (
            settings.GLIDE_CSS_THEME_URL
            if hasattr(settings, "GLIDE_CSS_THEME_URL")
            else "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.theme.min.css"
        )

    @property
    def default_template(self) -> str:
        """
        Returns the default slide template
        """
        return (
            settings.GLIDE_DEFAULT_TEMPLATE
            if hasattr(settings, "GLIDE_DEFAULT_TEMPLATE")
            else "template.html"
        )
