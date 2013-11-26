AllToMantid
===========

Code to call existing reduction software and import it to Mantid.

All tests use the package ```asynccall.communicate.py``` to communicate through pipes with the Linux processes.

To date there are tests for Lamp and iFit. Both import create new workspaces in Mantid.

### Note:
Any of the test examples must be called from the Mantid Ipython console:
	View menu: Launch IPython console

E.g.:
```python
run /home/leal/git/AllToMantid/testMantid.py
```

