install:
	python setup.py install

bdist:
	python setup.py bdist

wheel:
	python setup.py bdist_wheel

rpm:
	python setup.py bdist_rpm

upload:
	python setup.py bdist_rpm bdist_wheel upload

clean:
	rm -fr pymschap.egg-info
	rm -fr dist
	rm -fr build
	rm -fr venv



.PHONY:  install upload  clean

