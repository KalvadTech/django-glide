"""
Tests related to the template tags
"""

from django.test import TestCase, override_settings
from django.template import Context, Template
from django_glide.config import Config
from django_glide.templatetags.glide_tags import (
    glide_assets,
    normalize_value,
    prepare_options,
)


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

    def test_normalize_bool(self):
        expected_value = True
        self.assertEqual(normalize_value("true"), expected_value)

        expected_value = False
        self.assertEqual(normalize_value("false"), expected_value)

    def test_normalize_str(self):
        expected_value = "test"
        self.assertEqual(normalize_value("test"), expected_value)

        expected_value = None
        self.assertEqual(normalize_value("null"), expected_value)

        expected_value = None
        self.assertEqual(normalize_value("none"), expected_value)

    def test_normalize_float(self):
        expected_value = 3.5
        self.assertEqual(normalize_value(3.5), expected_value)
        self.assertEqual(normalize_value("3.5"), expected_value)

    def test_normalize_int(self):
        expected_value = 3
        self.assertEqual(normalize_value(3), expected_value)
        self.assertEqual(normalize_value("3"), expected_value)

    def test_normalize_json(self):
        expected_value = '{1024: {"perView": 4}}'
        self.assertEqual(normalize_value(expected_value), expected_value)

    def test_prepare_options(self):
        options = {"perView": 4, "breakpoints": '{"1024": {"perView": 4}}'}
        expected_value = {"perView": 4, "breakpoints": {"1024": {"perView": 4}}}

        self.assertEqual(prepare_options(**options), expected_value)

    def test_prepare_options_invalid_json(self):
        options = {"perView": 4, "breakpoints": '{1024: {"perView": 4}}'}
        self.assertRaises(ValueError, prepare_options, **options)
