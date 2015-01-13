all: pypeFLOW FALCON DAZZ_DB DALIGNER

gitmodules:
	git submodule init
	git submodule update

pypeFLOW: gitmodules
	(cd pypeFLOW; python setup.py install --root ../resources)

FALCON: gitmodules
	(cd FALCON; python setup.py install --root ../resources)

DAZZ_DB: gitmodules
	$(MAKE) -C DAZZ_DB
	(cd DAZZ_DB; cp -f DBrm DBshow DBsplit DBstats fasta2DB ../resources/usr/bin/)

DALIGNER: gitmodules
	$(MAKE) -C DALIGNER
	(cd DALIGNER; cp -f daligner daligner_p DB2Falcon HPCdaligner LA4Falcon LAmerge LAsort ../resources/usr/bin/)

.PHONY: all pypeFLOW FALCON DAZZ_DB DALIGNER gitmodules
