# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import aptean.city


class ApteanCityLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=aptean.city)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'aptean.city:default')


APTEAN_CITY_FIXTURE = ApteanCityLayer()


APTEAN_CITY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(APTEAN_CITY_FIXTURE,),
    name='ApteanCityLayer:IntegrationTesting'
)


APTEAN_CITY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(APTEAN_CITY_FIXTURE,),
    name='ApteanCityLayer:FunctionalTesting'
)


APTEAN_CITY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        APTEAN_CITY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ApteanCityLayer:AcceptanceTesting'
)
