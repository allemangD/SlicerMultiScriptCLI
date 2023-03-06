#-----------------------------------------------------------------------------
set(MODULE_NAME SampleCLI)

SlicerMacroBuildScriptedCLI(
    NAME ${MODULE_NAME}
)

slicerMacroBuildScriptedModule(
    NAME InnerLibrary
    SCRIPTS InnerLibrary/__init__.py
)
