# Demo: Library sources for Scripted CLI modules

This is a short example of a Scripted CLI module that depends on additional python scripts.

The most straightforward way of installing arbitrary Python scripts is to place those scripts in a python package, and install that package via a Scripted _loadable_ module.

Here there is a CLI module [`SampleCLI`][cli] that depends on two Python packages: [`InnerLibrary`][inner] and [`OuterLibrary`][outer].

[`OuterLibrary`][outer] is organized as a typical Slicer module, except that it does not have any top-level `.py` file. This prevents Slicer from attempting to create a GUI for the module. Note [`OuterLibrary/CMakeLists.txt`][outer-cmake] has similar structure to the module template.

[`InnerLibrary`][inner] is installed the same way, but is located inside the [`SampleCLI`][cli] directory. Notice the macro usage in [`SampleCLI/CMakeLists.txt`][cli-cmake]; `InnerLibrary` is installed the same way as `OuterLibrary` but it is colocated with the relevant CLI.

---

Notice in both cases, the corresponding python _package_ [may be imported directly][cli-py]. These packages could both also be imported from other _loadable_ modules.

---

Generally I recommend the approach as in `OuterLibrary` as it follows the more typicaly Slicer Module structure, but if there is a compelling code-organization reason to keep the extra scripts close to the CLI module, the `InnerLibrary` approach is also an option.

[cli]: ./SampleCLI
[cli-cmake]: ./SampleCLI/CMakeLists.txt
[cli-py]: ./SampleCLI/SampleCLI.py
[outer]: ./OuterLibrary
[outer-cmake]: ./OuterLibrary/CMakeLists.txt
[inner]: ./SampleCLI/InnerLibrary
