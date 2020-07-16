FROM python:3.6-alpine
RUN apk --update --no-cache add \
	git && pip3 install gitpython requests bs4

RUN python -c 'from git import Repo; Repo.clone_from("https://github.com/l0gan/domainCat", "/usr/src/domainCat/")'

WORKDIR /usr/src/domainCat

ENTRYPOINT [ "python3", "domainCat.py" ]