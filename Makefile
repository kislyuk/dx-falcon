all: pypeFLOW FALCON DAZZ_DB DALIGNER

gitmodules:
	git submodule init
	git submodule update

pypeFLOW: gitmodules
	(cd pypeFLOW; rm -rf dist; python setup.py sdist)
	pip install --root "$$(pwd)/resources" --ignore-installed pypeFLOW/dist/*.tar.gz

FALCON: gitmodules
	(cd FALCON; rm -rf dist; python setup.py sdist)
	pip install --root "$$(pwd)/resources" --ignore-installed FALCON/dist/*.tar.gz

DAZZ_DB: gitmodules
	$(MAKE) -C DAZZ_DB
	(cd DAZZ_DB; cp -f DBrm DBshow DBsplit DBstats fasta2DB ../resources/usr/bin/)

DALIGNER: gitmodules
	$(MAKE) -C DALIGNER
	(cd DALIGNER; cp -f daligner daligner_p DB2Falcon HPCdaligner LA4Falcon LAmerge LAsort ../resources/usr/bin/)

.PHONY: all pypeFLOW FALCON DAZZ_DB DALIGNER gitmodules
