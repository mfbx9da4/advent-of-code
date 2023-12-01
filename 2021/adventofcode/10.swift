//
//  10.swift
//  adventofcode
//
//  Created by David Adler on 10/12/2021.
//

import Foundation




func solve10() {
    let path = Bundle.main.path(forResource: "10-small", ofType: "txt")
    let string = try! String(contentsOfFile: path!, encoding: String.Encoding.utf8)
    let lines = string.split(separator: "\n")
    let scores = [
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    ]
    
    var score = 0
    var score2s: [Int] = []
    for line in lines {
        var stack: [String] = []
        var ok = true
        print(line)
        for x in line {
            let c = String(x)
            if c == "<" {
                stack.append(">")
            } else if c == "(" {
                stack.append(")")
            } else if c == "[" {
                stack.append("]")
            } else if c == "{" {
                stack.append("}")
            } else {
                let last = stack.last
                if last == c {
                    let _ = stack.popLast()
                } else {
                    score += scores[c]!
                    ok = false
                    break
                }
            }
        }
        if ok == true && stack.count > 0 {
            var sch = 0
            for c in stack.reversed() {
                print(c)
                sch = sch * 5
                if c == ")" {
                    sch += 1
                } else if c == "]" {
                    sch += 2
                } else if c == "}" {
                    sch += 3
                } else if c == ">" {
                    sch += 4
                }
            }
            score2s.append(sch)
        }
    }
    
    
    print("ans part1", score)
    print(".count", score2s.count)
    print("ans part2", score2s.sorted()[score2s.count / 2])
}
