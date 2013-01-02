rhino-py-repl
=============

Motivation
----------

Python scripting on the OSX version of Rhino is problematic. The only way to run a script is via the RunPythonScript command, which prompts the user to open a file. There is no console, stdout prints to the one-line status bar at the bottom of the screen, and the Python port of RhinoScript is prone to fail in ways that can't be predicted by reading the documentation. As a result, writing Python scripts for Rhino on OSX is extremely slow.

Description
-----------

This code provides Rhino with an interactive Python REPL. A client script running in a terminal window, collects user input, and sends it over a socket. A server script running within Rhino receives the input, evaluates it, and sends the result back to the client. Everything about this is fast, dirty, and ugly. But it works, mostly.


Usage
-----

In Rhino: 
    RunPythonScript server.py

In a separate Terminal window: 
    ./client.py