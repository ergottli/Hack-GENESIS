# The OpenBabel2 config file. To get the targets include the exports file.
get_filename_component(OpenBabel2_INSTALL_PREFIX "${OpenBabel2_DIR}/../../.."
  ABSOLUTE)

set(OpenBabel2_VERSION_MAJOR   "3")
set(OpenBabel2_VERSION_MINOR   "0")
set(OpenBabel2_VERSION_PATCH   "0")
set(OpenBabel2_VERSION         "3.0.0")

set(OpenBabel2_INCLUDE_DIRS "")
set(OpenBabel2_EXPORTS_FILE "${OpenBabel3_INSTALL_PREFIX}/lib/cmake/openbabel3/OpenBabel3_EXPORTS.cmake")
set(OpenBabel2_ENABLE_VERSIONED_FORMATS "ON")

# Include the exports file to import the exported OpenBabel targets
include("${OpenBabel2_EXPORTS_FILE}")
