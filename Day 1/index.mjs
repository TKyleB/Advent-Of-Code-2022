import { open } from 'node:fs/promises';

class Elf {
    constructor(food) {
        this.food = food
    }

    get totalCalories() {
        return this.calculateCalories();
    }

    calculateCalories() {
        return this.food.reduce((partialSum, a) => parseInt(partialSum) + parseInt(a), 0)
    }

}

let elfList = []
let currentFood = []

async function getElveData() {
    const file = await open('./Day 1/names.txt');

    for await (const line of file.readLines()) {

        if (line == "") {
            elfList.push(new Elf(currentFood));
            currentFood = [];
            continue;
        }
        currentFood.push(line);
    }
}

function getTopThreeCalories(elves) {
    let sum = 0
    let topThree = elves.slice(-3)
    for (let elve of topThree) {
        sum += elve.totalCalories
    }
    return sum
}


await getElveData();

//Sort List from lowest to highest
elfList.sort((a, b) => a.totalCalories - b.totalCalories)

console.log(`The highest calorie elf has : ${elfList[elfList.length - 1].totalCalories} caloires`)
console.log(`The top three calorie elves total ${getTopThreeCalories(elfList)}`)

