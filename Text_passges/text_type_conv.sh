#!/bin/bash

for f in AI*.rtf OR*.rtf
do
    pandoc -t plain "$f" | sed -n '1,/Multiple Choice Questions/p' | sed '/Multiple Choice Questions/d' > ${f%.rtf}.txt
done
