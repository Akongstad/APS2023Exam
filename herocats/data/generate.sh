#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution time.py              

compile generate_random.py
compile generate_nice.py
compile generate_notgreedy.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1
sample 2
sample 3
sample 4

tc  random1 generate_random 42 
tc  random2 generate_random 23
tc  random3 generate_random 1
tc  random4 generate_nice 1999 499 49 42
tc  random5 generate_nice 1999 499 49 42
tc  greedy generate_notgreedy
tc  edge1 generate_explicit

