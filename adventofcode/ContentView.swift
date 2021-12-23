//
//  ContentView.swift
//  adventofcode
//
//  Created by David Adler on 04/12/2021.
//

import SwiftUI



struct SheetView: View {
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        Button("Press to dismiss") {
            dismiss()
        }
        .padding()
    }
}

struct Tab1: View {
    @State private var showingSheet = false
    
    var body: some View {
        Button("Show Sheet") {
            showingSheet.toggle()
        }
        .fullScreenCover(isPresented: $showingSheet, content: SheetView.init)
//        .sheet(isPresented: $showingSheet) {
//            SheetView()
//        }
    }
}



struct MainView: View {
    var body: some View {
        TabView {
            Tab1()
                .tabItem {
                    Label("Tab 1", systemImage: "heart")
                }
        }
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        MainView()
    }
}
