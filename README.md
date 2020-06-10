# twitoff-pt5

<!-- Installation -->

```sh
git clone ________
cd twitoff-pt5/
```

<!-- Setup -->

```sh
pipenv install
```



migrate the database:

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```
<!-- Usage -->

```sh
FLASK_APP=web_app flask run
```
