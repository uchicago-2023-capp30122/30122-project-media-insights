/data/comment_data.json:
	curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
	cd "${curr_dir}"/scraping

	poetry run python comments.py