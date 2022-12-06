import { open } from 'node:fs/promises';

const file = await open("./Day 2/input.txt")
let totalScore = 0

for await (const line of file.readLines()) {
    const turn = line.split(" ")
    const opponentMove = turn[0]
    const desiredResult = turn[1]

    const calculatedMove = determineMove(opponentMove, desiredResult)
    totalScore += calculateMoveValue(calculatedMove)
    totalScore += calculateResultScore(opponentMove, calculatedMove)

}

console.log(totalScore)

function calculateMoveValue(yourMove) {
    switch (yourMove) {
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3
    }
}

function calculateResultScore(opponentMove, yourMove) {
    let translatedMove
    if (yourMove == "X" || yourMove == "Y" || yourMove == "Z") translatedMove = translatedMove(yourMove)
    else translatedMove = yourMove
    
    // Its a draw
    if (opponentMove == translatedMove) return 3

    // Win Conditions
    else if (opponentMove == "A" && translatedMove == "B") return 6
    else if (opponentMove == "B" && translatedMove == "C") return 6
    else if (opponentMove == "C" && translatedMove == "A") return 6

    // Else Lose
    else return 0
}

function translateYourMove(yourMove) {
    switch (yourMove) {
        case "X":
            return "A"
        case "Y":
            return "B"
        case "Z":
            return "C"
    }
}

function determineMove(opponentMove, desiredResult) {
    // Draw, return same move
    if (desiredResult == "Y") return opponentMove

    // You want to lose
    if (desiredResult == "X" && opponentMove == "A") return "C"
    if (desiredResult == "X" && opponentMove == "B") return "A"
    if (desiredResult == "X" && opponentMove == "C") return "B"

    // You want to win
    if (desiredResult == "Z" && opponentMove == "A") return "B"
    if (desiredResult == "Z" && opponentMove == "B") return "C"
    if (desiredResult == "Z" && opponentMove == "C") return "A"
}


