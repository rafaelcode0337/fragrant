clean:
	rm -rf *egg-info
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
