# How to initialize the environment and build help files

**Note: Python is not used in runitime**, it is only used to build the static HTML site from the source .MD files.

1. Install Python, if you do not have it:

* Change dir to `Help\install`

* Run `install\installpy.ps1`
    * this script downloads and silently installs the latest Python from _python.org_ (icluding the `pip` package manager).

2. Install MkDocs and dependencies (when you have Python):

* Change dir to `Help\install` (if you are not there yet)

* Run  `installmkdocs.ps1`
    * this script installs all MKDocs dependencies listed in the `requirements.txt` config file and has only one command:
        * `py -m pip install -U -r requirements.txt`

3. Build the help files to `Web\help`

* Change dir to `Help` under the solution root folder.
    
    * Execute `py buildhelp.py` — builds languages help to `Web\help`.

    * The language list is set in `line 23` in `buildhelp.py` as an array:
        
        `LANGUAGE_LIST = ["en", "ru"]`

    * The `py buildhelp` script can also be executed with:
        
        `npm run buildhelp`

    * You should see the newly compiled help subfolders in the `Web\help` folder:
        * en
        * ru
        * stylesheets

3. Build and run the product normally and see the Help system in action.

    * Change dir to `Web` within the solution root folder.
    * Execute `npm run build` or `npm run start`.
    * You should see the Help question sign to the left of the search button in the top bar:
        * The CSS is pulled dynamically from the current theme.
        * The help is displayed in the current CBAP language.
        * The help is context dependent: it shows the topic for the current module.
    
            See the help button and context resolver code:
            `js\modules\shared\view\help\HelpPathMappingService.js`
            `js\modules\shared\view\help\HelpButtonView.js`
            `js\modules\shared\view\NavigationToolbarView.js` _line 137_

# Testing: running and authoring the help without building it or compiling the product
To serve both English and Russian docs locally at http://127.0.0.1:8000 

* Change dir to `Help` under the solution root folder.
* Execute the command:

`mkdocs serve` (or `py -m mkdocs serve`)

**NOTE:**
* The help is not build by, it is only served locally to http://127.0.0.1:8000.
* The server watches for edits in the `Help\docs` folder and updates the help on the fly. Any edits you make in the `docs` folder will be immediately reflected at http://127.0.0.1:8000.
* _At http://127.0.0.1:8000 you will see En and Ru help navigation tree together, **this is different from the single language view in the actual product**. Within CBAP the help only shows in the current language and **the left navigation bar looks different fro the locally served one**._
* _The navigation at http://127.0.0.1:8000 will be in Russian per the theme.language setting in the mkdocs_en_ru_local.yml_, while in CBAP the navigation language changes per the CBAP language.
* _The CSS is not dynamically pulled from the CBAP to http://127.0.0.1:8000_

# Uninstallation scripts

* `install\uninstallmkdocs.ps1` — uninstalls installs all MKDocs dependencies listed in the `requirements.txt` config file, runs a single command: `py -m pip uninstall -y -r requirements.txt`

* `install\uninstallpy.ps1` — silently uninstalls Python, runs a single command: `.\python_latest.exe /uninstall /quiet`

# The help is powered by the very popular and well-maintained MkDocs framework: 
https://squidfunk.github.io/mkdocs-material/ 
https://github.com/squidfunk/mkdocs-material
https://www.mkdocs.org/

This framework is trusted by Atlassian, Mozilla, Google, Microsoft, Adruino, etc...
