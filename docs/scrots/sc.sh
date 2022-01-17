#!/bin/bash
for f in ./*.py;
do
  echo "===$f===" >> fc.txt
  cat $f >> fc.txt
  echo "" >> fc.txt
  echo "" >> fc.txt
done