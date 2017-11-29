import sys, os
import psi4
sys.path.insert(1, '../')
import spinflip
from spinflip import sf_cas

# threshold for value equality
threshold = 1e-7
# setting up molecule
n2 = psi4.core.Molecule.create_molecule_from_string("""
0 7
N 0 0 0
N 0 0 2.5
symmetry c1
""")

# Test: SF-CAS/STO-3G with N2 (0,7 to 0,1)
def test_1():
  options = {"basis": "cc-pvdz", 'num_roots': 4}
  e = sf_cas( 0, 1, n2, conf_space="1x", add_opts=options )
  expected = -108.780110376393
  assert (e - expected) < threshold

