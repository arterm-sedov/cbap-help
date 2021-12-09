# How to initialize the environment and build help files

1. Install Python, MkDocs, and dependencies:
    * If you do not have Python, cd to <Help\install> folder, run <install\installpymkd.ps1> — downloads and silently installs Python 3.10.1, then installs all MKDocs dependencies listed in the requirements.txt config file
    * If Python 3.10 is present in your system, cd to <Web> folder, execute <npm run installhelp> — installs all MKDocs dependencies listed in the requirements.txt config file
2. Execute <npm run buildhelp> — builds all languages help to <\web\help\>. The <npm run buildhelp> script is also executed with <npm run build> after the <localization> task.
3. Build and run the product normally. Switch to Russian language. You should see the Help question sign to the left of the search button in the top bar.

Python is not used in runitime at all, only to build the static HTML site from MD files.

# To serve Russian docs locally to http://127.0.0.1:8000 use this command (the server watches edits and rebuilds on the fly)

py -m mkdocs serve -f mkdocs_ru.yml

NO CUSTOM CSS IS APPLIED THIS WAY!!!

To see the Help with Comindware Business Application CSS (including dynamic theme CSS linking), build the docs and run the CBAP.

# To build Russian docs locally to \web\help\ru\ use this command:

py -m mkdocs build -f mkdocs_ru.yml

Then run <npm run build> or <npm run start> to see the Help system in action

# Installation and build commands

* install\installpymkd.ps1 — downloads and silently installs Python 3.10.1, then installs all MKDocs dependencies listed in the requirements.txt config file

* install\uninstallpymkd.ps1 — uninstalls Python and all MKDocs dependencies listed in the requirements.txt config file

* npm run buildhelp - builds all languages help to <\web\help\>
    - the list of languages to build help for is defined in the  localizedLanguages array at js\build\buildHelpTask.js

* npm run installhelp - installs all MKDocs dependencies listed in the requirements.txt config file
                        DOES NOT INSTALL THE PYTHON

# The help is powered by the very popular and well-maintained MkDocs framework: 
https://squidfunk.github.io/mkdocs-material/ 
https://github.com/squidfunk/mkdocs-material
https://www.mkdocs.org/

It is trusted by Atlassian, Mozilla, Google, Microsoft, Adruino, etc...
