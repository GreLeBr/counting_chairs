# Counting chair:
Counting chairs from map in a text file

# Installation: 
You need python, re, os, argparse  

Download the package and move to the decompressed directory run:
`pip install -e .`

To use the script run (with options):
`chairs_counting`
Options are :
* --d or --dir -> to specify the location of map file if you want to specify one or it will use the files where you are launching the script from
* --o or --out -> to specify the path for outpulfile, by default it is the same folder and append _output to a map file  

So for example, in a folder where is a map file:
`chairs_counting`

# WIP:
Test on other files

# Instructions:

1. Count and sort variables in a matrix.

2. Create a coordinate system to define different rooms

turning points:   
+-    +      +
      I      /

Task:
Apartment And Chair Delivery Limited has a unique position on the housing market.
The company not only builds apartments, but also equips them with chairs.
Now the business has grown continuously over the past few years and
there are a few organizational problems that could be solved by automation.

We will focus on one of them here:

While a new residential building is erected, the chairs that are to be placed there need to be produced.
In order to be able to plan this, the home buyers indicate the desired position of the armchairs in their home on a floor plan at the time of purchase.
These plans are collected, and the number of different chairs to be produced are counted from them.
The plans are also used to steer the workers carrying the chairs into the building when furnishing the apartments.

In the recent past, when manually counting the various types of chairs in the floor plans,
many mistakes were made and caused great resentment among customers.
That is why the owner of the company asked us to automate this process.

Unfortunately, the plans are in a very old format (the company's systems are still from the eighties),
so modern planning software cannot be used here.
An example of such an apartment plan is attached.

We now need a command line tool that reads in such a file and outputs the following information:
- Number of different chair types for the apartment
- Number of different chair types per room

The different types of chairs are as follows:
W: wooden chair
P: plastic chair
S: sofa chair
C: china chair

The output must look like this so that it can be read in with the old system:

total:   
W: 3, P: 2, S: 0, C: 0   
living room:   
W: 3, P: 0, S: 0, C: 0   
office:   
W: 0, P: 2, S: 0, C: 0   


The names of the rooms must be sorted alphabetically in the output.
