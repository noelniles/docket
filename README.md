## Law Docket Explorer

*requirements are listed in requirements.txt*


### How to Test It
1. Clone it.
2. `$ cd docket`
3. Install dependencies with pip: `pip install -r requirements.txt`
4. run `nosetests`

#### Output from nostests should be something like this
```
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```

### How to Use the Command Line Interface
1. `$ cd docket` or whatever directory you cloned into

   **All Commands Should be Run From Same Directory as the README file**
    ```
    $ ls -l
    total 164
    drwxrwxr-x 1 me me     0 Jun 26 14:50 bin
    -rw-rw-r-- 1 me me 35147 Jun 27 13:04 COPYING
    drwxrwxr-x 1 me me  1384 Jun 27 14:25 docket
    -rw-rw-r-- 1 me me  1367 Jun 26 17:05 docket.ipynb
    drwxrwxr-x 1 me me     0 Jun 26 14:50 docs
    drwxrwxr-x 1 me me  2152 Jun 26 21:27 law_data
    -rw-rw-r-- 1 me me   701 Jun 27 14:58 README.md
    -rw-rw-r-- 1 me me    26 Jun 26 15:08 requirements.txt
    -rw-rw-r-- 1 me me  1173 Jun 27 13:02 setup.py
    -rw-rw-r-- 1 me me 64341 Jun 26 21:25 testdoc.xml
    drwxrwxr-x 1 me me   920 Jun 27 13:12 tests
    drwxrwxr-x 1 me me   712 Jun 26 14:50 venv
    ```

2. run `$ python -m <options> <params>`
  
##### current usages
  - `python -m docket tag-set` returns a the set of all tags
  - `python -m docket grab <tag>` grabs all the text associated with tag
  - `python -m docket grab-many <tag1> <tag2> ... <tagN>` grabs many tags
