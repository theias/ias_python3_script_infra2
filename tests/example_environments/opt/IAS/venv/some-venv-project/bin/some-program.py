#!/usr/bin/python3

import sys
import os
import pprint

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '../../../../../../../src/lib/python3'))) # pylint: disable=line-too-long

# pprint.pprint(sys.path)

from ias.infra2.infra2 import IASInfra2

class IASVenvApplication(IASInfra2):
    """ This app does something. """
    def setup(self):
        """ This is where you setup. """
        self.log_info("Setting up.")

    def tear_down(self):
        """ This is where you tear down. """
        self.log_info("Tearing down.")

    def main(self):
        """ This is where the work gets done """
        self.log_info("In main.")

        # Use this to see what variables are available.
        # Currently, inconsistent and was used for testing.
        self.log_debug_variables()

        generic_output_file = self.get_generic_output_file_name('extract', 'txt')
        self.log_info(
            "Generic output file: "
            + generic_output_file
        )

        text_file = open(generic_output_file, "w")
        text_file.write("Here is an extract.\n")
        text_file.close # pylint: disable=pointless-statement



if __name__ == '__main__':
    APP = IASVenvApplication()
    # Set the environment variable, IASInfra_log_to_stderr, to something non-zero
    # to enable debugging to stderr.
    # Example:  export IASInfra_log_to_stderr=1
    APP.run()
