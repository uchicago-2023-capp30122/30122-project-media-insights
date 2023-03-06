# .PHONY: everything

# everything : data/comment_data.json
# 	@echo "Making everything"

data/comment_data.json:
	cd scraping && poetry run python comments.py

data/clean_comment_data.json: data/comment_data.json
	cd scraping && poetry run python clean_comments.py