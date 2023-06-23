# Linear model

``` python
import numpy as np
import polars as pl
import statsmodels.api as sm
import statsmodels.formula.api as smf
from marginaleffects import comparisons, predictions

df = sm.datasets.get_rdataset("Guerry", "HistData").data
mod = smf.ols("Literacy ~ Pop1831 * Desertion", df)
fit = mod.fit()
```

# `comparisons()`

## Difference

``` python
comparisons(fit, variables = "Pop1831", value = 1, comparison = "differenceavg")
```

<small>shape: (1, 5)</small>

| estimate | std_error | statistic | conf_low  | conf_high |
|----------|-----------|-----------|-----------|-----------|
| f64      | f64       | f64       | f64       | f64       |
| 0.003717 | 0.011597  | 0.320485  | -0.019353 | 0.026786  |


``` python
comparisons(fit, variables = "Pop1831", value = 1, comparison = "difference").head()
```

<small>shape: (5, 28)</small>

| estimate  | std_error | statistic | conf_low  | conf_high | dept | Region | Department     | Crime_pers | Crime_prop | Literacy | Donations | Infants | Suicides | MainCity | Wealth | Commerce | Clergy | Crime_parents | Infanticide | Donation_clergy | Lottery | Desertion | Instruction | Prostitutes | Distance | Area | Pop1831 |
|-----------|-----------|-----------|-----------|-----------|------|--------|----------------|------------|------------|----------|-----------|---------|----------|----------|--------|----------|--------|---------------|-------------|-----------------|---------|-----------|-------------|-------------|----------|------|---------|
| f64       | f64       | f64       | f64       | f64       | i64  | str    | str            | i64        | i64        | i64      | i64       | i64     | i64      | str      | i64    | i64      | i64    | i64           | i64         | i64             | i64     | i64       | i64         | i64         | f64      | i64  | f64     |
| -0.009946 | 0.013663  | -0.727936 | -0.037126 | 0.017234  | 1    | "E"    | "Ain"          | 28870      | 15890      | 37       | 5098      | 33120   | 35039    | "2:Med"  | 73     | 58       | 11     | 71            | 60          | 69              | 41      | 55        | 46          | 13          | 218.372  | 5762 | 346.03  |
| -0.042023 | 0.025143  | -1.671333 | -0.092041 | 0.007995  | 2    | "N"    | "Aisne"        | 26226      | 5521       | 51       | 8901      | 14572   | 12831    | "2:Med"  | 22     | 10       | 82     | 4             | 82          | 36              | 38      | 82        | 24          | 327         | 65.945   | 7369 | 513.0   |
| 0.036388  | 0.018517  | 1.965047  | -0.000449 | 0.073225  | 3    | "C"    | "Allier"       | 26747      | 7925       | 13       | 10973     | 17044   | 114121   | "2:Med"  | 61     | 66       | 68     | 46            | 42          | 76              | 66      | 16        | 85          | 34          | 161.927  | 7340 | 298.26  |
| 0.017379  | 0.012825  | 1.355129  | -0.008133 | 0.042891  | 4    | "E"    | "Basses-Alpes" | 12935      | 7289       | 46       | 2733      | 23018   | 14238    | "1:Sm"   | 76     | 49       | 5      | 70            | 12          | 37              | 80      | 32        | 29          | 2           | 351.399  | 6925 | 155.9   |
| 0.013815  | 0.012195  | 1.132804  | -0.010445 | 0.038075  | 5    | "E"    | "Hautes-Alpes" | 17488      | 8174       | 69       | 6962      | 23076   | 16171    | "1:Sm"   | 83     | 65       | 10     | 22            | 23          | 64              | 79      | 35        | 7           | 1           | 320.28   | 5549 | 129.1   |


## Ratio

``` python
comparisons(fit, variables = "Pop1831", value = 1, comparison = "ratioavg")
```

<small>shape: (1, 5)</small>

| estimate | std_error | statistic   | conf_low | conf_high |
|----------|-----------|-------------|----------|-----------|
| f64      | f64       | f64         | f64      | f64       |
| 1.000255 | 0.00033   | 3029.838358 | 0.999598 | 1.000911  |


``` python
comparisons(fit, variables = "Pop1831", value = 1, comparison = "ratio").head()
```

<small>shape: (5, 28)</small>

