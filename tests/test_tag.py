"""
Tests related to the template tags
"""

from django.test import TestCase, override_settings
from django.template import Context, Template
from django_glide.config import Config
from django_glide.templatetags.glide_tags import glide_assets


class TemplateTagsTests(TestCase):
    """
    Test case for the template tags
    """

    def test_js_url(self):
        config = Config()
        expected_data = {
            "js_url": config.js_url,
            "css_core_url": config.css_core_url,
            "css_theme_url": config.css_theme_url,
        }

        self.assertEqual(glide_assets(), expected_data)
