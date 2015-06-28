## Law Docket Explorer

*requirements are listed in requirements.txt*


### How to Test It
1. Clone it.
2. `cd docket`
3. Install dependencies with pip: `pip install -r requirements.txt`
4. run `nosetests`

#### ouput should be something like this
```
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```
5. That's it.

### How to Use the Command Line Interface
1. `cd docket`
2. `run `python -m <options> <params>`
  
##### current usages
  - `python -m docket tag-set` returns a the set of all tags
  - `python -m docket grab <tag>` grabs all the text associated with tag
  - `python -m docket grab-many <tag1> <tag2> ... <tagN>` grabs many tags
