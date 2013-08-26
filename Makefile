.PHONY: doc clean

doc:
	rm -rf doc
	mkdir doc
	cd doc && PYTHONPATH=../lib pydoc -w ../lib

clean:
	rm -rf doc
