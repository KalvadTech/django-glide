"""
Contains the config for the library
"""

from django.conf import settings


class Config:
    """
    Configuration taken from Django's settings
    """

    @property
    def engine(self) -> str:
        """
        Returns the carousel engine to load
        """
        return settings.DG_ENGINE if hasattr(settings, "DG_ENGINE") else "glide"

    @property
    def glide_js_url(self) -> str:
        """
        Returns the URL to load glide javascript
        """
        return (
            settings.DG_GLIDE_JS_URL
            if hasattr(settings, "DG_GLIDE_JS_URL")
            else "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/glide.min.js"
        )

    @property
    def glide_css_core_url(self) -> str:
        """
        Returns the URL to load glide core CSS
        """
        return (
            settings.DG_GLIDE_CSS_CORE_URL
            if hasattr(settings, "DG_GLIDE_CSS_CORE_URL")
            else "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.core.min.css"
        )

    @property
    def glide_css_theme_url(self) -> str | None:
        """
        Returns the URL to load glide theme CSS
        It can be None as the theme is optional
        """
        return (
            settings.DG_GLIDE_CSS_THEME_URL
            if hasattr(settings, "DG_GLIDE_CSS_THEME_URL")
            else "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.theme.min.css"
        )

    @property
    def swiper_js_url(self) -> str:
        """
        Returns the URL to load swiper javascript
        """
        return (
            settings.DG_SWIPER_JS_URL
            if hasattr(settings, "DG_SWIPER_JS_URL")
            else "https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"
        )

    @property
    def swiper_css_url(self) -> str:
        """
        Returns the URL to load swiper CSS
        """
        return (
            settings.DG_SWIPER_CSS_URL
            if hasattr(settings, "DG_SWIPER_CSS_URL")
            else "https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.css"
        )

    @property
    def default_carousel_template(self) -> str | None:
        """
        Returns the default carousel template
        """
        return (
            settings.DG_DEFAULT_CAROUSEL_TEMPLATE
            if hasattr(settings, "DG_DEFAULT_CAROUSEL_TEMPLATE")
            else None
        )

    @property
    def default_slide_template(self) -> str | None:
        """
        Returns the default slide template
        """
        return (
            settings.DG_DEFAULT_SLIDE_TEMPLATE
            if hasattr(settings, "DG_DEFAULT_SLIDE_TEMPLATE")
            else None
        )
