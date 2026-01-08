type Direction = "left" | "right" | "up" | "down"

function move(direction: Direction): void {
  console.log("Moving:", direction)
}

// --------------------
// WORKING CODE
// --------------------

const d1 = "left"
move(d1)

let d2: Direction = "up"
move(d2)

const d3 = "down" as const
move(d3)

// --------------------
// NON-WORKING CODE (COMMENTED)
// --------------------

// const d4 = "forward"
// move(d4) // Error: not assignable to Direction

// let d5 = "left"
// move(d5) // Error: inferred as string

console.warn("Literals - 05")
