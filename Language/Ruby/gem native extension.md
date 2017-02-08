# gem native extension

The code is compiled and linked so that the resulting executable file can be required by Ruby on the machine.

The usual reasons for writing a Ruby C or C++ extension are:

Speed. For some CPU-intense tasks, C code can be 100 times faster than Ruby. In this case a native extension can be completely stand-alone with all C source code included in the gem.
Third-party library already written in C. In this case the gem will have C source code that binds the library functions into Ruby modules, classes and methods.