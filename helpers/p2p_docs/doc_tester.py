import string
from pathlib import Path
import sys
import importlib

from doc_parser import DocParser

class DocTester:
    def __init__(self, source_dir):
        sys.path.append(source_dir + "/test/functional")
        self.message_classes = __import__("test_framework.messages").messages

    def test_example(self, path, object_name):
        name = path.name[:-4]
        if name == "intro":
            return None
        parser = DocParser()
        with path.open() as file:
            doc_data = parser.parse(file.read())
        example = self.extract_example(doc_data)
        if not example:
            return None
        if object_name and name != object_name:
            return None
        return self.test_object(name, example)

    def test(self, update_expected_results=False, object_name=None):
        testresults = []
        for path in sorted(Path("doc_data").glob("*.txt")):
            result = self.test_example(path, object_name)
            if result:
                testresults.append(result)
        for path in sorted(Path("doc_data/types").glob("*.txt")):
            result = self.test_example(path, object_name)
            if result:
                testresults.append(result)
        if object_name:
            print(testresults[0])
        else:
            expected_file = Path("test_examples.expected")
            if update_expected_results:
                with expected_file.open("w") as file:
                    file.write("\n".join(testresults))
            else:
                count_all = 0
                count_fail = 0
                with expected_file.open() as file:
                    for i, line in enumerate(file.read().splitlines()):
                        count_all += 1
                        if testresults[i] != line:
                            count_fail += 1
                            print("Failed:")
                            print("  Expected:", line)
                            print("  Received:", testresults[i])
                if i + 1 < len(testresults):
                    for j in range(i + 1, len(testresults)):
                        print("Unexpceted test:")
                        print("  ", testresults[j])
                        count_all += 1
                        count_fail += 1
                print("%s of %s examples successfully tested" % (count_all - count_fail, count_all))

    def test_object(self, object_name, example):
        testresult = object_name + ": "
        object_class = "msg_" + object_name
        if not hasattr(self.message_classes, object_class):
            object_class = "C" + object_name
        if hasattr(self.message_classes, object_class):
            msg = getattr(self.message_classes, object_class)()
            try:
                self.message_classes.FromHex(msg, self.example_to_hex(example))
                testresult += "PASS: " + str(msg)
            except Exception as error:
                testresult += "FAIL: " + str(error)
        else:
            testresult += "SKIP: No test class for object '%s'" % object_name
        return testresult

    def example_to_hex(self, example_str):
        i = 0
        result = ""
        while(i < len(example_str)):
            c = example_str[i]
            if c in string.hexdigits:
                result += c
            elif c == " " or c == "|":
                pass
            else:
                i = example_str.find("\n", i)
                if i < 0:
                    break
            i += 1
        return result

    def extract_example(self, doc_data):
        for section in doc_data:
            if section["type"] == "example":
                return section["data"]
        return None
