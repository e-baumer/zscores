# zscores
<!--[![Build Status]()]()-->


A zscore calculator for the evaluation of children growth status using the three most commonly used anthropomorphic indices: Weight-for-height (WFH), Height-for-age (HFA), and Weight-for-Age (WFA)

## Overview

A calculator to determine the zscore of the following child growth indicators:

    - Weight-for-height (WFH)
    - Weight-for-length (WFL)
    - Weight-for-age (WFA)
    - Height-for-age (HFA)
    - Length-for-age (LFA)

Zscore tables have been compiled by the World Health Organization (WHO). Length should be used
in place of height for children <= 2 years old.

Calculation of the zscore is done using L, M, S, parameters based on:

_Cole, T.J. and Green, P.J., 1992. Smoothing reference centile curves: the LMS method and
penalized likelihood. Statistics in medicine, 11(10), pp.1305-1319._

See docs for reference.

## Example Use

Imports

```
from zscore_finder import ZScores
```

Initialize the class. During initialization specify the directory of the zscore tables. The zscore
tables have default file names. Use the file_nameis parameter to overwrite any of the default
file names.
```
test_scores = ZScores('/path/to/zscore/tables')
```

Now we can calculate actual zscores. For example, we want to calculate the zscore of weight for age
of a male child (age = 23 months, weight = 11 kg):
```
test_scores.z_score(gender=1, measure='wfa', weight=11, age=23)
>>> -0.73
```
