#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution accepted_iterative_space_op.py

compile generate_random.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1
sample 2
sample 3
sample 4

tc  random1 generate_random 
tc  random2 generate_random
tc  random3 generate_random
tc  random4 generate_random
tc  random5 generate_random
tc  edge1 generate_explicit 2 2 1 1
tc  edge2 generate_explicit 500 100 50 1
tc  edge3 generate_explicit 500 100 50 2
tc  edge4 generate_explicit 500 100 50 4
tc  edge5 generate_explicit 500 100 50 8