| estimate | std_error | statistic   | conf_low | conf_high | dept | Region | Department     | Crime_pers | Crime_prop | Literacy | Donations | Infants | Suicides | MainCity | Wealth | Commerce | Clergy | Crime_parents | Infanticide | Donation_clergy | Lottery | Desertion | Instruction | Prostitutes | Distance | Area | Pop1831 |
|----------|-----------|-------------|----------|-----------|------|--------|----------------|------------|------------|----------|-----------|---------|----------|----------|--------|----------|--------|---------------|-------------|-----------------|---------|-----------|-------------|-------------|----------|------|---------|
| f64      | f64       | f64         | f64      | f64       | i64  | str    | str            | i64        | i64        | i64      | i64       | i64     | i64      | str      | i64    | i64      | i64    | i64           | i64         | i64             | i64     | i64       | i64         | i64         | f64      | i64  | f64     |
| 0.999769 | 0.000315  | 3176.733532 | 0.999143 | 1.000395  | 1    | "E"    | "Ain"          | 28870      | 15890      | 37       | 5098      | 33120   | 35039    | "2:Med"  | 73     | 58       | 11     | 71            | 60          | 69              | 41      | 55        | 46          | 13          | 218.372  | 5762 | 346.03  |
| 0.999044 | 0.000647  | 1544.357883 | 0.997758 | 1.000331  | 2    | "N"    | "Aisne"        | 26226      | 5521       | 51       | 8901      | 14572   | 12831    | "2:Med"  | 22     | 10       | 82     | 4             | 82          | 36              | 38      | 82        | 24          | 327         | 65.945   | 7369 | 513.0   |
| 1.001225 | 0.000675  | 1484.291758 | 0.999883 | 1.002567  | 3    | "C"    | "Allier"       | 26747      | 7925       | 13       | 10973     | 17044   | 114121   | "2:Med"  | 61     | 66       | 68     | 46            | 42          | 76              | 66      | 16        | 85          | 34          | 161.927  | 7340 | 298.26  |
| 1.000529 | 0.000434  | 2306.440576 | 0.999666 | 1.001391  | 4    | "E"    | "Basses-Alpes" | 12935      | 7289       | 46       | 2733      | 23018   | 14238    | "1:Sm"   | 76     | 49       | 5      | 70            | 12          | 37              | 80      | 32        | 29          | 2           | 351.399  | 6925 | 155.9   |
| 1.000405 | 0.000393  | 2545.67391  | 0.999624 | 1.001187  | 5    | "E"    | "Hautes-Alpes" | 17488      | 8174       | 69       | 6962      | 23076   | 16171    | "1:Sm"   | 83     | 65       | 10     | 22            | 23          | 64              | 79      | 35        | 7           | 1           | 320.28   | 5549 | 129.1   |


## Group averages (SEs are broken)

``` python
comparisons(fit, variables = "Pop1831", value = 1, comparison = "difference", by = "Region")
```

    /home/vincent/repos/pymarginaleffects/marginaleffects/comparisons.py:47: UserWarning: vcov is set to False because `by` or `hypothesis` is not None
      warn("vcov is set to False because `by` or `hypothesis` is not None")

<small>shape: (6, 2)</small>

| Region | estimate  |
|--------|-----------|
| str    | f64       |
| "E"    | -0.011623 |
| "N"    | -0.004984 |
| "C"    | 0.017379  |
| "S"    | 0.021782  |
| "W"    | -0.006382 |
| null   | 0.044704  |


# `predictions()`

``` python
predictions(fit).head()
```

<small>shape: (5, 28)</small>

