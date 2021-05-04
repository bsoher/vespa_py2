# Python modules
from __future__ import division
import os
import sys
import subprocess

# 3rd party modules
try:
    import packaging.requirements as packaging_requirements
except ImportError:
    print "Please install 'packaging'. You can use this command:"
    print "pip install packaging"
    sys.exit()


# Note that this code can't assume too much about what's installed, nor about Vespa, so
# be careful what you try to import!


def strip_comment(line):
    """Strip from line everything after the first '#' character.

    If no such character is present, return line unchanged.
    """
    i = line.find('#')
    return line if (i == -1) else line[:i]


def scrub_lines(lines):
    """Given a list of lines from requirements.txt, returns them stripped of comments,
    leading/trailing whitespace, and blank lines.
    """
    lines = [strip_comment(line) for line in lines]
    lines = [line.strip() for line in lines]
    return [line for line in lines if line]


def get_installed_packages():
    """Returns a dict of {requirement.name: packaging.requirements.Requirement} based on the
    list generated by `pip freeze`.
    """
    # Since pip doesn't have an API (maybe someday?), we have to run it as a subprocess.
    cmd = 'pip freeze'
    installed = subprocess.check_output(cmd.split(' '), universal_newlines=True)
    installed = installed.split('\n')
    installed = scrub_lines(installed)
    installed = [packaging_requirements.Requirement(line) for line in installed]

    return {package.name: package for package in installed}


def is_fftw_ok():
    """Returns True if the FFTW runtime lib status is OK (is installed or isn't needed), False
    otherwise.

    This library is required by HLSVDPRO. Under OS X and Windows, it's statically linked. Under
    Linux it must be loaded at runtime, so this function always returns True under OS X and
    Windows and only under Linux can it return False.
    """
    all_is_well = True

    if "linux" in sys.platform.lower():
        import ctypes
        # Assume the worst unless we can prove otherwise.
        all_is_well = False
        # Look for it under several likely names.
        for name in ('libfftw3.so', 'libfftw.so.3', 'libfftw3.so.3'):
            try:
                ctypes.cdll.LoadLibrary(name)
            except OSError:
                pass
            else:
                # Loaded successfully
                all_is_well = True

    return all_is_well


def check_dependencies():
    """Checks the contents of requirements.txt and more (see below) against the list of installed
    packages as reported by `pip freeze`.

    Returns a 3-tuple of (installed, missing, insufficient). 'installed' is a dict of
    {package_name: packaging.requirements.Requirement} that represents all installed packages.
    Packages are in this list regardless of whether or not Vespa needs them.
    The last two elements of the 3-tuple are lists of packaging.requirements.Requirement instances.
    Those in the 'missing' list are not installed at all. Those in the 'insufficient' list are
    installed but the version is not acceptable.

    A few things are not pip-installable (or not consistently so), like wxPython. Those are
    handled explicitly here.

    This contains a simplified requirements.txt parser. It doesn't handle all of the features of
    that grammar. For instance, line continuation and including other requirements files are not
    implemented. Parsing comments *is* implemented.
    """
    path, _ = os.path.split(__file__)
    filename = os.path.join(path, 'requirements.txt')
    # Here it is -- a requirements.txt parser in 3 lines!
    lines = open(filename, 'r').read().split('\n')
    lines = scrub_lines(lines)
    requirements = [packaging_requirements.Requirement(line) for line in lines]
    # Requirements can have markers like 'python_version<"2.7"' which distinguish them as
    # relevant (or not) in the current environment. Of course we want to ignore requirements
    # marked as irrelevant.
    requirements = [requirement for requirement in requirements if
                    (not requirement.marker or requirement.marker.evaluate())]

    installed = get_installed_packages()

    # Depending on how it is installed, wxPython may or may not be visible to pip. If we can
    # detect that it's installed but pip-invisible, we sneak it into the 'installed' dict.
    wx_package = installed.get('wxPython')
    if not wx_package:
        # Try to import it.
        version = None
        try:
            import wx
            version = wx.__version__
        except ImportError:
            pass
        if version:
            # Found it!
            installed['wxPython'] = packaging_requirements.Requirement('wxPython==' + version)

    missing = []
    insufficient = []

    for requirement in requirements:
        package = installed.get(requirement.name)
        if not package:
            missing.append(requirement)
        else:
            # package.specifier has a slightly misleading name. It is actually a SpecifierSet
            # instance, and can contain zero or more Specifier objects. In this case, the
            # package comes from `pip freeze` output, so we know there will be exactly 1 specifier.
            package_specifier = [specifier for specifier in package.specifier][0]
            if package_specifier.version not in requirement.specifier:
                insufficient.append(requirement)

    # FFTW lib (Linux only) can't be expressed in requirements.txt, so we check for it explicitly.
    if not is_fftw_ok():
        # Add this to the list of missing requirements.
        missing.append(packaging_requirements.Requirement('fftw==3'))

    return installed, missing, insufficient


def report_dependencies(to_stdout=True):
    """Creates a report of the status of Vespa's dependencies. Failures are explicit about what's
    lacking so that the user has enough information to solve the problem.

    If to_stdout is True, the report is printed to stdout.

    The report is always returned as a string.
    """
    if to_stdout:
        print "Checking dependencies...\n"

    installed, missing, insufficient = check_dependencies()

    report = []

    if missing or insufficient:
        report.append("Vespa might not run properly because some dependencies are unmet.")

        if missing:
            report.append("The following dependencies are not installed:")
            for requirement in missing:
                specifiers = ';'.join([str(specifier) for specifier in requirement.specifier])
                report.append(" * %s%s" % (requirement.name, specifiers))

        if insufficient:
            report.append(
                "The following dependencies are installed, but Vespa needs a different version:")
            for requirement in insufficient:
                installed_package = installed[requirement.name]
                specifiers = ';'.join([str(specifier) for specifier in requirement.specifier])
                requirement = "%s%s" % (requirement.name, specifiers)

                report.append(" * %s is installed; Vespa requires %s" % \
                              (installed_package, requirement))

        report.append('')
        report.append("One can find information about satisfying these dependencies here:")
        report.append("http://scion.duhs.duke.edu/vespa/project")
    else:
        report.append('')
        report.append("Good news -- all of Vespa's dependencies are installed!")

    report = '\n'.join(report)

    if to_stdout:
        print(report)

def main():
    report_dependencies()

if __name__ == '__main__':
    main()
