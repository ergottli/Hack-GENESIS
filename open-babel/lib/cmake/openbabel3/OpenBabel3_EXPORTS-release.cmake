#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "openbabel" for configuration "Release"
set_property(TARGET openbabel APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(openbabel PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopenbabel.6.0.0.dylib"
  IMPORTED_SONAME_RELEASE "/usr/local/Cellar/open-babel/3.0.0/lib/libopenbabel.6.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS openbabel )
list(APPEND _IMPORT_CHECK_FILES_FOR_openbabel "${_IMPORT_PREFIX}/lib/libopenbabel.6.0.0.dylib" )

# Import target "inchi" for configuration "Release"
set_property(TARGET inchi APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(inchi PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libinchi.0.4.1.dylib"
  IMPORTED_SONAME_RELEASE "/usr/local/Cellar/open-babel/3.0.0/lib/libinchi.0.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS inchi )
list(APPEND _IMPORT_CHECK_FILES_FOR_inchi "${_IMPORT_PREFIX}/lib/libinchi.0.4.1.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
