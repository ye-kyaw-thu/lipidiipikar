#!/bin/bash

python ./mk-uniq-list.py --input ./tst-data/manual-conv-without-athat.txt \
--output ./tst-data/manual-conv-without-athat.uniq --uniq

python ./tab2json.py --input ./tst-data/manual-conv-without-athat.uniq \
--output ./tst-data/manual-conv-without-athat.uniq.json --sort desc


