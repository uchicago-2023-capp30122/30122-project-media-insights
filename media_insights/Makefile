# .PHONY: everything

# everything : data/comment_data.json
# 	@echo "Making everything"

data/transcript_data.json:
	cd scraping && poetry run python transcripts.py

data/comment_data.json:
	cd scraping && poetry run python comments.py

data/clean_comment_data.json: data/comment_data.json
	cd scraping && poetry run python clean_comments.py

data/preprocessed_comments.json: data/clean_comment_data.json
	cd .. && poetry run python media_insights/analysis/process_comments.py