# Copyright (c) 2019 The Unit-e developers
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

from code_parser import CodeParser
from renderer_rst import RendererRST
from doc_tester import DocTester


class CliController:
    """This class contains the logic of the command line commands."""
    def generate(self, source_dir, show_data_types=False):
        parser = CodeParser(source_dir)
        messages = parser.parse()
        renderer = RendererRST()
        renderer.render(messages, show_data_types=show_data_types)

    def test(self, source_dir, update_expected_results=False, object_name=None):
        tester = DocTester(source_dir)
        tester.test(update_expected_results, object_name)
