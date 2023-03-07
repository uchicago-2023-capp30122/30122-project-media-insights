.PHONY: everything

everything : data/transcript_data.json data/preprocessed_comments.json
	poetry run streamlit run media_insights/dashboard.py
	echo "Made everything"

data/transcript_data.json:
	export API_KEY="AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs" && cd scraping && poetry run python transcripts.py
	echo "From second source, finished scraping transcripts from YouTube"

data/comment_data.json:
	export API_KEY="AIzaSyBgP4m7PSCyZMn8V_cGnl4z6uAXryUtYFs" && cd scraping && poetry run python comments.py
	echo "Finished scraping raw comments data from YouTube"

data/clean_comment_data.json: data/comment_data.json
	cd scraping && poetry run python clean_comments.py
	echo "Finished cleaning raw comments data into videoId, date, and text"

data/preprocessed_comments.json: data/clean_comment_data.json
	cd .. && poetry run python media_insights/analysis/process_comments.py
	echo "Pre-processed comments"