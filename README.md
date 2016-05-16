# Python Druuid

A python implementation of a date-realtive (and relatively universally unique)
UUID generator. It is based on the [original][1] implementation in Ruby.

## Concept

Druuid's are a 64 bit identifiers which are sortable since they are time based.
A druuid is compromised of 2 blocks:
* 41-bit timestamp in miliseconds since epoch
* 23 random bits

For example, a druuid generated on 2016-05-16 might look like
`12276209757600130011`.

In binary: `10101010010111011101101110111011011111011 11100001010001111011011`

In base 36: `2L9OH62W41ES0`

## Examples

```
>>> from druuid import Druuid
>>>
>>> d = Druuid()
>>> d.druuid
12276209757600130011
>>> d.time
'Mon May 16 15:37:23 2016'
>>>
>>> d = Druuid(12276215031090144168)
>>> d.time
'Mon May 16 15:47:52 2016'
```

[1]: https://github.com/recurly/druuid
