.PHONY: doc clean test test-unit test-framework test-usecase

doc:
	rm -rf doc
	mkdir doc
	cd doc && PYTHONPATH=../lib pydoc -w ../lib

clean:
	rm -rf doc

test: test-unit test-framework test-usecase

test-unit:
	PYTHONPATH=lib bin/jubatest --config envdef.py --testcase test/unit

test-framework:
	PYTHONPATH=lib bin/jubatest --config envdef.py --testcase test/framework

test-usecase:
	PYTHONPATH=lib bin/jubatest --config envdef.py --testcase test/usecase

regenerate-config:
	util/generate_default_config.py /opt/jubatus/share/jubatus/example/config > lib/jubatest/_jubatus_config.py
