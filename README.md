# janscalckernel

![alt](janscalckernel/logo-svg.svg)

A simple and robust jupyter kernel implementation of [calc](http://www.isthe.com/chongo/tech/comp/calc/).
This was a follow-up to a previous kernel (for bc) I made where I ran into some problems with pexpect.
Realised with the IPython Kernel subclass and pexpect REPLWrapper.

## Dev Installation

- install calc from your distro's package manager
- `pip install` jupyterlab and pexpect
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user janscalckernel`

## Uninstall

- `jupyter kernelspec uninstall janscalckernel`
- `pip uninstall janscalckernel`
