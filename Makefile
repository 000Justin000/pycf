PYTHON  = python
MPIF90  = mpif90
F2PY    = f2py --fcompiler=intelem
MPIEXEC = mpiexec
NP_FLAG = -n
NP = 6

helloworld.so: helloworld.f90
	${F2PY} --f90exec=${MPIF90} -m helloworld -c $<

test: helloworld.so
	${MPIEXEC} ${NP_FLAG} ${NP} ${PYTHON} test.py

clean:
	${RM} helloworld.so
