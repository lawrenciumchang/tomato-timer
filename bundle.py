from setuptools import setup

APP = ['tomato-timer.py']
DATA_FILES = []
OPTIONS = {
  'argv_emulation': True,
  'iconfile': 'icon.icns',
  'plist': {
    'CFBundleShortVersionString': '0.2.0',
    'LSUIElement': True,
  },
  'packages': ['rumps', 'chime'],
}

setup(
  app=APP,
  name='Tomato Timer',
  data_files=DATA_FILES,
  options={'py2app': OPTIONS},
  setup_requires=['py2app'], install_requires=['rumps', 'chime']
)
