# coding: utf-8

"""
    Velocity-Sandbox

    API to create a Velocity Sandbox

    OpenAPI spec version: 1.0.0
    Contact: alay.vakil@veritas.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.sandbox import Sandbox


class TestSandbox(unittest.TestCase):
    """ Sandbox unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSandbox(self):
        """
        Test Sandbox
        """
        model = swagger_client.models.sandbox.Sandbox()


if __name__ == '__main__':
    unittest.main()
