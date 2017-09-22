Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/165598015/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
set [new month v] to [0]

set [original month v] to (answer)

set [months to add v] to (answer)

set [new month v] to (((original month) + (months to add)) mod (12))
```

```scratch:split:random
ask [Type in a number betweem 1 and 12 for a month of the year:] and wait

ask [Enter the number of months to add to the month:] and wait
```

```scratch:split:random
say (join (join (months to add) (join [ months after ] (item (original month) of [months v] :: list))) [ is December. ])

say (join (join (join (join (months to add) (join [ months after ] (item (original month) of [months v] :: list))) [ is ]) (item (new month) of [months v] :: list)) [.])
```

```scratch:split:random
if <(new month) = [0]> then
else
end
```

{panel end}
