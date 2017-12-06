# import-finder
Determine top-level imports in a python package

## How To

### Example Usage

```bash
ag --python --noheading --nonumbers --nofilename <search_term> | import_finder
```

Just the top-level packages

```bash
^same | awk -F '.' '{print $1}'
```
