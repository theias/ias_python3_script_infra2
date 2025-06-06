#!/usr/bin/python3
"""An example application for using IASInfra

This will call a library based application.

This is a description of your project.

"""
__author__ = "Your Name <your-email@example.com"
__credits__ = """
Infrastructure Design: Martin VanWinkle, Institute for Advanced Study
"""

import os
import sys

sys.path.append('/opt/IAS/lib/python3')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../lib/python3'))) # pylint: disable=line-too-long

# pylint: disable=wrong-import-position
from ias.infra2.sampleApplication.sampleApplication import IASSampleApplication

APP = IASSampleApplication()
# Set the environment variable, IASInfra_log_to_stderr, to something non-zero
# to enable debugging to stderr.
# Example:  export IASInfra_log_to_stderr=1
APP.run()
