# ghost test
# http://jeanphix.me/Ghost.py/
# http://ghost-py.readthedocs.org/en/latest/

from ghost import Ghost
ghost = Ghost()

##url = "https://www.biblegateway.com/passage/?search=John+1&version=AMP"

page, extra_resources = ghost.open(url)