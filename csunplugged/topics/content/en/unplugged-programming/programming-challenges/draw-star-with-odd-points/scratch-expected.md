Click on the green flag to see the expected output of your program.

{iframe link="https://scratch.mit.edu/projects/embed/153925156/?autostart=false"}

{panel type="help" title="Recommended blocks"}

```scratch:split:random
when green flag clicked
```

```scratch:split:random
clear

pen down

pen up
```

```scratch:split:random
ask [Enter an odd number of points to draw a star:] and wait

repeat (points)
end

set [points v] to (answer)
```

```scratch:split:random
go to x: (0) y: (0)

move (200) steps

turn cw ((180) - ((180) / (points))) degrees
```

{panel end}
