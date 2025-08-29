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

    def test_js_url(self):
        js_url = self.config.js_url
        self.assertEqual(
            js_url, "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/glide.min.js"
        )

    @override_settings(GLIDE_JS_URL="my-js-url")
    def test_custom_js_url(self):
        js_url = self.config.js_url
        self.assertEqual(js_url, "my-js-url")

    def test_css_core_url(self):
        css_url = self.config.css_core_url
        self.assertEqual(
            css_url,
            "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.core.min.css",
        )

    @override_settings(GLIDE_CSS_CORE_URL="my-css-url")
    def test_custom_css_core_url(self):
        css_url = self.config.css_core_url
        self.assertEqual(css_url, "my-css-url")

    def test_css_theme_url(self):
        css_url = self.config.css_theme_url
        self.assertEqual(
            css_url,
            "https://cdn.jsdelivr.net/npm/@glidejs/glide/dist/css/glide.theme.min.css",
        )

    @override_settings(GLIDE_CSS_THEME_URL="my-css-url")
    def test_custom_css_core_url(self):
        css_url = self.config.css_theme_url
        self.assertEqual(css_url, "my-css-url")

    def test_default_template(self):
        template = self.config.default_template
        self.assertEqual(
            template,
            "template.html",
        )

    @override_settings(GLIDE_DEFAULT_TEMPLATE="test.html")
    def test_custom_default_template(self):
        template = self.config.default_template
        self.assertEqual(template, "test.html")
