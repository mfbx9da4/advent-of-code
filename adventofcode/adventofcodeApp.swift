//
//  adventofcodeApp.swift
//  adventofcode
//
//  Created by David Adler on 04/12/2021.
//

import SwiftUI


func sumToN(_ n: Double) -> Double {
    (n * (n + 1)) / 2
}


func solve7() {
    let path = Bundle.main.path(forResource: "7", ofType: "txt")
    let string = try! String(contentsOfFile: path!, encoding: String.Encoding.utf8)
    let numbers = string.split(separator: "\n")[0].split(separator: ",").map({ Int($0)! })
    print(sumToN(11))
    var lowestI = -1
    var lowestCost = Double.infinity
    let theMax = numbers.max()!
    let theMin = numbers.min()!
    for x in theMin...theMax {
        var cost = 0.0
        for j in 0..<numbers.count {
            cost = cost + sumToN(abs(Double(x - numbers[j])))
        }
        if cost < lowestCost {
            lowestI = x
            lowestCost = cost
        }
    }
    print(lowestI, lowestCost)
    
}


@main
struct adventofcodeApp: App {
    var body: some Scene {
        
        solve7()
        return WindowGroup {
            ContentView()
        }
    }
}
