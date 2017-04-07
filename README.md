## Usage on Django and React Js

### Requirements
+ Python 3
+ virtualenvwrapper
+ git
+ NodeJS 4+ with NPM 3+

Setup virtaulwrapper, virtualenv (not required)
```bash
mkvirtualenv djr
workon djr
```

Install dependencies
```bash
pip install -r requirements.txt
npm install
```

Django migrate, create admin user
```bash
./manage.py migrate
 ./manage.py createsuperuser
```

Run django server
```bash
./manage.py runserver
```

Login to Django Admin, create CMS pages
```bash
http://localhost:8040/admin/
```

In other terminal , compile file and run webpack dev server
```bash
./node_modules/.bin/webpack --config webpack.config.js --progress --colors

node server.js
```


The default home.html in templates is over ridden by React Js. Any changes made to `assets/js/app.jsx` shows in browser.
