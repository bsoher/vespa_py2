# Python modules
from __future__ import division

# 3rd party modules
import setuptools


VERSION = open("VERSION").read().strip()

NAME = "Vespa-Suite"

DESCRIPTION = """Vespa is a suite of inter-connnected applications for magnetic resonance spectroscopy simulation and data analysis."""

LONG_DESCRIPTION = """Vespa stands for Versatile Simulation, Pulses, and Analysis. The Vespa
package migrates three previously developed magnetic resonance spectroscopy (MRS) software tools
into an integrated, open source, open development platform. The applications are called Pulse,
Simulation and Analysis and allow users to design RF pulses, create spectral simulations and
perform spectral data processing and analysis.  A (newer) fourth application called Priorset
creates simulated spectroscopy data sets.

The Vespa project addresses previous software limitations, including: non-standard data access,
closed source multiple language software that complicate algorithm extension and comparison,
lack of integration between programs for sharing prior information, and incomplete or missing
documentation and educational content.

These applications can be run separately but can communicate among themselves via a shared
database of objects/results.  One example of inter-application sharing might be that
Simulation would make use of an RF pulse designed in Pulse application to create a more
realistic MR simulation."""

MAINTAINER = "Dr. Brian J. Soher"
MAINTAINER_EMAIL = "bsoher@briansoher.com"
URL = "http://scion.duhs.duke.edu/vespa/"
# http://pypi.python.org/pypi?:action=list_classifiers
CLASSIFIERS = [ "Development Status :: 5 - Production/Stable",
                "Intended Audience :: Science/Research",
                "Intended Audience :: Healthcare Industry",
                "License :: OSI Approved :: BSD License",
                "Operating System :: MacOS :: MacOS X",
                "Operating System :: Unix",
                "Operating System :: POSIX :: Linux",
                "Operating System :: Microsoft :: Windows",
                "Programming Language :: Python :: 2.7",
              ]
LICENSE = "http://creativecommons.org/licenses/BSD/"
PLATFORMS = 'Linux, OS X, Windows, POSIX'
KEYWORDS = "mri, mrs, pygamma, spectral simulation, rf pulses, magnetic resonance spectroscopy, fitting, time domain, frequency domain"

packages = setuptools.find_packages()

setuptools.setup(name=NAME,
                 version=VERSION,
                 packages=packages,
                 url=URL,
                 maintainer=MAINTAINER,
                 maintainer_email=MAINTAINER_EMAIL,
                 zip_safe=False,
                 include_package_data=True,
                 classifiers=CLASSIFIERS,
                 license=LICENSE,
                 description=DESCRIPTION,
                 long_description=LONG_DESCRIPTION,
                 platforms=PLATFORMS,
                 keywords=KEYWORDS,
                 # setuptools should be installed along with Vespa; the latter requires the
                 # former to run. (Vespa uses setuptools' pkg_resources in get_vespa_version()
                 # to get the package version.) Since Vespa is distributed as a wheel which can
                 # only be installed by pip, and pip installs setuptools, this 'install_requires'
                 # is probably superfluous and just serves as documentation.
                 install_requires=['setuptools'],
                 )
