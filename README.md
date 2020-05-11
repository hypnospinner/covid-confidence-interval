# Confidence interval solution

Program pics data from CSV table, takes from user list of countries one wishes to observe & outputs the result as `pandas` `DataFrame`

> BUG: program can't handle countries which have name that consists from 2 or more words like `United States`

Example:

```
Input: Australia Russia Kazakhstan Kenya

Output:
      Country      Mean                           Confidence interval
0   Australia  0.011483  (0.010577445812364004, 0.012388651852987143)
1      Russia  0.028599    (0.02823757406324443, 0.02896087902522122)
2  Kazakhstan  0.013049  (0.011707046102459966, 0.014390207876552003)
3       Kenya  0.018247   (0.01352172529000852, 0.022972607029593355)
```

Note that not all countries have data on picked date (1st of May) so error can occur.
