## Usage on Django and React Js

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

Run django server
```bash
./manage.py runserver
```

In other terminal , compile file and run webpack dev server
```bash
./node_modules/.bin/webpack --config webpack.config.js

node server.js
```


The default home.html in templates is over ridden by React Js. Any changes made to `assets/js/app.jsx` show in browser.
