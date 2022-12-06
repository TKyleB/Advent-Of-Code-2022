import { open } from 'node:fs/promises';

const file = await open("./Day 3/input.txt")
let result = 0;
let count = 0
let currentString = ""
for await (const line of file.readLines()) {
    if (count == 3){
        let duplicates = getDuplicates(currentString)
        result += getCharacterValue(duplicates)
        currentString = ""
        count = 0
    }
    new Set(line).forEach(char => currentString += char)
    count++   
}

console.log(result)

function getDuplicates(string) {
    let chars = {}
    for (let c of string) {
        chars[c] ? chars[c] = chars[c] + 1 : chars[c]= 1
    }
    return Object.entries(chars).filter(char => char[1] >= 3).map(char => char[0]).toString()
}

function getCharacterValue(char) {
    if (char == char.toUpperCase()) return char.charCodeAt(0) - 38
    if (char == char.toLowerCase()) return char.charCodeAt(0) - 96
}




