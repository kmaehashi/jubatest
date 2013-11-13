.PHONY: doc test clean

doc:
	rm -rf doc
	mkdir doc
	cd doc && PYTHONPATH=../lib pydoc -w ../lib

test:
	PYTHONPATH=lib bin/jubatest --config envdef.py --testcase test

clean:
	rm -rf doc
