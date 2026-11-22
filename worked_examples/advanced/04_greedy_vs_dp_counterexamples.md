# Worked example A4 · Let the computer find the counterexample

**Problem.** A greedy rule is tempting for "fewest coins". Instead of arguing in circles, search small inputs automatically for a case where greedy loses, and fall back to DP.

## 1. Plan

1. Write the greedy rule.
2. Write an obviously-correct DP oracle.
3. Enumerate small coin systems and amounts until they disagree.

## 2. The tempting rule

```python
def greedy_coins(coins, amount):
    used = 0
    for c in sorted(coins, reverse=True):
        used += amount // c
        amount %= c
    return used if amount == 0 else None

print(greedy_coins([1, 5, 10, 25], 63), greedy_coins([1, 3, 4], 6))
```

<!-- output -->
```text
6 3
```
<!-- /output -->

## 3. The DP oracle and an automatic search

```python
def dp_coins(coins, amount):
    best = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                best[a] = min(best[a], best[a - c] + 1)
    return best[amount] if best[amount] != float("inf") else None

def first_counterexample(max_coin=6, max_amount=20):
    from itertools import combinations
    for size in (2, 3):
        for others in combinations(range(2, max_coin + 1), size - 1):
            coins = (1,) + others
            for amount in range(1, max_amount + 1):
                if greedy_coins(coins, amount) != dp_coins(coins, amount):
                    return coins, amount, greedy_coins(coins, amount), dp_coins(coins, amount)
    return None

print(first_counterexample())
```

<!-- output -->
```text
((1, 3, 4), 6, 3, 2)
```
<!-- /output -->

The smallest failing system is found in milliseconds: greedy takes `4 + 1 + 1` for 6 with coins (1, 3, 4), while `3 + 3` uses two coins.

## 4. Which systems are safe?

Systems where greedy is always optimal are called *canonical*. A known result: if greedy fails, it fails below `c_{n-1} + c_n` (the sum of the two largest coins), so a bounded check suffices:

```python
def is_canonical(coins):
    coins = sorted(coins)
    limit = coins[-1] + (coins[-2] if len(coins) > 1 else 0)
    return all(greedy_coins(coins, a) == dp_coins(coins, a) for a in range(1, limit + 1))

for system in ([1, 5, 10, 25], [1, 3, 4], [1, 2, 5, 10, 20, 50], [1, 7, 10]):
    print(system, is_canonical(system))
```

<!-- output -->
```text
[1, 5, 10, 25] True
[1, 3, 4] False
[1, 2, 5, 10, 20, 50] True
[1, 7, 10] False
```
<!-- /output -->

The lesson: when an exchange argument doesn't come easily, a 10-line exhaustive search is the fastest way to find out whether there's anything to prove.

**Practise next:** drills `DI36`, `DA14`; interview problem `A07`.
