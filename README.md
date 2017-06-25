
# wc.py visual interface


![Image of wcpy API](https://github.com/axsauze/wcpy-api/blob/master/assets/wcpy-api.jpg)

This repository contains the visual interface to interact with the [wc.py library](http://github.com/axsauze/wcpy).

# Installing WCPY interface

**NOTE: Python 3.x is required to run this application**.

In order to install the interface it is recommended to use virtualenv:

```
virtualenv --no-site-packages -p python3 venv

source venv/bin/activate
```

Then make sure you install the requirements with `pip`:

```
pip install -r src/requirements.txt
```

# Running Interface

To run the application, all you have to do, is start it with:

```
python src/app/app.py
```

And then just open `web/index.html` in your browser to interact with the wcpy interface.




