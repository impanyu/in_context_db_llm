#!/bin/bash
python3 experiments_new_batch.py --model all --prompting few_shot --encoding sql --operation single_filtering --scale -1 
python3 experiments_new_batch.py --model all --prompting few_shot --encoding sql --operation single_filtering --balance -1
python3 experiments_new_batch.py --model all --prompting few_shot --encoding sql --operation single_filtering --overlap -1
