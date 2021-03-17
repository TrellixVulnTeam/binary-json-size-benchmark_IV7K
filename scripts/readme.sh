#!/bin/sh

set -eu

echo "Binary JSON-compatible Format Size Benchmark"
echo "============================================"
echo "
A size benchmark of JSON-compatible binary serialization formats.
"

echo "- [JSON documents](#json-documents)"
echo "- [Serialization formats](#serialization-formats)"
echo "- [Results](#results)"
for document in output/*
do
  DOCUMENT_ID="$(basename "$document")"
  TITLE="$(tr -d '\n' < "benchmark/$DOCUMENT_ID/NAME")"
  echo "    - [$TITLE](#$DOCUMENT_ID)"
done
echo "- [Running locally](#running-locally)"
echo "- [License](#license)"

echo "
JSON documents
--------------

| Name | Type | Link | SchemaStore |
|------|------|------|-------------|"

for document in output/*
do
  DOCUMENT_ID="$(basename "$document")"
  TITLE="$(tr -d '\n' < "benchmark/$DOCUMENT_ID/NAME")"
  SCHEMASTORE_URL="$(tr -d '\n' < "benchmark/$DOCUMENT_ID/SOURCE")"
  printf "| %s | %s | %s | %s |\n" \
    "[$TITLE](#$DOCUMENT_ID)" \
    "$(cat "benchmark/$DOCUMENT_ID/TAXONOMY")" \
    "[:arrow_upper_right:](benchmark/$DOCUMENT_ID/document.json)" \
    "[:arrow_upper_right:]($SCHEMASTORE_URL)"
done

echo "
Serialization formats
---------------------
"

cat docs/versions.markdown

echo "
Results
-------
"

for document in output/*
do
  DOCUMENT_ID="$(basename "$document")"
  TITLE="$(tr -d '\n' < "benchmark/$DOCUMENT_ID/NAME")"
  echo "<h3 id=\"$DOCUMENT_ID\">$TITLE</h3>"
  echo ""
  echo "![$TITLE chart](./charts/$DOCUMENT_ID.png)"
  echo ""

awk -f data.awk "output/$DOCUMENT_ID/data.dat"
echo ""

done

echo "
Running locally
---------------
"

cat docs/reproducibility.markdown

echo "
License
-------

This work is released under the Apache-2.0 license."
