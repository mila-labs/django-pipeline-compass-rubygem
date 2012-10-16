# Django Pipeline Compass

[Compass](http://compass-style.org/) compiler for django-pipeline.

## Requirements

- Compass: `gem install compass`

## Installation

```
pip install git+https://github.com/mila-labs/django-pipeline-compass.git
```

## Usage

```python
# settings.py

PIPELINE_COMPASS_BINARY = '/usr/local/bin/compass' # default: '/usr/bin/env compass'
PIPELINE_COMPASS_ARGUMENTS = '-l myframework'      # default: ''

PIPELINE_COMPILERS = (
  'pipeline_compass.compass.CompassCompiler',
)
```