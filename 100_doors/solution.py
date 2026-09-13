def open_doors(num_doors: int) -> str:
    doors = ["#"] * num_doors
    num_passes = num_doors
    for i in range(1, num_passes + 1):
        j = i - 1
        while (j < num_doors):
            doors[j] = "@" if doors[j] == "#" else "#"
            j += i
    return "".join(doors)
            