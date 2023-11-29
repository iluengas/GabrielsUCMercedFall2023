#!/bin/bash

rm -f output/*

#javac Lab_9.java
#java -classpath ".:sqlite-jdbc-3.32.3.2.jar" Lab_9

python3 Lab_9.py

sqlite3 tpch.sqlite ".schema" > output/schema.out

if grep -q -i "create view V1" output/schema.out; then
  echo ""
else
	echo "View V1 does not exist!"
fi

if grep -q -i "create view V2" output/schema.out; then
  echo ""
else
	echo "View V2 does not exist!"
fi

if grep -q -i "create view V4" output/schema.out; then
  echo ""
else
	echo "View V4 does not exist!"
fi

if grep -q -i "create view V10" output/schema.out; then
  echo ""
else
	echo "View V10 does not exist!"
fi

if grep -q -i "create view V111" output/schema.out; then
  echo ""
else
	echo "View V111 does not exist!"
fi

if grep -q -i "create view V112" output/schema.out; then
  echo ""
else
	echo "View V112 does not exist!"
fi
