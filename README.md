# TkinterDnD2 (Fork)

This is a fork in a long line of forks.
The original [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2) bt pmgagne became unmaintained and was forked by [Eliav2](https://github.com/Eliav2/tkinterdnd2) in order to be listed as a PyPI package. It too, unfortunately appears to have become unmaintained. This repository aims to maintain it at a minimum for my own purposes. I will be reviewing the improvement recommendations from the older repositories and implementing them here. Those recommendations (which were really reasonable) never were implemented nor even received comments in greater than 2 years. 

But what is the project really? `tkinterdnd2` is a wrapper for [tkdnd](https://github.com/petasis/tkdnd). TkDnD is the addition of Drag-and-Drop capabilities to Tk, a cross-platform toolki for making user-interfaces. TkinterDnD2 is then intended for implementing those drag-and-drop capabilities easily into Tkinter (and thus Python) GUI applications.

This repository is not yet on PyPI, but may be in the future.

The following is the documentation from previous versions of this project, and has yet to be updated:

## usage

```python
import tkinter as tk

from tkinterdnd2 import DND_FILES, TkinterDnD

root = TkinterDnD.Tk()  # notice - use this instead of tk.Tk()

lb = tk.Listbox(root)
lb.insert(1, "drag files to here")

# register the listbox as a drop target
lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', lambda e: lb.insert(tk.END, e.data))

lb.pack()
root.mainloop()
```
![tkinterdnd2 example usage](https://i.stack.imgur.com/jnOWd.png)


see any of the [demos](./demos) for usage examples.

# tkinterdnd2

Tkinter native drag and drop support for windows, unix and Mac OSX.

## What is TkInterDnD2

[TkinterDnD2](http://tkinterdnd.sourceforge.net) is a python wrapper for George Petasis' tkDnD Tk extension version 2.

It is a domain public project.

## What is TkDnD2

[tkDnD2](https://github.com/petasis/tkdnd) is a tcl/Tk extension adding native drag and drop support.

## What this repository is about

It package TkinterDnD2 and tkdnd2 into a standard python module.

When the extension is imported in python its location will be automatically added to the Tk search path.

In this project we use the pre-compiled release
from https://github.com/petasis/tkdnd/releases/tag/tkdnd-release-test-v2.9.2 and copy them in tkinterdnd2/tkdnd.

## pyinstaller

If you want to use pyinstaller, you should use the hook-tkinterdnd2.py file included. Copy it in the base directory of
your project, then:

    pyinstaller -F -w myproject/myproject.py --additional-hooks-dir=.

