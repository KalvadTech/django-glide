"""
Tests related to the Config
"""

from django.test import TestCase, override_settings
from django_glide.config import Config


class ConfigTests(TestCase):
    """
    Test case for Config
    """

    def setUp(self):
        self.config = Config()

    def test_engine(self):
        engine = self.config.engine
        self.assertEqual(engine, "glide")

    @override_settings(DG_ENGINE="swiper")
    def test_custom_engine(self):
        engine = self.config.engine
        self.assertEqual(engine, "swiper")

    @override_settings(DG_GLIDE_JS_URL="my-js-url")
    def test_custom_glide_js_url(self):
        js_url = self.config.glide_js_url
        self.assertEqual(js_url, "my-js-url")

    def test_glide_js_url(self):
        js_url = self.config.glide_js_url
        self.assertEqual(
            js_url, "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/glide.min.js"
        )

    @override_settings(DG_GLIDE_JS_URL="my-js-url")
    def test_custom_glide_js_url(self):
        js_url = self.config.glide_js_url
        self.assertEqual(js_url, "my-js-url")

    def test_glide_css_core_url(self):
        css_url = self.config.glide_css_core_url
        self.assertEqual(
            css_url,
            "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.core.min.css",
        )

    @override_settings(DG_GLIDE_CSS_CORE_URL="my-css-url")
    def test_custom_glide_css_core_url(self):
        css_url = self.config.glide_css_core_url
        self.assertEqual(css_url, "my-css-url")

    def test_glide_css_theme_url(self):
        css_url = self.config.glide_css_theme_url
        self.assertEqual(
            css_url,
            "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.theme.min.css",
        )

    @override_settings(DG_GLIDE_CSS_THEME_URL="my-css-url")
    def test_custom_glide_css_core_url(self):
        css_url = self.config.glide_css_theme_url
        self.assertEqual(css_url, "my-css-url")

    @override_settings(DG_GLIDE_CSS_THEME_URL=None)
    def test_none_glide_css_core_url(self):
        css_url = self.config.glide_css_theme_url
        self.assertEqual(css_url, None)

    def test_swiper_js_url(self):
        js_url = self.config.swiper_js_url
        self.assertEqual(
            js_url, "https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.js"
        )

    @override_settings(DG_SWIPER_JS_URL="my-js-url")
    def test_custom_swiper_js_url(self):
        js_url = self.config.swiper_js_url
        self.assertEqual(js_url, "my-js-url")

    def test_swiper_css_url(self):
        css_url = self.config.swiper_css_url
        self.assertEqual(
            css_url,
            "https://cdn.jsdelivr.net/npm/swiper/swiper-bundle.min.css",
        )

    @override_settings(DG_SWIPER_CSS_URL="my-css-url")
    def test_custom_glide_css_core_url(self):
        css_url = self.config.swiper_css_url
        self.assertEqual(css_url, "my-css-url")

    def test_default_carousel_template(self):
        template = self.config.default_carousel_template
        self.assertEqual(
            template,
            None,
        )

    @override_settings(DG_DEFAULT_CAROUSEL_TEMPLATE="test.html")
    def test_custom_default_template(self):
        template = self.config.default_carousel_template
        self.assertEqual(template, "test.html")

    def test_default_slide_template(self):
        template = self.config.default_slide_template
        self.assertEqual(
            template,
            None,
        )

    @override_settings(DG_DEFAULT_SLIDE_TEMPLATE="test.html")
    def test_custom_default_template(self):
        template = self.config.default_slide_template
        self.assertEqual(template, "test.html")
