# tomato-timer

Mac menu-bar application that tells you when to stop working.

Based on this [project tutorial](https://camillovisini.com/article/create-macos-menu-bar-app-pomodoro/).

## Useful Commands for Development

### Install dependencies
```
pip3 install -U py2app
pip3 install -U rumps
pip3 install chime
```

### To run locally
```
python3 tomato-timer.py
```

### To bundle
```
python3 bundle.py py2app -A
```

App will appear in `dist` folder.
