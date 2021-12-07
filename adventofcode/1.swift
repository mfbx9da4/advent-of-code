//
//  1.swift
//  adventofcode
//
//  Created by David Adler on 05/12/2021.
//

import Foundation

func solve1() {
    let path = Bundle.main.path(forResource: "1", ofType: "txt")
    let string = try! String(contentsOfFile: path!, encoding: String.Encoding.utf8)
    let lines = string.split(separator: "\n").map({ Int($0)! })
    var prev = lines[0] + lines[1] + lines[2]
    var inc = 0
    for i in 2...lines.count - 1 {
        let next = lines[i] + lines[i - 1] + lines[i - 2]
        if (next > prev) {
            inc += 1
        }
        prev = next
    }
    print(inc)
}
