//
//  11.swift
//  adventofcode
//
//  Created by David Adler on 21/12/2021.
//

import Foundation


let input11 = """
1172728874
6751454281
2612343533
1884877511
7574346247
2117413745
7766736517
4331783444
4841215828
6857766273
"""

struct Pair<T:Hashable> : Hashable {
    let values : (T, T)
    
    init(_ a: T, _ b: T) {
        values = (a, b)
    }
    
    static func == (lhs: Pair<T>, rhs: Pair<T>) -> Bool {
        return lhs.values == rhs.values
    }
    
    func hash(into hasher: inout Hasher) {
        let (a, b) = values
        hasher.combine(a)
        hasher.combine(b)
    }
}



func solve11() {
    // parsing
    let lines = String(input11).split(separator: "\n")
    var rows: [[Int]] = []
    for line in lines {
        var row: [Int] = []
        for c in line {
            row.append(Int(String(c))!)
        }
        rows.append(row)
    }
    
    func printRows() {
        print("[")
        for row in 0..<rows.count {
            print("\t",rows[row])
        }
        print("]")
    }
    
    let directions = [
        [-1, 0], // top
        [-1, 1], // top right
        [0, 1], // right
        [1, 1], // bottom right
        [1, 0], // bottom
        [1, -1], // bottom left
        [0, -1], // left
        [-1, -1] // top left
    ]
    
    func inRange (_ row: Int, _ col: Int) -> Bool {
        row >= 0 && row < rows.count && col >= 0 && col < rows[0].count
    }
    
    var totalFlashes = 0
    

    for step in 1...10000 {
        var flashes = 0
        
        // increment all by one
        for row in 0..<rows.count {
            for col in 0..<rows[row].count {
                rows[row][col] += 1
            }
        }
        
        // create visited matrix
        var visited = rows.map { $0.map { _ in false } }
        
        var toVisit: Set<Pair<Int>> = Set()
        
        // for each gt 9 -> mark visisted -> increment neighbours, add neighbours to queue
        for row in 0..<rows.count {
            for col in 0..<rows[row].count {
                if rows[row][col] > 9 {
                    visited[row][col] = true
                    rows[row][col] = 0
                    flashes += 1
                    
                    for dir in directions {
                        let nextRow = row + dir[0]
                        let nextCol = col + dir[1]
                        if inRange(nextRow, nextCol) && visited[nextRow][nextCol] == false {
                            let p = Pair(nextRow, nextCol)
                            if toVisit.contains(p) == false {
                                toVisit.insert(p)
                            }
                            rows[nextRow][nextCol] += 1
                        }
                    }
                }
            }
        }
        
        
        // bfs queue -> if not visisted -> apply flash -> add neighbours to queue
        var queue = Array(toVisit)
        while (queue.count != 0) {
            let (row, col) = queue.removeFirst().values
            if visited[row][col] == false && rows[row][col] > 9 {
                visited[row][col] = true
                rows[row][col] = 0
                flashes += 1
                for dir in directions {
                    let nextRow = row + dir[0]
                    let nextCol = col + dir[1]
                    if inRange(nextRow, nextCol) && visited[nextRow][nextCol] == false {
                        queue.append(Pair(nextRow, nextCol))
                        rows[nextRow][nextCol] += 1
                    }
                }
            }
        }
        if step <= 100 {
            totalFlashes += flashes
        }
        
        if flashes == rows.count * rows[0].count {
            print(step)
            break
        }
        
    }
    
    print(totalFlashes)
    
    
    
}
