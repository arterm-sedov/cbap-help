# The language list is set in line 23 as LANGUAGE_LIST 

# After this script runs, you should see the newly compiled help subfolders in the `Web\help` folder:
#     * en
#     * ru

# from __future__ import unicode_literals, absolute_import

import os
import sys
import shutil
import subprocess

# check if mkdocs is present
print("Checking if mkdocs is installed")
try:
    import mkdocs
except ImportError:
    print("You need to have mkdocs installed!")
    sys.exit(1)
print("Mkdocs is present")

LANGUAGE_LIST = ["en", "ru"]
THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))
HELP_SOURCE_DIR = THIS_FILE_DIR
DOCS_DIR = os.path.join(HELP_SOURCE_DIR, "docs")
HELP_COMPILED_DIR = os.path.join(THIS_FILE_DIR, "..", "web", "help")
EXTRA_STYLESHEETS_SOURCE_DIR = os.path.join(DOCS_DIR, "stylesheets")
EXTRA_STYLESHEETS_COMPILED_DIR = os.path.join(HELP_COMPILED_DIR, "stylesheets")


def build_mkdocs(langCodes):
    if os.path.exists(HELP_COMPILED_DIR):
        print("\nFound %s folder\nDeleting it" % HELP_COMPILED_DIR)
        try:
            shutil.rmtree(HELP_COMPILED_DIR, ignore_errors=True, onerror=None)
            print("\nDeleted the %s folder\n" % HELP_COMPILED_DIR)
        except IOError:
                print("\nCould not delete the the %s folder\n" % HELP_COMPILED_DIR)
    
    for langCode in langCodes:
        CONFIG_FILE = resolve_condig_filename(langCode)
        if CONFIG_FILE:
            print("\nCompiling the mkdocs for %s:\n %s\n" % (langCode.upper(), CONFIG_FILE))
            pipe = subprocess.PIPE
            mkdocs_process = subprocess.Popen(
                ["mkdocs", "build", "-f", CONFIG_FILE], stdout=pipe, stderr=pipe)
            std_op, std_err_op = mkdocs_process.communicate()

            print(std_err_op, "\n", std_op)

    return True

def resolve_condig_filename(langCode):

    fileName = "mkdocs_" + langCode + ".yml"
    CONFIG_FILE = os.path.join(HELP_SOURCE_DIR, fileName)
    if os.path.exists(CONFIG_FILE):
        print("\nFound the %s language config file:\n %s\n" % 
         (langCode.upper(), CONFIG_FILE))
        return CONFIG_FILE
    else: 
        print("\nNo %s language config file:\n %s\n" % 
        (langCode.upper(), CONFIG_FILE))
        return False

if __name__ == "__main__":

    if not os.path.isdir(DOCS_DIR):
        print("This NOT the source Help directory: %s" % HELP_SOURCE_DIR)
        sys.exit(1)

    print("\nLanguages to build:", LANGUAGE_LIST)

    if build_mkdocs(LANGUAGE_LIST):
        print('\nFinished compiling the mkdocs\n')
    else: 
        print('\nCould not compile the mkdocs\n')
        sys.exit(1)
