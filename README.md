# Coeden for python

Coeden is a library to make work with tree data structures ergonimic and ideomatic in python.

### Disclaimer
This library is in an early alpha stage, expect major changes in the API in subsequent versions. 

# Getting started
## Requirements
Python >= 3.10.x

## Install
You can install it with pip:

```
python3 -m pip install coeden
```

# Documentation
## Create a tree
In coeden there is no tree object, the trees are made of nodes and from every node you can create new leafs (nodes without childs). 

Let's create a simple tree with 3 levels of depth:
``` 
from coeden import node

color_tree = Node("colors")
```

and this node can grow new leafs
```
color_tree["colors"].new_leaf("red")
color_tree["colors"].new_leaf("blue")
color_tree["colors"].new_leaf("green")
```

then `blue` can grow a couple of leafs or typing the whole chain
```
color_tree["colors"]["blue"].new_leaf("marine")
color_tree["colors"]["blue"].new_leaf("celeste")
```

also, the red node can be stored in a variable and grow some leafs from it
```
red = color_tree["colors]["red"]
red.new_leaf["dark"]
red.new_leaf["velvet"]
```

The current tree can be printed like this
```
color_tree.print_tree()

# Output
colors
  red
    dark
    velvet
  blue
    marine
    celeste
  green
```

but as all nodes are the starting point of their own tree blue can print its own tree, that happens to be a subtree of colors because blue belong to colors

```
blue.print_tree()

# Output
blue
  marine
  celeste
```

## Traversing the tree
Trees are traversed using the index operator `[]`. Using the brackets you can traverse the previous tree from the root to the velvet node for example
```
if color_tree["red"]["velvet"] != None:
    ...    
```

this is kind of a nested dictionary (and they are internaly nested dictionaries indeed) but it hides some interesting features that normal dicts do not.

### Traverse inexistent nodes
Imagine you want to check the existance of "dark gray" in the tree with dictionaries you have to do something like:
```
if color_tree["gray"] != None and color_tree["gray"]["dark"] != None:
    ...
```
or at least wrap it in a try/except. But coeden allows to make free test for existance
```
if color_tree["gray"]["dark"] != None:
    print("Nice color!")
else:
    print("Nah, not a real color")

# Output
Nah, not a real color 
```
or even better you can create al the inexistent nodes in one call with
```
color_tree["gray"]["dark"].create_all()
color_tree.print_tree()

# Output
colors
  red
    dark
    velvet
  blue
    marine
    celeste
  green
  gray
    dark
```

### Wildcards
Wilcards allow to consider every node of a level, for instance, we can search for marine node without knowing it is blue.
```
marine = color_tree["__*__"]["marine"]  # Marine is an iterable set of nodes
```
but wildcards return sets of nodes and not nodes so there are two options, if you know that there is going to be only one node you can use the special key `"__?__"` that converts the set to a node again its length is exactly one. If there are more the sets can be iterated in a loop.

```
marine = color_tree["__*__"]["marine"]["__?__"]  # Now it is the node 
print("marine parent: " + marine.parent.key)

for node in color_tree["__*__"]["dark"]:
   print("dark parent: " + node.key)

# Output
marine parent: blue
dark parent: red
dark parent: gray 
```