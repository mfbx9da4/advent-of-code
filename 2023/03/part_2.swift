import Foundation

let inputPath = FileManager.default.currentDirectoryPath + "/input.txt"
let inputUrl = URL(fileURLWithPath: inputPath)
let inputString = try String(contentsOf: inputUrl, encoding: .utf8)
let inputArray = inputString.components(separatedBy: "\n")

print("Input:", inputString)

// 467..114..
// ...*......
// ..35..633.
// ......#...
// 617*......
// .....+.58.
// ..592.....
// ......755.
// ...$.*....
// .664.598..

var board = [[Character]]()

for line in inputArray {
    var row = [Character]()
    for char in line {
        row.append(char)
    }
    board.append(row)
}


// 1. Find all the numbers
// 2. Iterate through each number -> keep or not?
// 3. Skip iterated numbers


struct Node: Hashable {
    var number: Int
    var row: Int
    var column: Int
    var length: Int

    func isNeighborOf(r: Int, c: Int) -> Bool {
        for (r2, c2) in neighbors() {
            if r2 == r && c2 == c {
                return true
            }
        }
        return false
    }

    func neighbors() -> [(Int, Int)] {
        // Get all the neighbouring cells of the node
        var result = [(Int, Int)]()
        // Left column
        result.append((row - 1, column - 1))
        result.append((row, column - 1))
        result.append((row + 1, column - 1))
        // Right column
        result.append((row - 1, column + length))
        result.append((row, column + length))
        result.append((row + 1, column + length))
        // Top row
        for i in 0..<length {
            result.append((row - 1, column + i))
        }
        // Bottom row
        for i in 0..<length {
            result.append((row + 1, column + i))
        }
        // Filter out of bounds
        return result.filter { $0.0 >= 0 && $0.0 < board.count && $0.1 >= 0 && $0.1 < board[$0.0].count }
    }
}


// 1. Find all the numbers
var nodes = Set<Node>()
for r in 0..<board.count {
    var currentNumber = ""
    for c in 0..<board[r].count {
        let char = board[r][c]
        if char.isNumber {
            currentNumber += String(char)
        } else {
            if currentNumber.count > 0 {
                nodes.insert(Node(number: Int(currentNumber)!, row: r, column: c - currentNumber.count, length: currentNumber.count))
            }
            currentNumber = ""
        }
    }
    if currentNumber.count > 0 {
        nodes.insert(Node(number: Int(currentNumber)!, row: r, column: board[r].count - currentNumber.count, length: currentNumber.count))
    }
}


// 2. Iterate through each number
var sum = 0
while nodes.count > 0 {
    let node = nodes.removeFirst()
    
    // 3.a Find a neighbouring *
    for (r, c) in node.neighbors() {
        if board[r][c] == "*" {
            // 3.b If there is a neighbouring *, find if any of the neighbours of the * is a number
            for node2 in nodes {
                if node2.isNeighborOf(r: r, c: c) {
                    // 3.c If there is a neighbouring number -> mark seen and add (number1 * number2) to sum
                    sum += node.number * node2.number
                    nodes.remove(node2)
                    break
                }
            }
        }
    }
}
print(sum)

