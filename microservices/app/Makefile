whiterose:
	gunicorn --reload --bind "0.0.0.0:8080" src:app

pushcode:
	git push hasura master

live:
	hasura microservice open app
