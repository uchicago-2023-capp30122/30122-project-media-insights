#!/bin/bash

echo "You can relax while we run all the programs for you. Slow Version"

curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "${curr_dir}"/scraping

poetry run python comments.py

echo -e "\n\nFinished scraping raw comments data from YouTube"

sleep 1

poetry run python clean_comments.py

echo -e "\n\nFinished cleaning raw comments data into videoId, date, and text"

sleep 1

poetry run python transcripts.py

echo -e "\n\nFrom second source, finished scraping transcripts from YouTube"

sleep 1

cd ../..

poetry run python media_insights/analysis/process_comments.py

sleep 4

poetry run streamlit run media_insights/dashboard.py

echo -e "\n\nCreating dashboard using streamlit"