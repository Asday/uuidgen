# `bytegen`

Bytegen and its brothers aim to make use of as much entropy as `os.urandom()` can provide.  They do this, much like `uuidgen()` and `urandomgen()`, in having domain knowledge.

The list of allowed characters (ascii uppercase and numbers) is of length 36.  No product of 36 and an integer ever equals 2<sup>n</sup>, so it is not possible to interpret an arbitrary binary sequence as a string of allowed characters.  Instead, each 6 bits, (64 possibilities), must be interpreted as an index to the string of allowed characters, repeated at the end.  `0x00 == 'A'`, `0x24 == 'A'`, and so on.

To avoid crushing entropy by making `'2'` to `'9'` slightly less likely to appear in the generated string, each subsequent character must begin "counting" from where the last character's loop was cut off.  If `0x40` would be `'2'` for character `n`, that means `0x00` would be `'2'` for character `n+1`.

This pattern has a period of 9 cycles, or 576 characters, meaning any generated string of length not divisible by 9 will have slightly less entropy.  This could be avoided by carrying on the pattern from the previous run, and randomising the start index, at the cost of execution time.

```
  0
  x
  0000000000000000111111111111111122222222222222223333333333333333
  0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  ----------------------------------------------------------------
0 ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ01
1 23456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRST
2 UVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKL
3 MNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCD
4 EFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ012345
5 6789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWX
6 YZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOP
7 QRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGH
8 IJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
```
