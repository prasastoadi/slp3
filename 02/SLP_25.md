2.5 Figure out whether _drive_ is closer to _brief_ or to _divers_ and what the edit distance is to each. You may use any version of distance that you like

Using insertion cost 1, deletion cost 1, substitution cost 2.


|   |   | d | r | i | v | e |
|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 |
| **b** | 1 | 2 | 3 | 4 | 5 | 6 |
| **r** | 2 | 3 | 2 | 3 | 4 | 5 |
| **i** | 3 | 4 | 3 | 2 | 3 | 4 |
| **e** | 4 | 5 | 4 | 3 | 4 | 3 |
| **f** | 5 | 6 | 5 | 4 | 5 | 4 |


|   |   | d | r | i | v | e |
|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 |
| **d** | 1 | 0 | 1 | 2 | 3 | 4 |
| **i** | 2 | 1 | 2 | 1 | 2 | 3 |
| **v** | 3 | 2 | 3 | 2 | 1 | 2 |
| **e** | 4 | 3 | 4 | 3 | 2 | 1 |
| **r** | 5 | 4 | 3 | 4 | 3 | 2 |
| **s** | 6 | 5 | 4 | 5 | 4 | 3 |