| estimate  | std_error | statistic | conf_low  | conf_high | dept | Region | Department     | Crime_pers | Crime_prop | Literacy | Donations | Infants | Suicides | MainCity | Wealth | Commerce | Clergy | Crime_parents | Infanticide | Donation_clergy | Lottery | Desertion | Instruction | Prostitutes | Distance | Area | Pop1831 |
|-----------|-----------|-----------|-----------|-----------|------|--------|----------------|------------|------------|----------|-----------|---------|----------|----------|--------|----------|--------|---------------|-------------|-----------------|---------|-----------|-------------|-------------|----------|------|---------|
| f64       | f64       | f64       | f64       | f64       | i64  | str    | str            | i64        | i64        | i64      | i64       | i64     | i64      | str      | i64    | i64      | i64    | i64           | i64         | i64             | i64     | i64       | i64         | i64         | f64      | i64  | f64     |
| 42.992617 | 1.965112  | 21.877945 | 39.083383 | 46.901852 | 1    | "E"    | "Ain"          | 28870      | 15890      | 37       | 5098      | 33120   | 35039    | "2:Med"  | 73     | 58       | 11     | 71            | 60          | 69              | 41      | 55        | 46          | 13          | 218.372  | 5762 | 346.03  |
| 43.954782 | 4.570692  | 9.616657  | 34.862219 | 53.047345 | 2    | "N"    | "Aisne"        | 26226      | 5521       | 51       | 8901      | 14572   | 12831    | "2:Med"  | 22     | 10       | 82     | 4             | 82          | 36              | 38      | 82        | 24          | 327         | 65.945   | 7369 | 513.0   |
| 29.729568 | 2.744031  | 10.834267 | 24.270815 | 35.188321 | 3    | "C"    | "Allier"       | 26747      | 7925       | 13       | 10973     | 17044   | 114121   | "2:Med"  | 61     | 66       | 68     | 46            | 42          | 76              | 66      | 16        | 85          | 34          | 161.927  | 7340 | 298.26  |
| 32.891659 | 3.25552   | 10.103351 | 26.415393 | 39.367925 | 4    | "E"    | "Basses-Alpes" | 12935      | 7289       | 46       | 2733      | 23018   | 14238    | "1:Sm"   | 76     | 49       | 5      | 70            | 12          | 37              | 80      | 32        | 29          | 2           | 351.399  | 6925 | 155.9   |
| 34.085588 | 3.417628  | 9.973463  | 27.286836 | 40.884339 | 5    | "E"    | "Hautes-Alpes" | 17488      | 8174       | 69       | 6962      | 23076   | 16171    | "1:Sm"   | 83     | 65       | 10     | 22            | 23          | 64              | 79      | 35        | 7           | 1           | 320.28   | 5549 | 129.1   |


## Group averages (SEs are broken)

``` python
predictions(fit, by = "Region")
```

<small>shape: (6, 6)</small>

| Region | estimate  | std_error | statistic | conf_low  | conf_high |
|--------|-----------|-----------|-----------|-----------|-----------|
| str    | f64       | f64       | f64       | f64       | f64       |
| "E"    | 43.892679 | 2.043144  | 21.482912 | 39.828215 | 47.957143 |
| "N"    | 41.974184 | 2.363304  | 17.760806 | 37.27282  | 46.675549 |
| "C"    | 35.693435 | 1.982075  | 18.008115 | 31.750456 | 39.636414 |
| "S"    | 33.82303  | 2.215093  | 15.269351 | 29.416505 | 38.229555 |
| "W"    | 41.871616 | 1.856515  | 22.553884 | 38.178417 | 45.564815 |
| null   | 22.66595  | 4.51115   | 5.024429  | 13.691836 | 31.640064 |


# `hypothesis` argument

``` python
hyp = np.array([1, 0, -1, 0, 0, 0])
predictions(fit, by = "Region", hypothesis = hyp)

hyp = np.vstack([
    [1, 0, -1, 0, 0, 0],
    [1, 0, 0, -1, 0, 0]
]).T
predictions(fit, by = "Region", hypothesis = hyp)
```

<small>shape: (2, 6)</small>

| term       | estimate  | std_error | statistic | conf_low | conf_high |
|------------|-----------|-----------|-----------|----------|-----------|
| str        | f64       | f64       | f64       | f64      | f64       |
| "column_0" | 8.199244  | 1.804968  | 4.542598  | 4.608588 | 11.789899 |
| "column_1" | 10.069649 | 2.214312  | 4.54753   | 5.664678 | 14.47462  |


Which corresponds to:

``` python
p = predictions(fit, by = "Region")
print(p["estimate"][0] - p["estimate"][2])
print(p["estimate"][0] - p["estimate"][3])
```

    8.199243639851169
    10.069648968961637

``` python
predictions(fit, by = "Region", hypothesis = "reference")
```

<small>shape: (5, 6)</small>

| term            | estimate   | std_error | statistic | conf_low   | conf_high  |
|-----------------|------------|-----------|-----------|------------|------------|
| str             | f64        | f64       | f64       | f64        | f64        |
| "Row 2 - Row 1" | -1.918495  | 2.079076  | -0.922763 | -6.054439  | 2.21745    |
| "Row 3 - Row 1" | -8.199244  | 1.804968  | -4.542598 | -11.789899 | -4.608588  |
| "Row 4 - Row 1" | -10.069649 | 2.214312  | -4.54753  | -14.47462  | -5.664678  |
| "Row 5 - Row 1" | -2.021063  | 1.065328  | -1.897128 | -4.140339  | 0.098213   |
| "Row 6 - Row 1" | -21.226729 | 4.989687  | -4.25412  | -31.152806 | -11.300651 |

