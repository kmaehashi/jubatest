# -*- coding: utf-8 -*-

from xml.dom.minidom import *

from .unit import JubaTestCase

class JubaTestReporter(object):
    def create_report(self, result):
        raise NotImplementedError

    @classmethod
    def prettify_logs(self, servers):
        ent = []
        for (kind, host, port, log) in servers:
            if not log:
                continue
            ent.append("""
# ====== {kind} Log ({host}:{port}) ================================================== #
{log}
# ==================================================================================== #
""".format(kind=kind, host=host, port=port, log=log))
        return '\n'.join(ent)

class JubaTestTextReporter(JubaTestReporter):
    def create_report(self, result):
        buf = ""
        buf += """
===== TEST SUMMARY =====
  Total:  %d
   ( Error:  %d )
   (  Fail:  %d )
   (  Skip:  %d )
========================
        """ % (result.testsRun, len(result.errors), len(result.failures), len(result.skipped))

        buf += "\n----- Success -----\n{result}".format(result=('\n'.join(map(str, result.successes))))

        for elem in [('Failure', result.failures), ('Error', result.errors), ('Skipped', result.skipped)]:
            buf += "\n\n----- {heading} -----".format(heading=elem[0])
            for (test, err) in elem[1]:
                if elem[0] != 'Skipped':
                    logs = '(no logs available)\n'
                    if hasattr(test, 'logs'):
                        logs = self.prettify_logs(test.logs) + '\n'
                else:
                    logs = ''
                buf += "\n{name}:\n{err}\n{logs}".format(name=str(test), err=err, logs=logs)
        return buf


class JubaTestXunitReporter(JubaTestReporter):
    def create_report(self, result):
        def _setAttributes(node, attrs):
            map(lambda x: node.setAttribute(x[0], x[1]), attrs)

        def _setMeasurementForPlot(doc, record):
            results = []
            for key in record:
                measurement = doc.createElement('measurement')
                name = doc.createElement('name')
                name.appendChild(doc.createTextNode(str(key)))
                value = doc.createElement('value')
                value.appendChild(doc.createTextNode(str(record[key])))
                measurement.appendChild(name)
                measurement.appendChild(value)
                results += [measurement.toxml()]
            return '\n'.join(results)

        def _testcase(doc, test):
            node = doc.createElement('testcase')
            test_id = test.id()
            if ':' in test_id: # test comes from generator
                (test_id, test_args) = test_id.split(':', 1)
                test_args = ':' + test_args
            else:
                test_args = ''
            (test_class, test_name) = test_id.rsplit('.', 1)
            _setAttributes(node, [
                ('classname', test_class),
                ('name',      test_name + test_args),
            ])
            if hasattr(test, 'timeTaken'):
                _setAttributes(node, [
                    ('time', str(test.timeTaken)),
                ])
            if hasattr(test, 'get_record'):
                record = test.get_record()
                if record:
                    stdout = doc.createElement('system-out')
                    node.appendChild(stdout)
                    stdout.appendChild(doc.createTextNode(_setMeasurementForPlot(doc, record)))
            if hasattr(test, 'logs'):
                logs = self.prettify_logs(test.logs)
                stderr = doc.createElement('system-err')
                node.appendChild(stderr)
                stderr.appendChild(doc.createTextNode(logs))
            return node

        def _testcase_notok(doc, test, msg, result):
            node = _testcase(doc, test)
            node_inner = doc.createElement(result)
            node_inner.appendChild(doc.createTextNode(msg))
            node.appendChild(node_inner)
            return node

        doc = Document()
        suiteNode = doc.createElement('testsuite')
        _setAttributes(suiteNode, [
            ('name',     'jubatest'),
            ('tests',    str(result.testsRun)),
            ('errors',   str(len(result.errors))),
            ('failures', str(len(result.failures))),
            ('skip',     str(len(result.skipped))),
        ])

        for test in result.successes:
            suiteNode.appendChild(_testcase(doc, test))
        for (test, msg) in result.failures:
            suiteNode.appendChild(_testcase_notok(doc, test, msg, 'failure'))
        for (test, msg) in result.errors:
            suiteNode.appendChild(_testcase_notok(doc, test, msg, 'error'))
        for (test, msg) in result.skipped:
            suiteNode.appendChild(_testcase_notok(doc, test, msg, 'skipped'))

        doc.appendChild(suiteNode)
        return doc.toprettyxml(indent=' ')
