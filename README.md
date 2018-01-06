# import-finder
Determine top-level imports in a python package

## How To

### Example Usage

```bash
ag --python --noheading --nonumbers --nofilename import | import_finder | sort | uniq
```

Just the top-level packages

```bash
ag --python --noheading --nonumbers --nofilename import | import_finder | awk -F '.' '{print $1}' | sort | uniq
```
