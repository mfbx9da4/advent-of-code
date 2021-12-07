//
//  4.swift
//  adventofcode
//
//  Created by David Adler on 07/12/2021.
//

import Foundation


struct Board {
    var vals: [[Int]] = []
    var marked: [[Bool]] = [
        [false, false, false, false, false],
        [false, false, false, false, false],
        [false, false, false, false, false],
        [false, false, false, false, false],
        [false, false, false, false, false]
    ]
    
    var score: Int {
        var sum = 0
        for row in 0...4 {
            for col in 0...4 {
                if marked[row][col] == false {
                    sum = sum + vals[row][col]
                }
            }
        }
        return sum
    }
    
    var isBingo: Bool {
        for row in 0...4 {
            var fullRow = true
            for col in 0...4 {
                if marked[row][col] == false {
                    fullRow = false
                    break
                }
            }
            if fullRow {
                return true
            }
            
        }
        for col in 0...4 {
            var fullCol = true
            for row in 0...4 {
                if marked[row][col] == false {
                    fullCol = false
                    break
                }
            }
            if fullCol {
                return true
            }
        }
        return false
    }
    
    mutating func mark(_ x: Int) {
        for row in 0...4 {
            for col in 0...4 {
                if vals[row][col] == x {
                    self.marked[row][col] = true
                }
            }
        }
    }
}


func solve4() {
    let path = Bundle.main.path(forResource: "4", ofType: "txt")
    let string = try! String(contentsOfFile: path!, encoding: String.Encoding.utf8)
    let lines = string.split(separator: "\n")
    let numbers = lines[0].split(separator: ",").map({ Int($0)! })
    
    var boardVals: [[Int]] = []
    
    var boards: [Board?] = []
    for i in 1..<lines.count {
        let line = lines[i]
        
        if boardVals.count == 5 {
            boards.append(Board(vals: boardVals))
            boardVals = []
        }
        
        var vals: [Int] = []
        for i in 0..<5 {
            let start = line.index(line.startIndex, offsetBy: i * 3)
            let end = line.index(line.startIndex, offsetBy: (i * 3) + 1)
            let range = start...end
            let sub2 = line[range]
            vals.append(Int(sub2.trimmingCharacters(in: .whitespacesAndNewlines))!)
        }
        
        boardVals.append(vals)
    }
    if boardVals.count == 5 {
        boards.append(Board(vals: boardVals))
    }
    
    
    for num in numbers {
        //        print(num)
        for i in 0..<boards.count {
            let maybeBoard = boards[i]
            if maybeBoard != nil {
                var board = maybeBoard!
                board.mark(num)
                if board.isBingo {
                    print("bingo", board.score * num)
                    boards[i] = nil
                } else {
                    boards[i] = board
                }
                
            }
        }
    }
    
}
