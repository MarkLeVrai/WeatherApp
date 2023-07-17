[app]

# (str) Title of your application
title = EasyWeatherApp

# (str) Package name
package.name = com.example.easyweatherapp

# (str) Package domain (reverse domain notation)
package.domain = com.markapps

# (str) Source code where the main.py lives
source.dir = .

# (str) Main Python file
source.main = main.py

# (list) List of requirements (necessaires pour votre application)
requirements = kivy, requests, arabic-reshaper, bidi.algorithm

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Version of the application
version = 1.0

# (list) List of additional files and directories to include
#source.include_exts = py, png, jpg, kv, ttf
#source.include_patterns = assets/*,images/*.png,font.ttf

# (list) List of modules to include (dependencies are detected automatically, but you can also specify them manually)
#source.include_py_modules = main.py

# (list) List of modules to exclude (if empty, all modules are included)
#source.exclude_modules =

# (list) List of additional files to exclude
#source.exclude_exts = spec, gitignore, kate-swp

# (list) List of additional patterns to exclude
#source.exclude_patterns = licenses/*,tmp/*,*.bak

# (list) List of additional files to include (above patterns are also taken into account)
#source.include_files = icon.png, splash.jpg

# (bool) If you want to strip the debugging symbols
#strip = True

# (bool) Comment line for stripping debugging symbols
#strip_comment = True

# (str) Mac OS X application bundle (Mac OS X packaging only)
#osxapp_mainmenu = MainMenu.nib

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivy = ../../kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#p4a.source_dir = ../../kivy

# (list) List of build specific requirements (necessaires pour votre application)
#python-for-android will check those for you before distribution of the application
#p4a.build_dir = ./.buildozer/android/platform/build

# (str) Path to a custom blacklist file (default is empty)
#p4a.blacklist =

# (str) Path to a custom whitelist file (default is empty)
#p4a.whitelist =

# (str) Path to a custom blacklist file (default is empty)
#p4a.blacklist =

# (str) Path to a custom whitelist file (default is empty)
#p4a.whitelist =

# (str) Path to a custom blacklist file (default is empty)
#p4a.blacklist =

# (str) Path to a custom whitelist file (default is empty)
#p4a.whitelist =
