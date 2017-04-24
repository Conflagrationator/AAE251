# AAE251
Analysis code for the AAE 251 Final Project

## To Do

- Write Rocket Analysis Code
- Write Airplane Analysis Code
- Make Plotting Suite

## Style Guidelines
To help keep the code readable between ourselves I propose the following guidelines for the file structure and code look.

- Keep Imports at the top
- Delimit major sections with title blocks
- Major subsections are capitalized
- Minor subsections are camel capitalized

```python
################################################################################
# PLOTTING
################################################################################

# FIRST TEST SUITE

# First Test
```

- Comment Sections of code that have a unified purpose (like before a for loop)
- Comments of functionality are lowercase
- Comment `if`, `elif` and `else` statements with how we should interpret them
- Name functions descriptively (it doesn't matter if they're long names, you have editors which can autofill)
- Provide Function helper comments that state the inputs & outputs (that's the three quotation mark comment immediately after a function `def` header line) if the function name is not descriptive enough
- Write Functions in a functional way. Namely that they have no side-effects, 
and if you input the same thing, they will always output the same thing.
- Functions should do only 1 thing
- Modularize multi-step algorithms into many functions
- Organize Different Analyses into different files and import into other's as necessary
- Keep code below 80 lines as well as possible
- Write all code to be in SI, then use the conversion module to convert only as the very first and last steps
- If you write a section of code that has a likelyhood of breaking, write an exception for it so we know where to go and look for the error. use `raise Exception("message")`
- Camel Capitalize Function Names (no underscores)
- For any Hard-Coded Numbers, write the unit as first comment after it: `stuff # unit # any more comments`
- Use subscripts for things that are unambiguously and necessarily subscripts (example: `f_inert`)
