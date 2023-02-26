#!/bin/bash

echo "You can relax while we run the comments and clean_comments program."

sleep 2

curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "${curr_dir}"/scraping

poetry run python comments.py

sleep 5

poetry run python clean_comments.py

