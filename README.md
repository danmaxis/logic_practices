# Python: Logic pratices

---@

##### Source: [4 Hard Python Questions That Will Probably Take You Days to Solve | Python in Plain English](https://python.plainenglish.io/4-hard-python-questions-that-will-probably-take-you-days-to-solve-15b9cb6d9544)

Each one is under a folder labeled accordingly.

## 1. Largest Puddle

You are given a 2D list of integers.

```
map = [ 
[5, 5, 5, 5, 5, 2, 2], 
[5, 4, 3, 3, 5, 2, 2], 
[5, 3, 5, 3, 5, 2, 2], 
[5, 5, 5, 5, 5, 5, 2], 
[5, 5, 5, 5, 2, 1, 5], 
[5, 3, 2, 5, 1, 4, 5], 
[5, 5, 2, 5, 5, 3, 5] 
]
```

Each coordinate here represents some land, and the number represents the height of the land. If it rains, water flows from higher coordinates to lower coordinates (horizontally and vertically).

Puddles collect when it rains and water cannot flow out of the map. Assume that the map is surrounded by land of height 0, and that water that flows outside of the map is lost and will *not* form a puddle.

<img src="https://miro.medium.com/max/1400/1*xHHOny4mmOCz0m89efeXVQ.png" title="" alt="" width="356">

- The red area is a puddle as water cannot flow out
- The blue area is NOT a puddle, as water can flow out of bounds
- The green area is a puddle as water cannot flow out
- The yellow area is NOT a puddle as water can flow out of bounds
- The pink area is also NOT a puddle as water can flow out of bounds

In our example here, we only have 2 valid puddles — the area circled in red and green.

Our task here would be to write a function `largest_puddle(map)` that takes in a 2D list `map`, and returns the coordinates of the largest puddle on the map. For our above example, this would be our output:

`{(1,1), (2,1), (1,2), (1,3), (2,3)}`

Note that these are the coordinates of the points that are inside the red area.



## 2. Finding Island Coordinates

You are given a 2D list of integers (either 0 or 1)

```
map = [ 
[1,1,0,1,1], 
[1,1,0,0,0], 
[0,0,0,0,0], 
[1,1,1,0,0], 
]
```

1’s are land coordinates, while 0’s are sea coordinates. Land coordinates that are beside one another horizontally or vertically (not diagonally) make up 1 island. In this map, we have 3 distinct islands:

<img src="https://miro.medium.com/max/1386/0*KXExACkEzeMOshPV.jpeg" title="" alt="" width="432">

Write a function `get_islands(map)` that takes in a 2D list `map`, and returns a list of sets. Each set represents 1 island and contains all land coordinates that are inside the island. Example of what should be returned for the above map:

```
[ 
{(0, 1), (1, 0), (0, 0), (1, 1)}, # the top-left island 
{(0, 3), (0, 4)}, # the top-right island 
{(3, 0), (3, 2), (3, 1)} # the bottom-right island 
]
```





## 3. Longest Word Chain

You are given a list of English words:

`words = ["apple", "orange", "tank", "elephant", "kitten"]`

A word chain is a list of English words where the last letter of each word is equal to the first letter of the next word. For instance:

- `["apple", "elephant"]` is a valid word chain
- `["tank", "kitten"]` is a valid word chain
- `["elephant", "apple"]` is not a valid word chain as `"apple"` does not begin with `"t"`
- `["apple", "kitten"]` is not a valid word chain as `"kitten"` does not begin with `"e"`

Write a function `longest_word_chain(words)` that takes in a list of English words `words`, and returns the longest possible valid word chain. For the example above, the longest possible valid word chain is:

`["apple", "elephant", "tank", "kitten"]`

Or:

`["orange", "elephant", "tank", "kitten"]`



## 4. Hollow Diamond

Write a function `hollow_diamond(string)` that takes in a string `string`, and prints the following pattern:

```
string = "abcdefgh"
  a
 b h
c   g
 d f
  e
```

If there are insufficient characters to form a perfect hollow diamond shape, append your string with `*` characters.

```
string = "abcdefghij"
   a
  b *
 c   *
d     j
 e   i
  f h
   g
```

Another example:

```
string = "abcdefghijklmnop"
    a
   b p
  c   o
 d     n
e       m
 f     l
  g   k
   h j
    i
```

Yet another example:

```
string = "abcdefghijklmn"
    a
   b *
  c   *
 d     n
e       m
 f     l
  g   k
   h j
    i
```


