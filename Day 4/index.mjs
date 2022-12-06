import { open } from 'node:fs/promises';

const file = await open("./Day 4/input.txt")
let overlap = 0

for await (const line of file.readLines()) {
   let pair = line.split(",")
   let firstSet = pair[0].split("-").map((num) => parseInt(num))
   let secondSet = pair[1].split("-").map((num) => parseInt(num))
   const pairOneRange = generateRange(firstSet[0], firstSet[1])
   const pairTwoRange = generateRange(secondSet[0], secondSet[1])
   
   if (pairOneRange.includes(pairTwoRange[0]) || pairOneRange.includes(pairTwoRange[pairTwoRange.length - 1])) overlap += 1
   else if (pairTwoRange.includes(pairOneRange[0]) || pairTwoRange.includes(pairOneRange[pairOneRange.length - 1])) overlap += 1
}
console.log(overlap)

function generateRange(start, end) {
    let array = []
    for (let i = start; i <= end; i++) {
        array.push(parseInt(i))
    }
    return array
}


