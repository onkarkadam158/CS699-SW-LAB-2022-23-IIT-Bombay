#!/bin/bash


sed -r 's/([0-9][0-9][0-9][0-9]) ([0-9][0-9][0-9][0-9]) ([0-9][0-9][0-9][0-9]) ([0-9][0-9][0-9][0-9])/\4 \3 \2 \1/' $1 > $2
