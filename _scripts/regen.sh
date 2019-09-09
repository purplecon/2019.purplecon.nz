#! /bin/bash

mv ~/Downloads/Schedule\ -\ Schedule.csv all_schedule.csv
mv ~/Downloads/All\ submissions\ -\ Form\ Responses\ 1.csv all_talks.csv
cd ../_data 
python3 make_schedule.py ../_scripts/all_schedule.csv
python3 make_talks.py ../_scripts/all_talks.csv

