"""
Tests related to the template tags
"""

from unittest.mock import patch

from django.test import TestCase, override_settings
from django.template import Context, Template
from django_glide.config import Config
from django_glide.templatetags.glide_tags import (
    glide_assets,
    glide_carousel,
    get_carousel_template,
    get_slide_template,
    normalize_value,
    prepare_options,
)


class TemplateTagsTests(TestCase):
    """
    Test case for the template tags
    """

    def test_default_assets(self):
        config = Config()
        expected_data = {
            "js_url": config.glide_js_url,
            "css_core_url": config.glide_css_core_url,
            "css_theme_url": config.glide_css_theme_url,
        }

        self.assertEqual(glide_assets(), expected_data)

    @override_settings(DG_ENGINE="glide")
    def test_glide_assets(self):
        config = Config()
        expected_data = {
            "js_url": config.glide_js_url,
            "css_core_url": config.glide_css_core_url,
            "css_theme_url": config.glide_css_theme_url,
        }

        self.assertEqual(glide_assets(), expected_data)

    @override_settings(DG_ENGINE="swiper")
    def test_swiper_assets(self):
        config = Config()
        expected_data = {
            "js_url": config.swiper_js_url,
            "css_core_url": config.swiper_css_url,
            "css_theme_url": None,
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

    def test_prepare_options_breakpoints(self):
        options = {"perView": 4, "breakpoints": '{"1024": {"perView": 4}}'}
        expected_value = {"perView": 4, "breakpoints": {"1024": {"perView": 4}}}

        self.assertEqual(prepare_options(**options), expected_value)

    def test_prepare_options_peek(self):
        options = {"perView": 4, "peek": '{"before": 100, "after": 50}'}
        expected_value = {"perView": 4, "peek": {"before": 100, "after": 50}}

        self.assertEqual(prepare_options(**options), expected_value)

    def test_prepare_options_classes(self):
        options = {"perView": 4, "classes": '{"slider": "glide--slider"}'}
        expected_value = {"perView": 4, "classes": {"slider": "glide--slider"}}

        self.assertEqual(prepare_options(**options), expected_value)

    def test_prepare_options_invalid_json(self):
        options = {"perView": 4, "classes": '{"slider": "glide--slider'}
        expected_value = {"perView": 4, "classes": '{"slider": "glide--slider'}

        self.assertEqual(prepare_options(**options), expected_value)

    def test_get_carousel_template_custom(self):
        config = Config()
        result = get_carousel_template(config, "custom/carousel.html")
        self.assertEqual(result, "custom/carousel.html")

    def test_get_carousel_template_default_config(self):
        with override_settings(DG_DEFAULT_CAROUSEL_TEMPLATE="custom/carousel2.html"):
            config = Config()
            result = get_carousel_template(config)
            self.assertEqual(result, "custom/carousel2.html")

    def test_get_carousel_template_default_engine(self):
        config = Config()
        result = get_carousel_template(config)
        self.assertEqual(result, f"{config.engine}/carousel.html")

    def test_get_slide_template_custom(self):
        config = Config()
        result = get_slide_template(config, "custom/slide.html")
        self.assertEqual(result, "custom/slide.html")

    def test_get_slide_template_default_config(self):
        with override_settings(DG_DEFAULT_SLIDE_TEMPLATE="custom/slide2.html"):
            config = Config()
            result = get_slide_template(config)
            self.assertEqual(result, "custom/slide2.html")

    def test_get_slide_template_default_engine(self):
        config = Config()
        result = get_slide_template(config)
        self.assertEqual(result, f"{config.engine}/slide.html")

    @patch("django_glide.templatetags.glide_tags.get_template")
    def test_glide_carousel(self, mock_get_template):
        mock_template = mock_get_template.return_value
        mock_template.render.return_value = '<div class="glide-carousel">rendered</div>'

        items = ["item1", "item2"]
        result = glide_carousel(Context(), items)

        mock_get_template.assert_called_once()
        self.assertIn("glide-carousel", result)
