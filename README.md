# The vespa_py2 Repository

Last Python 2 compatible version of the Vespa MRS software package

Project: Vespa
Contact: Brian J. Soher
Email:   vespa.mrs@gmail.com
Licence: BSD, specifically a "three-clause" BSD license

For the most up-to-date information regarding installation, usage, 
technical details, and the complete list of developers see the wiki:

http://scion.duhs.duke.edu/vespa/project/wiki (now defunct)

#----------------------------------------------------------------------------#

DESCRIPTION:

Vespa stands for Versatile Simulation, Pulses, and Analysis. The environment 
contains four magnetic resonance spectroscopy (MRS) software applications 
called Pulse, Simulation, Priorset and Analysis. These are applications for   
MR RF pulse design, MRS spectral simulation, creation of fake MRS data and 
spectral processing/analysis of MRS data.

The Vespa package is an extensive redesign of three previously developed 
magnetic resonance spectroscopy (MRS) software tools that enhances their 
functionality and migrates them into an integrated, open source, open 
development platform. 

The original tools migrated into this package include:  

  MatPulse (RFPulse) - software for RF pulse design written in Matlab, 
  GAVA/Gamma (Simulation) - software for spectral simulation written in IDL
  IDL_Vespa (Analysis) - spectral data processing and analysis written in IDL 

The Vespa project addresses previous software limitations, of non-standard 
data access, closed source and multiple language software that complicates 
algorithm extension, and a lack of integration between programs by porting 
all the code to Python, and using a shared database design, with high-quality
documentation. 

These applications can be run separately, but can also communicate via 
a shared database of objects/results. This integration will make the package
even more valuable by allowing, for example, Simulation to make use of an RF 
pulse designed in Pulse to create a more realistic MR simulation.

Thanks to the NIH (grant number 1R01EB008387-01A1) for funding the maintenance 
and extension of these separate applications into a combined environment based 
entirely on the Python language.

#----------------------------------------------------------------------------#

COMPATIBILITY:

Vespa has been tested and is certified to run on the following systems: 
Windows, Macintosh OSX, and Linux. 

However, it should run on any system that supports python and wxpython.

#----------------------------------------------------------------------------#