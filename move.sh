#!/bin/bash
timestamp=$(date -Is|tr : -)
mv Downloads/copy.txt Downloads/copy$timestamp.txt
mv Downloads/copy$timestamp.txt Datastore/