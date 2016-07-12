from mpi4py import MPI
import helloworld as hw

wd_comm  = MPI.COMM_WORLD
wd_size  = wd_comm.Get_size()
wd_rank  = wd_comm.Get_rank()

ms_color = wd_rank / 2
ms_comm  = wd_comm.Split(ms_color, wd_rank)

f_ms_comm = ms_comm.py2f()

hw.sayhello(f_ms_comm)

try:
    hw.sayhello(list())
except:
    pass
else:
    assert 0, "exception not raised"
