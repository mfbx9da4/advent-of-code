//
//  8.swift
//  adventofcode
//
//  Created by David Adler on 10/12/2021.
//

import Foundation


// 1: 2
// 4: 4
// 7: 3
// 2: 5
// 3: 5
// 5: 5
// 0: 6
// 6: 6
// 9: 6
// 8: 7


// each char could be one of 7 chars
// assign all chars at random from one of the chars in that word
// loop through each other word if it forms valid words
// then we have a valid set use it
// for example

// a b c d e f g
// 2^7
// config:
// a: a, b: b, c: d, d: e...
// 7!

// t(e, c) -> d (valid)
// sort the words first
// for each encoded -> is valid word
// given a configuration
// rec(array) => array[]
// [1, ...] or [..., 1]

func perm<T>(_ arr: [T]) -> [[T]] {
    if arr.count < 2 {
        return [arr]
    }
    var ret: [[T]] = []
    let rest = Array(arr[1...])
    for p in perm(rest) {
        for i in 0...p.count {
            ret.append(Array(p[0..<i]) + [arr[0]] + Array(p[i...]))
        }
    }
    return ret
}


func configs() -> [[String: String]] {
    let a = ["a", "b", "c", "d", "e", "f", "g"]
    let perms = perm(a)
    var dicts: [[String: String]] = []
    for p in perms {
        var dict: [String: String] = [:]
        for i in 0..<a.count {
            dict[a[i]] = p[i]
        }
        dicts.append(dict)
    }
    return dicts
}


let allSets =  [
    Set(["a", "b", "c", "e", "f", "g"]): 0,
    Set(["c", "f"]): 1,
    Set(["a", "c", "d", "e", "g"]): 2,
    Set(["a", "c", "d", "f", "g"]): 3,
    Set(["b", "c", "d", "f"]): 4,
    Set(["a", "b", "d", "f", "g"]): 5,
    Set(["a", "b", "d", "e", "f", "g"]): 6,
    Set(["a", "c", "f"]): 7,
    Set(["a", "b", "c", "d", "e", "f", "g"]): 8,
    Set(["a", "b", "c", "d", "f", "g"]): 9
]




func isValid(_ config: [String: String], _ innie: String) -> Bool {
    var o: Set<String> = Set()
    for c in innie {
        o.update(with: config[String(c)]!)
    }
    return allSets[o] != nil
}

func decode(_ config: [String: String], _ innie: String) -> Int {
    var o: Set<String> = Set()
    for c in innie {
        o.update(with: config[String(c)]!)
    }
    return allSets[o]!
}

func solve8 () {
    let path = Bundle.main.path(forResource: "8", ofType: "txt")
    let string = try! String(contentsOfFile: path!, encoding: String.Encoding.utf8)
    let lines = string.split(separator: "\n")
    let allConfigs = configs()
    var countSimple = 0
    for line in lines {
        let parts = line.split(separator: "|")
        let encoded = parts[0].split(separator: " ")
        let inputs = parts[1].split(separator: " ")
        for config in allConfigs {
            var ok = true
            for x in encoded {
                if isValid(config, String(x)) == false {
                    ok = false
                    break
                }
            }
            if ok {
                var digits: [String] = []
                for x in inputs {
                    let digit = decode(config, String(x))
                    digits.append(String(digit))
                }
                let val = Int(digits.joined(separator: ""))!
                countSimple += val
                
                break
            }
        }
    }
    print(countSimple)
}
