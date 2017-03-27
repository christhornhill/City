# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from aptean.city.testing import APTEAN_CITY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that aptean.city is properly installed."""

    layer = APTEAN_CITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if aptean.city is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'aptean.city'))

    def test_browserlayer(self):
        """Test that IApteanCityLayer is registered."""
        from aptean.city.interfaces import (
            IApteanCityLayer)
        from plone.browserlayer import utils
        self.assertIn(IApteanCityLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = APTEAN_CITY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['aptean.city'])

    def test_product_uninstalled(self):
        """Test if aptean.city is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'aptean.city'))

    def test_browserlayer_removed(self):
        """Test that IApteanCityLayer is removed."""
        from aptean.city.interfaces import \
            IApteanCityLayer
        from plone.browserlayer import utils
        self.assertNotIn(IApteanCityLayer, utils.registered_layers())
