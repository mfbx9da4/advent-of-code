from dataclasses import dataclass
from typing import List, Literal, Tuple, Optional

# David's input
input = """
F|7.F|-F|777FJ7FF77-F777F7F|7..FF-77FF|--JJFJ7-J-F77.FF-F7F-F-FL7|--7---F.FL-7-7J.FFF7|-FFJ7.7.LF-LLJ77|F7FJJ-JFF|-.|FFF7F7..FFL7F-FJ-7-LL77
|-J-JL.LL7-7-J|FLJLJ.L|7|F-J-|-FL7L-7-J-LJFJ-77FF-LL-FJFLLJ7L.L.||..7FJ7J7FJFL-LJFLJL--.|7JL||FLJLL|JLJ.LL7J.FF|-J.L---JJ.F77L-LLF7L|F77LJ|J
LLJ|FJF-F--7LFL-J|7F--F--JJ|-JF-7|F-JJJ..FLJ.LFJJ.FJ-|J|J7.JFFJ-7---LLJL7FJ.J-FL-FLF7|LLJJ|L-J--7JJ|77LJ.FJFFFJL7J7|-|-J.FL7JL|LLJL7L7JFF.JJ
7-L-J7|LJJ-7-JLLF77J7.LF77LLJJL7|||F7J.|-FJ|FL7|-|7|JL7JLF|--JJJ|J7..|LL|J7-|FFJ|LJ.7--L|L7.L|F7.FF||L..FLJL-JF-JFLFF77.FFLLJL7F|F-J-L7JFJJ.
-7JL|7L-||F7|F|JF-F---7|L77F|-FJLJ||L7-J7|7F7.L|7L|JL---7-|7LJ|-|.F7--.|.L-FJ7JJLL-7|LF-7F|FF77JF7JLJ7.|.|-|7J|.L-.|JL--FJ7--7|-FJ7|J|LLL--J
L77JLJ-FJ-FJJ-|7JF77LF-7LL-F7FJF-7||FJF7L|J-J7JL--||FJJ-|..J..F-7--FJ|77.L7|L7-7..FL-.L7|-L|J|J.FJ7|F-FJ--.J7F-LFJ--J.FF|-7--7--|-F-FJ.LL7|J
LLF7-7F7.-L|JLJ|.LJ-.F7|FF.||L-JFJ||L7F7L|J.L-77-77-JJ.-J77.F.L7|F|L77|L-7F--J|--LLJ|.F||J-LFLJFF7--|L|..|-|L|JFJ77|.L--77.LJ-JLL-7F|-7|LLL7
|.||.F-...FLF-7L7-7FJ|FJ||FJ|F-7L7||FJ||F77.-7L||.|-|.LLL-7.F-7||J7-LJ77L||J--||.|JFFJF|L-7F7JF-J|7J|||-LL7|.|F7LJ-|.F7FL7F7J||LL7LF--77-L|7
FFJ7.||.--7.JJF.7.F-J7|F7FL7LJFJFJ||L7|||L7.|L7|J-F777-|L7-7L7LJ|JL7-L-77L-.7L|7FF-|J|-L7FJ||F7.FLL77F-.FLLF7-||7LFF-LF|.|-J7FL-7|...-77F-LJ
||L|7F7JJ|J...F.777JJL7||F7L-7|FJFJL7||||FJ7-F7||-||-F-J|..FLL7FJ7JF-7L|7-L--FJ||7-J.F7FJL7|L7LLJJ7LFJF|J7F|L-JL7-7|.|||FL7LJ7LJ-|-77.LFJ|..
LJ7FJ-J|-JFF|-J7L-.|JFFJ||L--JLJFJF-JLJLJL7F7F7-7F||7|-F7-FFF7||F-7J-7-L|7J7.||F7.J|.||L7FJ|FJ|F|7LL-|7L---L--7FJJJF7F|JF-7--|7||||F-F-||L|7
|.LL|J.L-JFLJF7|.|7.F-L7LJF--7F7L7|F----7FJ||||-F7||FF7F7F--JLJLJFJ||F.|J.LF-LFJL7JF-JL-JL-JL7-F.|JF-|F77F|||FJL77.-JF7.LF7LFJ-|7-||FL-|-JL|
JFF-7.FFLFJ7-FLJ7L7F|7FL7FJF-J|L7LJL---7LJFJLJL7|LJL-J|||L----7F-J|FFJ--F77.|.L-7L7L-7F------JJ.FF77--J|7FF7FJF7L7-.LL--FJ|||L-LJ.LJ7.|J.L|J
|FJJ|.---L-JJLL||L|LF-7FLJ7|F-JJL-7F---JF7|F---JL--7F-J|L7F-7FJL7J7LJL-L||L-7F7FL7L7L|L---7F7J-FF7F777F-7FJLJFJL-J7F77J7.L|F|J|LJFL7F7L-7-7-
L77FJ-||7FF7---LJ-7.LJF7F-7LJF-7F-JL-7F7||||F7F7LF-JL7FJFJL7||F-JF77J||L||7LFJ|F7L7L7|F---J|L-7F|LJ|F7|FJL--7||F7F-J|F-77F-|J77LF|-JJJ.J7.LJ
||LJ..L-LJJ-7-7L7.L.FF|||FJF7L7|L-7F-J|||||||LJL7L7F-J|FJJFJLJ|F7|L7F-7.|L7FJFJ||.L7||L--7||F-J-L-7LJ|||F7|FJL7|||F-J|FJJ-.|L-7-|L|.|L.L|77.
F7-LJ7|JFL|7LFJ|L7.FF7|LJ|FJL-JL--J|-FJLJLJLJF--JFJL7FJ|F7L7F7||LJFJL7|-L7|L7||||F7|||F--JFJ|F7F7LL-7LJLJL7L7FJ|LJL--JL7J.-|-L--F-7F|--|J|7L
J77F.JJ.J-7J-L7F77F7||L-7|L-------7|FJF------JF7|L-7||FJ|L7LJ|LJF-JF7||F7||FJL7|LJLJLJL-7|L7|||||FF7L7F7F-JL||FJF7F----J---J|.|7L7L7|.FLF|77
FL-JF|FL-7.|7LLJF7||||LFJL-7F7F7F7|LJFJ-F--7-FJL7F-J|||L|FJFFJF7L-7|||||||LJF-JL---7F7F-JF-J||LJ|FJL7LJ|L-7L|||FJLJF7F7J.|-|FL.L--7FJ---|JL7
FF7L-|L|.L|||.FFJLJLJL7L--7||||LJ|L7FJF7|F7L-JF-JL-7LJL7|L--JFJL7FJ|||LJ||F-J-F-7F7||LJF7L-7||F-JL-7|F-JF-JFJLJL7F7|LJL77FFJLL|.L.JJL-J7J-J|
|-7FFJL|.|||..FL-----7L---JLJ|L-7L7|L7|LJ||F7FJJF-7|F7FJ|F--7|F7LJFJ|L-7|||F-7L7LJLJL--JL7FJ||L7F7FJ|L7FJF7L7F--J|||F--JF77L-7J.|L.|.LL|-7J7
7F77|J7|F--FF-7JLF7F7L------7S77L7LJFJ|F-JLJLJF7L7|LJ|L7LJF-JLJL77L7|F-JLJLJFJFJF---7F---JL7LJFJ||L7|L|L-JL-JL7F7||||F-7||LL|LF--J.L7FL|L|-|
L7|LJ|F7L.J.L7|FL|LJ|F7F----JFJF7L-7|FJL7F7F-7||FJL-7|FJF7L-7F-7L7FJ|L---7F-JFL7|F--JL----7|F7|FJ|FJ|FJF--7F--J|||||LJFJ||F7|F|F|FJLJ7.7J|LF
F-FJLJLL---FFJL7LL-7LJ|L-7F-7L7|L--JLJF-J|||FJ||L--7LJL7||F7|L7L-J|FJF-7L|L--77LJL--7F----JLJ|LJFJL7|L7|F7LJF-7|||LJF-JFJL--7-JL77||.|7LLL7L
FJ|J-|J-FJ.FL-7|-F7L-7|F7LJFJFJL--7F-7L-7||||7|L7F7L-7FJ||||L7L7F7|L7L7|FJF--JF7-F7FJL--7F-7FJF-JF7|L-JLJL7FJFJ|||F7L--JF7F-JFLLJ|L-.|FF.FJJ
L7.LF777FFF7F7||.|L--J|||F7L7|F7F7LJJ|F7||LJL7L7|||F7|L7|LJL7L7||||FJFJ|L7|7F7||FJLJF---J|FJL7|F7||L-7F---J|FJFJLJ|L----JLJF77--7-7.L-JLF|J.
FJ7LJJL--LLFJLJL-JF--7LJLJL-JLJ|||LF-J|LJL-7FJFJ||LJ||FJL-7FJ.|||LJL7L7L-JL7|LJ|L--7L7F7FJ|F7|||LJL7FJL7F7L|L7L-7FJF--7F7F7||JLFJF|7LLF--J.|
|JL.J7-|J|.L-7F---JF7L--------7|||FJF-JJF-7|L-JFJL-7||L-7FJL-7|LJF--JJL-7F-JL-7|F7FJFJ||L7|||||L-7FJL-7LJL-JFJF-JL7|F-J|LJ|||-FJFF7--J..||-|
JLLFJLFJFF--7LJF--7|L7F7F7F---JLJLJFJ7F7L7||F--JF-7|LJF-JL-7FJL-7L7F7F--JL7F7L||||L7L7||FJ|||||F7||F-7L7F---J7L-7FJ||F-JF-J||F7F-J|.|F|-L7.7
|.|.FJL-FL-7L-7L-7LJFJ|||||F7F---7FJF7||FJLJL-7FL7LJF7L7F7FJL7F7|FJ||L---7LJL7|LJ|JL7|||L7LJLJ||LJ|L7|7||LF7F7F7|L-JLJF7L--JLJLJF-JFF-|L|77F
L77.|7FFF--JF7L7FL-7|FJ|||LJLJF77|L7||||L--7F-JF7L--JL7LJ|L7FJ|||L7||F7F7|F--JL-7L7FJLJL7L7F--JL-7L7|L7|L7|||||LJF----J|F7F-7F--JFJ7|F--7L|J
F||7L-77L---J|FJ7F-J|L7|||.F--JL7L7|||||F--JL7.||F-7F-JF-JL||FJ||FJ|||||LJ|F7F7FJFJL--7FJFJL---7.L7||FJ|FJ|LJLJF7L----7LJLJLLJJJ-|-LL--7J-LJ
L|-FF7LF.FF--JL-7L-7L-J||L7L-7F7L-J|||||L---7L7||L7|L-7L7F-J||FJ||FJ|||L-7|||||L7L7F7FJL7L7F---JF7|LJ|FJ|FJF-7FJL-----JF--7F7.FLJ|L|.|JL--JJ
F.LLJF.|F7L----7L--JF-7|L7|F7LJ|F-7LJ||L7F7FJFJ||FJ|F7|FJL-7||L7|||FJ||F7|LJLJL7|FJ|||F7|FJ|F-7FJ||F-JL7LJFJ.LJF7F7F7F7|F-J||-||F|.|FL7L|..L
J.L|.L-FJL-7FF7|F---JFJL-J||L7FJ|7L7FJ|FJ|||FJ-||L7|||||F7L|||FJ||||.||||L7F---J||7||||LJL7||FJ|FJ||F7LL7FJF---J||LJLJLJ|F-JL--7-J7-|F7-L.|.
F----FFJF-7L-J|LJF7F-JF--7|L7||FJF7||FJL7|LJ|F-J|FJ||||||L7|||L7||||FJ|||FJL7F--J|FJ||L-7FJLJ|FJL7||||F7||FJF7F-J|F--7F7LJF7F--J7F7-F7J-7|LL
JJ-7L-L-JFL7F7L-7||L7FJF7||FJ|LJFJLJ||7L||F-JL-7|L7LJ||LJF|||L7||||||FJ||L7FJ|F--JL7|L7JLJ|F-J|F-J|||||LJ||FJLJF-JL-7LJL--J||F7LFJ|FJL7J7|F|
|L|LFLJJ.F7LJL-7||L7LJFJLJ|L7|F7L--7|L7FJ||F7F7||FJF-JL7F7|||FJLJ||||L7||FJL7|L-7F7|L7L7F--JF7||F7||||L77LJL---JF7F-JF-7|F7LJ||-L7||F-JLFFJ|
|-|..|J-FJL----J|L7||FJF-7L-JLJL---JL-J|FJ||||||LJFJF-7LJ|||||JF7||||7LJ|L7FJ|F-J|||FJFJL7F7|||LJ|||||FJF-----7FJLJF7L7L-J|F-JL--JLJ|J7||F.J
F-FL--7L|F---7F7L7||FJFJJL--7F7F-7F--7FJL7|||||L-7L-JFJF7||||L-J|LJ||F--JFJL7|L7FJ||L7|.FJ||||L7FJ|||LJFL---77LJF7-|L7|F--J|F----7F7|-|F-|7J
|FL|.|FFJL7F-J|L7LJLJFJF----J|||FJ|F-JL-7||||||F-JF7FJFJ|||||F-7L-7|||F-7|F-J|FJL7||FJL7L7||||FJL-J||F-----7L---JL7|FJ|L7F-JL---7LJLJ|LJ||.|
L-J.FFJL--JL--JFL---7L7|F7F-7|LJL-JL---7LJLJ||||JFJLJFJFJ||||L7L7FJ||||FJ|L-7||F7|||L7FJFLJ|||L7F--J|L7F--7L------J||7|FJL7F----JL|-L7FJ-|-7
|.F-J|L|7F---7F-----JFJLJLJ.||F---7F---JF7F7LJ|L7L7F7|-L7|LJL7|7|L7||LJ|FJF-J|||LJ|L7|L-7F-J||FJL7F7L7LJF-JF7.F--7J|L7||F7|L-7FF7F7.F-J|.LFJ
F-|7LJ-JFL--7|L7F7F-7|F7F7F7LJL--7|L----JLJL-7|FJJLJLJF-JL7FFJL7|FJLJF-JL7L-7||L-7|FJ|F7||F7|LJF7||L-JF7L--JL7|F-JFJFJ|LJLJF-JFJLJL-7JFFFJ|J
JFL-L7.F----J|JLJLJ||||LJLJL--7F-JL------7F7FJLJF7F-7|L7F7L7L7FJ|L-7FJF7FJ-FJ|L-7||L7||LJ||||7FJ|LJF77||-F---J||F7L7L7|F---JF7|F----J|||F--.
|FJF-|.L----7L-7F7F-J|L7F7F7F7|L--------7LJ|L7FFJLJFJF7LJL7L7|L7|F-JL7|||F-JFJF-J|L7|LJF7|||L7L7L--J|FJL-JF7.FJLJL-JFJ||FF7FJLJL----7-J-|.|7
J|.|L7FF7F-7L-7LJLJF7L7||||LJ|L-------7FJF7L-JFJF7FJ.||LF-JFJ|FJ||F7|LJ||L-7L7L-7L7|L--J|LJL7|LL---7LJF---JL-JF----7L-JL-JLJF---7F--J.||J-L7
|-F7-LL||L7|F7L7F-7|L7|||LJF7L-------7LJFJL7F-JFJLJF7|L7|F7L7|L7|LJL7LFJ|F-JFJF-JFJL7F7FJJF-J|F----JF7|F---7F7L---7L7F--7F-7L--7LJ7.J.LF-F-7
7-7L|.||L-JLJL-J|FJ|.||LJF-JL-------7L-7|F7|L-7|JF7|||FJLJL7||FJL7F-JFJFJL-7|-L-7L-7||||7FJF7|L7F7F7|||L-7.LJ|F-7FJ.|L-7LJFL7F7L--77FJ.|-7J.
--L7F-F|F-7F---7|L7L7||F-JF7F--7F--7L--J||LJF-JL-JLJLJL---7|||L-7LJF7L7L7F-JL-7-L7FJ|||L7L-JLJFJ|||LJ||F7L--7LJFJL-7|F7L---7|||F7FJ-J.-F-J.F
||L7|7JLJ-|L7F-JL7L7|LJL--JLJF7LJF7L---7||F7L7F----7F-7F--J|||F7L--JL7L7|L-7F7L7FJ||||L7L-7.F7L7|LJF7LJ|L---JF7L7F-JLJ|F7F7|||LJ||JLJFL||..|
FJFFFL.FLFJFJL7F-JFJ|F-7F7F--JL-7||F---J||||J|L---7||F||F-7|||||F7F7FJFJ|F-J|L-JL7L7LJFJF-JFJ|FLJLFJ|F7L-----J|||L--7FJ|LJLJ||F7LJF7|7FL7-FJ
L7L77JFFJL-JF-JL7-L-JL7LJLJF7F-7LJLJF7.FJLJL-JF---J|L7|LJFJLJLJLJ|||L7L7|L-7L---7L7|F7|FJF7L7|F7F7L7LJ|F------JFJF-7|L7L77F-JLJL7F-FL|L-F.J.
FJ-|||F--|F7L7F7|7LF--JF--7||L7L7F-7||FJF7F-7FJF--7L7||F7L7F-7F7L|||FJFJ|F-JF7F-J.LJ||LJFJL-JLJLJL-JF7|L-7F7F7JL-J7LJ7L7L7|F7F7FJ-FLFJLLJF.7
FJ|LJ-L7.FJL-J|LJF7L---JF7LJL-JLLJFLJLJFJLJL|L-JF-J|LJ||L7|L7LJL7LJLJFJFJL-7|LJF----JL-7L----7F7F7F-J||F7LJLJL---77F-7FJFJLJ|||L77-.L-7LF|-7
|-F7-|J|-L7F-7|F-J|F7F7FJL-7F7FF-------JF7F-JF--JF--7-LJFJL-JF7FJLF7LL7|F--JL-7L-7F7F7FJ-F7JFJ|LJLJF-JLJL---7F7F7L7L7|L-JF7-LJ|FJJ-FJ.F--J7|
L|LF7|-LL-LJFLJL-7||LJLJF-7LJL7L--------J||F7L7F-JF7L-7JL7F7FJLJF7|L7|||L7F7F-JF-J|LJ||.FJL-JFJF7F-JF------7LJ||L7L7|||F7|L--7LJ7-LF7-7F7LL7
FJ-L77777LFJ-F---J||F7F7|FJF7FJF----7F-7FJLJL7LJF7|L-7L-7LJ|L---JLJFJ-||-|||L-7|F7|F-JL7L----J-|LJF-JF7F7F7L-7LJ-L-J|L-JLJF--JJ.77.L7..F7-J|
|||L|J.77-L|FL---7|LJ||||L-J|L7L-7F7LJ7LJF7F-JF-J|L-7L--JF7L7F-7F7FJ.FLJL|||F-J||LJL7F7L--7F7F7L--JF-JLJLJL--JF7F7F-JF-7F7L--7|||-LF7FFF7.FJ
|FF-JJ7LF7-LF----JL7|LJLJ7F7L7L-7LJL7F---J||F7L-7L--JF7F-J|-LJJLJ|L--7-F-||||.LLJF-7LJL--7|||||F7F-JF-----7F7||LJLJF-JJLJL---J7F||LL-LFJ|F7J
LL7.J.LFJ|.FL-----7|F7F7F7|L7|F7|F7FJ|F---JLJL-7L7F--JLJF7L---777L7F-J--JLJLJ7..FL7|F7F--JLJ||||||F7|F----J|L7|F7F7L7F7-F7F7F7F-77.|.||L-LJJ
LL77.L7L7L7F7F7F--J||LJ|||L7|LJ|LJLJFJL---7FF-7L7LJF7F7FJ|F7F7L--7|||J-JF||LL7FFF7||||L-7F-7LJ|||LJ||L-7F7F|FJ||LJL-J|L7|||LJ||FJ|F--J|JJJFF
LL|||L7.L7LJ||LJF-7|L7FJ||FJL7FJF--7|F----JFJFJ-L--JLJLJ7LJLJL-7FJ||-J7FJL7|7.FFJLJ|||F7LJ.L-7LJL7JLJF7LJL-JL-JL--7F7L7LJ||F7LJL-77.|LFJJLJJ
.|LL-J.7|L-7|L--JFJL-J|FJ|L-7||FJF7LJL-7|F7L7|JF7F---------7F7-LJ.LJ.LF-7-J7-7JL--7LJ||L--7F7L7F7|F--JL-7F7F------J|L-JF7LJ||F7F7L7777|.FFJJ
FL-|LFF--7.||F77FJF7F7LJFJF-J|LJFJL-7F7L7||F|L7|LJF-7F7F7F7LJL---7|.7JF-JJLJFFF7F-JF-J|F-7LJL7||LJL----7LJ|L--7F---JF7FJL--J||||L7|7-J7FFL-7
||.|J|L-7L-JLJL-JFJLJL-7L7L-7L7FJF-7LJL7LJL-JFJ|F-JJLJLJ||L------JJ7-7LF|JJJF-J|L-7L-7LJ7L--7LJL7F7F7F7L-7L7F7LJF-7FJLJF---7||LJ-LJJ|.|LF-7|
FF|J.F|JL----7F7FJF---7L7L--JFJL7L7L-7.L7F-7FJ-||F7F---7|L--77L|LJ-F-L-L-F77L-7|F-JF-JF7-F7J|F-7LJLJLJL--J7LJ|F-JFJL---JF7FJ|L7|.|.F77-J.|FL
J.FJF7LLF--7.LJLJ|L--7L-JF7F7L-7L-JF-JF7LJFJL--JLJLJF--JL-7FJ77.|.|J.J-JJ|L--7||L-7|F7|L-JL-JL7L------7F---7J|L-7L7F7F-7||L7L7L7FL-FJJL7-LJ|
|F|F|7FLL-7|F7|-F----JF--JLJL7FJ7F-JF-JL7-L7F7F-7F-7L----7LJJLJFFFF--7|LLL7F7LJL--JLJLJF7F7F7FJF7F7LF7LJF-7L7|F7L7LJ|L7LJL-J7L7L7J.L|.LFJ.FL
FJLFF7F-7FJLJ|F7L-7F--JF-----J||FJF-JF--JF7|||L7LJFJF7F--JF|7.LFJF-JF-JJLLLJL-7F7F-7F-7|||LJLJFJLJ|FJL-7L7L-JLJL7L7FL7L7F7F7F7L-J.FFJ|.|.7-L
77F7|||FJL--7LJL7|LJF-7L7F-7F7L-JFJF-JF--J||||FJF7L-J|L---7F7F77L7-L|J...-F--7LJ|L7LJFJ|LJF---JF-7LJF-7L7L--77F7L7L-7L-J|||LJL----7JL|F|FL-|
F-JLJLJL---7L--7|F7-L7|JLJ.LJ|F-7L7L--JF7FJ|||L-JL--7L----J|LJ|7.|FL|.FL.FL-7L--JFJF7|FJF-JF7F7|JL7FJFL7L---JFJ||L--JFF-JLJF--7F--J7.LJ-7JF|
L-7F-7F-7F7L---JLJL-7||F-7FF-J|FJFJF7F7||L7LJ|F-----JF-----JF7L77-JL|77FL77|L-7F7L7|LJL7L--JLJ||F-JL7F-JF--7-L7L------JF7F7L7JLJ|F||F|-J.F||
L.LJ.||FJ|L-7F-7F7F7LJ|L7L7L--J|FJFJLJLJL-JF7LJF----7L7F--7FJL-JJ|FFJ|L7--L||FJ|L7||F-7|F-----J||F7FJL--JF-JF7|F------7|LJL-J7-F--7FF77.--77
.FLJFLJL-J7FJ|FJ||||F7L7L7|F7F7LJJL7F7|F7F7|L--JF--7|FJL-7|L-7F7-FFJL7-7|.LLFJFJFJ||L7LJL-----7|||LJF7|F7L--JLJL-----7|L-----7-L7FJ7|L.FJL||
FF7-FJF--77L-JL-J||LJL7L-JLJLJL7JF7LJL-JLJLJF---JF7LJ|F--JL--J||F7L7-|7L77.FL7L7L-JL-J.F--7F-7LJ||F-J|FJL-7F7F-------JL------JF7|||JL7F|.|L|
LFF7||L-7L7F-----J|F--JF7F----7|FJ|F---7F7F7L---7|L--JL--7F7F7||||F7F|J-||F7J|FJF-----7L-7|L7L-7LJ|F7LJF-7LJ|L7JF7F7F7.F7.F7F7|LJL-7.F-F-J.|
.FJL--7-L7|L------JL-7FJ||F--7||L7LJF-7LJ||L7F-7LJF------J|LJ||||||L7J-F7J7LFLJ7L----7L--JL7|F7L-7||L7FJFJF7L-JFJLJLJL-JL-J||LJF---J-J|L-7LJ
FL---7|F7||F7F---7FF7|L7||L-7LJ|JL-7|FJF7LJFJ|7|F7L-7F7F7F|F-J|LJLJFJJ.||||||F-7JF7F7L---7FJLJ|F-JLJ|LJ-L-JL---JF-----7F7F7LJF7|F--7-FJ7L7.|
7-LLFJLJLJLJLJF-7L-JLJFJLJF7L-7L-7-LJL-JL-7L-JFJ||F7LJLJL7||F7|F--7|JLF|L77--|FJFJLJL----JL7F7||F77F----7F------JF---7LJLJL--JLJ|F-J-|.|7LJJ
L--L|F-7F-7F7FJ-L-7F-7L77FJL7FJF7L------7FJF7-|FJLJ|F-7F-J|LJLJL-7||7LFJFJ.F7|L-JF7F------7LJLJLJL7L---7LJF7-F7F7|F-7L7F7F7F----JL-7FJ-J|FJ|
|-|.LJFJL7LJ|L-7F-J|FJFJFJF7LJFJ|F-----7|L-JL7|L--7|L7|L-7|F--7F-JLJF-JFJ|F-7L---JLJF-----JF7F-7F7L7|F7|F-JL-JLJ|||FL7LJ||LJF------JJ|LL7LF-
L--L-FJF7|F7L7FJL7FJ|FJJL-JL7FJFJ|F-7F-JL-7F7||F7FJL7|L-7||L-7|L--77L-7|F7L7L7LF7JF|L---7F-J||L||L7L7||LJF7F7F--J|L-7|F-J|F-J.F--7|JFFJ.7-LJ
.|-|.L7|LJ|L7|L-7|L7LJF---7FJL7L-JL7|L-7F7LJ|||||L-7|L-7LJ|F-JL---JF--JLJL7|FJ7|L7FF7F7JLJJFJL7LJ7L7LJL--JLJ||7F7|F-JLJ|FJL7F7|F-JF7-F7FJJ..
F.FF-FJL-7L7LJF-JL-JF7L--7|L--JF---J|F-J||F7LJLJ|F-JL--J-FJ|F7F--7|L----7FJ||F7L7|FJLJL----JF7L7F7-L7F-----7||FJLJL7F---JF7LJLJL--JL-JL77FL7
77-|LL-7FJLL-7|F-7LFJ|F7FJL7F7-L7F-7||F-JLJL7F7.LJ-F7F7F7L7||||F-J7F-7F7||FJ|||FJ||F--7F---7|L7||L--J|F---7|||L-7F-J|F---JL-7F---------J-FJ.
L7.L7LFJL7|FFJ|L7L7L7LJ|L7FJ||F7|||||||F---7LJL---7|||LJL-JLJ|||F-7L7|||||L7LJ||FJLJF-J|F--JL7||L----JL--7LJLJFFJL--JL-----7|L-----7|FLJJ|J.
|L--J-L7FJ77|FJLL7|JL-7L-JL-J|||LJFJLJ||F7FL------J|||F--7F--J|LJFJFJLJ||L-JF-J||7F7L--JL---7|||.F7F7.F-7L7F7F-JF7F7F---7F-J|F-----J777JL|.F
J7..|-FLJ|F7LJF--J|F--JF-7F-7LJL7FL77FJLJL7F------7||LJF-JL--7|F-JFJF-7LJF--JF7|L7||F7F---7LLJLJFJLJL7L7|FJ||L7FJLJ|L--7LJLFJL--------7J.JF|
FF--|-7FFF||F7L--7LJF--JJLJ|L--7L-7L-JF--7LJF--7F-J||F7L7F7F-J|L7|L-J7|F-JF7FJ||FJ||||L--7L-7F7FJF--7L-JLJF||FJL--7|F--J-F7L-7F-7F7F--J77.J|
FLJ-L-F7FF|LJL7F7L-7L7F-7LF7F-7|F7L--7L-7|F7L-7LJF7|||L7LJ|L7FJFJF7F7FJL--J|L7LJ|-||||FF7|F-J|LJFJF7L-7F---JLJF7F7||L7F--JL-7LJFJ|LJJLLFJ--7
7J7.L|LL-JL7F7LJ||FJFJL7L7||L7|LJL-7|L7FJLJL--JF-J||||FJJFJFJ|FJ.||||L-7F-7L7L7FJFJ||L7|||L7FL--JL||F7LJF---7FJLJLJL-J|F---7L-7L7L7||FFF7|J|
F-F7LFF7L-FJ||F7L-JFJF7L7LJ|FJL----JF7LJF7FF-7.|F-J||||F7L7|FJL7FJ||L-7||JL-JFJL7L7||FJ||L7L7F7F--JLJL7JL--7LJF7F7F7F7|L--7|F-JFJFJ-J---LJF|
L-.LJ|L77LL7|||L7F7|||L7L-7LJF------JL--JL7L7L7||FFJ||LJL7|||F-JL7|L-7LJL7F7FJF-JFJ||L-JL7|FJ||L-7F--7L7F-7L--JLJLJLJLJF--JLJF7L-J-7JJJ.L-L-
|-|LF7.LF7LLJ||FLJ|L7L7L--JF7|F-----------JFJFJ||FJFJL--7||LJL7F7||F7L--7LJ||FJF7|FJL---7LJL7||F7LJF-JFJL7L--------7F-7L--7F7|L-7JF77-JF.LL7
7|L|.||.J77J.LJ-F-JFJ7L--7FJLJL--------7F77|FJFJLJFJF---J||F--J||||||LF-JF-J||FJ||L7F7F7L-7FJ||||F-JF7L-7L--7F7-F7JLJ.L7F-J|LJF7|FJ|7FFL7-LJ
|7F|F7|7JF7-FJF|L--J7F---JL7F---------7LJL-JL7L7F-JFL--7FJ|L7F-J|||||FJF7|F7||L7||FJ||||JFJL7||||L7FJ|F7L--7LJL7|L-7F7JLJF-JF-JLJ|FJF-7-F.FJ
F-LJ|J7|--JF7-F7FFF--JF--7FJL7F7F7F--7L-7F--7|FJL--7F-7||FJFJL-7|||||L-J|LJLJ|FJ||L7|||L7L-7||||L7||JLJL--7|F-7LJF-J|L7F7L-7|.F7FJ|FJFJ|JFF7
|-|LJF7||.J-|.||FFJF-7|F-JL7F||LJLJF7L7FJL-7LJ|F---JL7||||FJF7FJLJLJ|F7FJF---JL7|L7|||L7|F-JLJ||FJLJF7F---JLJLL--JF-JFJ|L-7||FJLJFJL7|F7F7LJ
L7L7|FJL-7.-JL|L7L-J|LJ|F7FJFJ|F---JL-JL---JF-JL--7FFJLJ|||FJ|L----7|||L7|F7F7-|L-J|||FJ|L--7FJ||F--JLJF-7F7F-----JF-J||F-J|||F--JF7|LJLJL7J
LJFF---|.|7FF.L7L--7F-7LJLJJL-JL----7F7F7F7-L-7F--JFJF--J|||FJF7F-7|||L7|LJ|||FJF-7|||L7L-7FJ|FJ|L-7F-7|FJ|LJF7F-7FJF--JL--JLJL---JLJF----JJ
||LJ..LL-.J-FF7L--7|L7L----7F7F7F---J|||||L7F7||F-7L7|F-7|LJL7||L7|||L7LJF-J|LJFJ7LJ||FJF-JL7LJFJF7|L7||L-JF-JLJF|L-JF7F--7F--------7L--7JL-
|J7..||.|FJFFJ|F7L||-L----7LJLJLJF---JLJ||FJ||||L7|FJ||FJL--7|||FJ||L7L-7|F7|F-JF7F7||L7|F7-L7FJF||L-JLJFF7L----7L7F-J|L-7|L7F-----7L7F7|.||
|.LF-F7FLJLLL7LJL-J|F-----JF-----JLF----J||FJ|||FJ||FJ|L7F7FJ||||FJL7L7FJ||||L-7|LJ|||FJ|||F7|L-7|L7F7F--JL7F---JFJ|F7L7FJL7LJF7F-7|FLJLJ-|7
F7JL|.|||J..LL7F--7|L------JF------J|F7F7|||FJ||L7|||-|FJ||L7|||||.||FJL7|||L7FJ|F-J||L7|||||L7FJ|FJ||L---7LJF--7L7LJL7|L7FJF7||L7LJ-LJFL|..
-|-F-F-|77-7FFLJF7||FF7F7JF-JF7F-7F7FJ||||||L7||FJ|||FJL7|L7|LJ||L7FJ|F7|LJL7||FJ|F7|L7|||LJL7|L7|L7|L7F-7L--JF7L7L7F-J|FJ|FJ||L7L7JJFLJ---|
L-.F-7L7|LF-7F7FJLJL-JLJL-JF7||L7LJ|L7|||||L7LJ|L7||||-FJL7|L-7|L7||FJ||L7F7|||L7|||L7||||F-7|L7LJF||7|L7|F7F-J|FJF|L-7||FJL7|L7|FJF7-F--J.7
-J77FF7L7FL7LJLJF-----7F7F7|||L-JJFJFJLJ||L7|F-JFJ||||FJF7||F-J|FJ||L-JL7LJ|||L-JLJL7|LJ||L7LJFJF--JL7L7|LJ|L-7||F-JF7|LJL-7||FJLJFJJ||7.|F|
FJ|LLJF-J77L----J|F7F-J|||||LJF---JFJLF-J|.LJ|F-JFJ|||L7||||L7FLJ7LJF7F-JF-J||F-7|F-J|F-JL7|F7L7L--7FJFJL-7|F7|LJL7FJLJF7F7LJ|L-77||LFF-F-FL
77J|FF|JL|F-------JLJF-JLJ||F-JF--7|F7|F7|F--JL-7|FJ|L7||||L7L--7F--JLJF7L-7LJ|FJFJF7||F7FJLJ|FJF--JL7L7F7||||L-7FJL-7.|LJL-7|F-J-J|-FJFL7|7
|J-F--J.FFL-7F-7F7F7FJF7F-J||F7|F-J||||||||F-7F-JLJFJFJ||LJFL7F-JL--7F7||F7L--JL7|FJ|||||L7F-JL7L7F7FJJLJ||LJ|F-J|F-7L7L7F--J|L7..L7||J|FJLJ
J--7.|7.JFF-J|-||||||FJLJF7|LJLJL-7LJ|||||LJFJL--77L7|FJL-7F-JL---7FJ||||||F7F7FJ|L7|||||FJL7F-JFJ||L---7||F-JL-7|L7L7L-J|F77L7|-L.|FF7|LL||
L-|.-J7-F-|F7|FJ|||LJL7F7|||F--7F7L7FJ||LJ|FJF7F-JF-J|L7F7|L7F7F--J|FJ||||||||||FJFJ|||||L7FJL-7L7||F-7FJ|||F7F-JL-J.|F7FJ||F7LJ7F--7JLJ7LF|
|JL7J||.J-LJ||L-JLJF7FJ|||LJ|F7LJL-JL7||F--JFJ|L-7L-7|FJ|||FJ||L-7FJL7LJ||||||||L7|7LJLJL7||F7FJ-LJ|L7|L7|||||L-----7LJLJFJ||L--77|J|-FJF-L7
J-|7LJJF7FJ-||FF---JLJFJ||LFJ|L7F7F7FJ||L7F7|FJF7L7J||L7|||L7||F-J|F-JLFJ|||||||J|L---7F-J|||LJF---JFJ|FJLJLJ|F7F-7FJF7F7L7LJF-7L7-F..L7F7|J
|LL-.LF-77.-LJFJF-7F7FJ.||FJFJFJ|LJ|L7LJFJ||||FJL7L7|L7|||L7LJ|L-7|L--7|FJLJ|||L7L7F7FJ|F7||L-7|F-7FJ||L-7F7FJ||L7LJL|LJL-JF7|LL7|.LF|-J|JLJ
L.-J.FJ|LF77-FJFJ-||LJF7||L7|.L7L7FJFJF7|FJ|||L7||FJ|FJLJL7|F-JF7||F-7|||F-7||L7L7LJ|L7||||L7FJ||FJ|-FJF7LJ||FJL7L---JF7F7FJ|L-7LJ7--JF|LF7J
F7J|F7J7---7FL7L7-LJF-JLJ|FLJF-JFJL7L7||LJ7LJL-JFJL7|L-7|JLJL-7||||L7||LJL7LJL7L7|F-JFJLJ||FJL7||L7L7|FJL--JLJLLL7F-7FJLJ|L7|F7L7JL-J-F--|-J
FF.FLJL-7.LJ-LL7|7F-JF7F7|F7FJF7L-7L7LJL----7F--JF7|L-7L7F7F--J||||FJ|L--7L-7FJLLJ|F7L-7FJ|L7FJLJLL7||L------77F7|L7|L--7|FJ||L-J7-L-7|L-J||
-|7-|.-7J-7-FJFLJ-L7FJLJLJ||L7||F7|FJF------JL-7FJ|L7|L7|||L--7||||L7L7F7|F-J|-F7FJ||F7|L7L7|L7F--7LJ|F7F---7L7|LJFJL---JLJFJ|JLLJ--7L|-7F--
|L7F77FJF-J.||FJF|J||F---7|L-J|LJLJL7L----7F7F-JL7L7L-7|||L---J|||L7||LJLJL-7L7|||FJ||||7|FJL-JL-7L--J||L--7L7||F7L-------7|FJJ7LJ-FJFLL-|J.
L-7FJ7F7F|77.77LJJ|LJL--7LJF7FJ-F---JF-7F7LJ||F-7|FJF-J|||F7F-7|||FJL---7F--JFJ|LJL7|||L7|L-7F7F7L-7F7|L7F7L7LJLJ|F------7|LJJLF.|F-777.L-J.
||JLJ-L7LJL7-JJ-|-LL-F7-L-7||L-7L---7L7|||F7|LJFJ|L7L-7||LJ|||||LJ|F7F7FJ|F7FJFL7F7||||FJ|F-J|LJL--J||L7||L7L---7|L-----7||JL|LF7|7.LL-7-7.F
L|7FL||L|L7||J7.L7LLFJL---J||F7L7F--JFJLJ||||F-JFJFJF7|||F7LJFJL7FJ|LJ||JLJ|L--7||LJLJ|L7|L7FJF7F7F7|L7|LJFJF7F-JL7F-7F7|LJ|-F--L7JFLJJ|||-7
.|--FL|FF7L---|..|FFJF---7FJ|||FJL-7FJF-7||LJL-7|FJFJ|||||L--JF7|L7L-7LJF--JF7FJ|L---7L7||FJ|FJ||||||FJL7-L7||L--7|L7||LJJ-L-L7JJJ.|J|F77.||
F|.LJ.F-F7J||.L77--L7|F--J|F||LJ|F-JL-JFJLJF---J|L7||LJLJ|F--7|||FJF7|F7L--7|LJ-|F7F-JFLJLJ.LJ-LJ|||||F7|F-J||F7FJ|FJ|||L|J7|7||J.77||LLL7-L
FF-77.L7LL--|-|L7-77LJL--7L7||F--JF-7F7L7F7L-7F7L7|L7F7J|LJF-J|||L7||LJL-7FJL7F-J||L--7|.|JF|J-FL||LJLJLJ|F7|||LJFJL7LJ7FJ---77JF|||7|7.|..J
|LL777.--F-7J7|J.FJL7LLF-JFJ||L--7|FJ|L7LJL7FJ||FJL7LJL7F77L-7|LJFJ||F---JL-7|L7FJL-7FJJ-L7LJ-77-LJJ|LF--J||||L-7L-7L---77|L|LJ7FLJ|7..F7F||
L-J||J.J.LJ|L77.FF--|FL|F7|.LJF--J|L7L7L7F-JL7|LJF7L7F7|||F7-||F-JFJ|L--7LF-J|FJL--7LJ|JF-77FF|F-|LF-FJF-7|||L7FJF-JF-7FJJ7.L-F7-JLL7--7---L
L|LL7FF.F|F.|||7L7JJ|FJLJ|L7F-JF-7L7L7L7LJF--JL7FJL-J||LJLJL7||L7FJFL7F7|FL-7|L7F7FJ-L7.JF|F-|J||JF7|L-J.LJ||FJ||L7FJFLJJ.FF7F7JLFJL-..LLLJL
.7J-|-F7F77FJJJ7.|JF||LFFJFJL-7|FJFJLL7L7J|F-7FJL7F-7|L7F7F-J||FJL7F-J|LJ7-FJ|FJ||L7J-L7||-7.--J7FJL-JL|7LFLJL7L-7LJ|LJJ|J7|FL--7J7J-J.||L7L
.L.7.LLF-JLF|-77-|-FLJ.FL7L-7FJ||FJ|-|L7L7||FJ|F-J|L|L7|||L7.LJL-7|L-7L7-7-|FJL7||FJ.L-L||.|---J|FL-7.FJJ-F---JF-J|FJJJ||FF77.|L|LJ.7F7-|J7J
|.FL-F-JJ.FL--JF.L7|JJF|LL7FJL7||L-7F-JL7|LJL-JL7FJFJFJLJL-J.|J|.||J.L7L-7JLJ-L||LJ||JF7|F-FJ-.FF-JFL|7JJ-L7F-7L7F-7-F-JLFJ|LL77LF7|F7LL|L7-
F-J|.||7F7LJFL7J..FJ|L7J|.LJFLLJL-7|7|L|||F-7J.||L7L7L-7.||-7J.L-LJ7-.L--J7|JJFLJJ.JJ-L-J-7L.L|7JLF|J||7.F7LJLL-J77JFJ-JLL7.7.--.LJ|LJ--7.||
7JJFF-J|-7-7|FJLJ-J.F7..FLL|7FL|J.||LF--JLJFJJ-F|FJFJF7L7--F--||FJJ||-JLJ7LJ..FLL--J|..|-LLJ7L||7LF7L|.--L-7|F|||LJF-JL7.FJL7-L7.F|F7||L|JLJ
|JF-J-LJL|.|L-L7..F--7-L7|L-7FL|LFLJFL--7F-JJ-FFJ|-L7||FJJFLJ7.7LL|FJ7F7J|7FF-J|J.|.-J-F--L7L-----|JFLF.L-L-L7|L--|LJ.7-FJJ-|7.FF|7J|F--FJ7J
|-LL7|L|FJ-JF|L|77||JJL||FL7L77|-FLJ||LLLJJLL7FL7|F-J||L7FJ7-FJJ--7|-7|F7LL7LL7L-|.-.|-|J7.LJJ|J..L.J-J7.FFF.L|..FJFL-|.LLF--J-FJJ.-LL-7|.F7
LF.|-F.-7JJF7.|J|F---7-L--J77JL--J.FLF.J-JF77F77LJL--J|FJJ|L-L|-F7L.7L-L77F7.F7|7|--7JJ.F-L-FF7JFF77.|.--FFJL-LFF77|..L7JLJ..LLL.F7.JL--7F-F
FF.J7LL-7.FL77F-|777LJ7||--JJF||FLF-F.L-|FL7-|-LJ-|L|L||JLJL7F----|-J|.LLJLJ7F|LFLJ.-J-F|.|JLJJF|LJF7-7.F||7|J|...FL-7-JJFF-77.L77F|F7||LL.|
|LL|-.L-J7JLJ-JJLL7--J----LJ.|L-L-L-L-LJLJ-L-|J.J.|.-JLJ77.LL|J-|-LF-LJ.L-|7LF--|JLJ-L---JJ.FLLLJ7-FJ.L.LLJ-|L|.LJ-LJJLL7.LJLJ-LF-7LJ-JJJ--.
"""


# # First example input
# input = """
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# """

# # Second exmample input
# input = """
# ..........
# .S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........
# """

# # # Third example input
# input = """
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJIF7FJ-
# L---JF-JLJIIIIFJLJJ7
# |F|F-JF---7IIIL7L|7|
# |FFJF7L7F-JF7IIL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# """

# input = """
# ..F7.
# .SJ|.
# FJ.L7
# L7F-J
# .LJ..
# """

# input = """
# ..F7..
# ..|L7.
# F-JJL7
# LS-7FJ
# ...LJ.
# """

pipes = {
    "F": {"left": "down", "up": "right"},
    "J": {"down": "left", "right": "up"},
    "L": {"left": "up", "down": "right"},
    "7": {"up": "left", "right": "down"},
    "|": {"down": "down", "up": "up"},
    "-": {"left": "left", "right": "right"},
    ".": {},
}


@dataclass
class Cell:
    row: int
    col: int

    def __hash__(self):
        return hash((self.row, self.col))


board = [x.strip() for x in input.splitlines() if x.strip() != ""]

# take first 50 rows and columns

start_cell = next(Cell(r, c) for r, row in enumerate(board)
                  for c, cell in enumerate(row) if cell == "S")


def move(cell: Cell, direction: Optional[str]) -> Optional[Cell]:
    moves = {
        #       r, c
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0)
    }
    if direction is None:
        return None
    move_row, move_col = moves[direction]
    next_cell = Cell(cell.row + move_row, cell.col + move_col)
    # Check if we are out of bounds
    if next_cell.row < 0 or next_cell.row >= len(board) or next_cell.col < 0 or next_cell.col >= len(board[0]):
        return None
    return next_cell


@dataclass
class Node:
    cell: Cell
    distance: int
    prev_direction: Optional[str] = None
    direction: str = None

# region Part 1


nodes = []
for direction in ["up", "right", "down", "left"]:
    next_cell = move(start_cell, direction)
    if next_cell:
        nodes.append(Node(next_cell, 1, direction))
seen = set([start_cell])
furthest_node = 0
while len(nodes) > 0:
    node = nodes.pop(0)
    if node.cell in seen:
        # Loop found
        furthest_node = node
        break
    char = board[node.cell.row][node.cell.col]
    direction = pipes[char].get(node.prev_direction)
    next_cell = move(node.cell, direction)
    if next_cell:
        # Important to only mark as seen if we managed to move through the pipe
        seen.add(node.cell)
        nodes.append(Node(next_cell, node.distance + 1, direction))


print("Furthest node", furthest_node)
print('Part 1 answer:', furthest_node.distance)

# endregion

# region Part 2

# 1. Find the path from S to S
# 2. Find cells connected to the wall and not part of the path
# 3. Flood fill from those outsider cells
# 4. Now find a cell on the path next to an outsider, walk along it always filling the inside

# 1. Find the path from S to S


def find_path_from_start():
    for start_direction in ["right", "down", "left", "up"]:
        node = Node(start_cell, 0, None, start_direction)
        path = [node]
        while True:
            char = board[node.cell.row][node.cell.col]
            direction = start_direction if char == "S" else pipes[char].get(
                node.prev_direction)
            path[-1].direction = direction
            next_cell = move(node.cell, direction)
            if not next_cell:
                break  # Dead end
            if next_cell == start_cell:
                return path  # Loop found
            node = Node(next_cell, node.distance + 1, direction)
            path.append(node)


path = find_path_from_start()
print("Path", len(path))
path_cells = [n.cell for n in path]


# 2. Find a cell connected to the wall and not to the path
first_outsiders = []
for r, row in enumerate(board):
    for c in range(len(row)):
        node = Cell(r, c)
        if node in path_cells:
            continue
        if c == 0 or c == len(row) - 1 or r == 0 or r == len(board) - 1:
            first_outsiders.append(node)
assert first_outsiders is not None
print("First outsiders", len(first_outsiders))

# 3. Flood fill from those outsider cells
outsiders = set(first_outsiders)
open_list = first_outsiders
while len(open_list) > 0:
    node = open_list.pop(0)
    for direction in ["left", "up", "right", "down"]:
        next_cell = move(node, direction)
        if next_cell and next_cell not in outsiders and next_cell not in path_cells:
            outsiders.add(next_cell)
            open_list.append(next_cell)

print("Outsiders", len(outsiders))

# 4. Now find a cell on the path next to an outsider, walk along it always filling the inside


@dataclass
class Node:
    cell: Cell
    prev_direction: str


print("Path", len(path))

# Find the first node where we're heading right and
# the outside is to the left of the direction of travel
first_node = None
for node in path:
    up = move(node.cell, "up")
    down = move(node.cell, "down")
    right = move(node.cell, "right")
    left = move(node.cell, "left")
    char = board[node.cell.row][node.cell.col]
    if char == "-" and (up in outsiders or up is None) and node.direction == "right":
        first_node = node
        break
    elif char == "|" and (right in outsiders or right is None) and node.direction == "down":
        first_node = node
        break
    elif char == "-" and (down in outsiders or down is None) and node.direction == "left":
        first_node = node
        break
    elif char == "|" and (left in outsiders or left is None) and node.direction == "up":
        first_node = node
        break

# We need to assume the directions are correct ie
# we must be travelling right
# if first_node.direction != "right":
#     # create a new path by reversing the directions in the path
#     node = Node(first_node.cell, 0, 'right', 'right')
#     path = [start_cell]
#     while True:
#         char = board[node.cell.row][node.cell.col]
#         direction = pipes[char].get(node.prev_direction)
#         path[-1].direction = direction
#         next_cell = move(node.cell, direction)
#         if not next_cell:
#             raise Exception("Dead end")
#         if next_cell == first_node.cell:
#             break
#     assert set(path_cells) == set([n.cell for n in path])
#     path_cells = [n.cell for n in path]


print("First node", first_node)
assert first_node is not None

# Walk along the path and fill anything unmarked

start_index = path.index(first_node)
insiders = set([n.cell for n in path])

print("Outsiders before")
# [print("".join(['X' if Cell(r, c) in outsiders else '.' for c,
#                 _ in enumerate(row)])) for r, row in enumerate(board)]

for i in range(len(path)):
    index = (start_index + i) % len(path)
    node = path[index]
    if node.cell in outsiders:
        break

    # Get all the cells around this one
    up = move(node.cell, "up")
    up_left = move(up, "left") if up else None
    up_right = move(up, "right") if up else None
    down = move(node.cell, "down")
    down_left = move(down, "left") if down else None
    down_right = move(down, "right") if down else None
    left = move(node.cell, "left")
    right = move(node.cell, "right")

    cells = set()
    if node.direction == "right":
        cells = set([up, up_right, right])
    elif node.direction == "down":
        cells = set([right, down_right, down])
    elif node.direction == "left":
        cells = set([down, down_left, left])
    elif node.direction == "up":
        cells = set([left, up_left, up])

    for neighbour in cells:
        # If it's not on the path mark it as outsider
        if neighbour and neighbour not in insiders:
            outsiders.add(neighbour)

    # print("Outsiders after node", node)
    # [print("".join(['X' if Cell(r, c) in outsiders else '.' for c,
    #        _ in enumerate(row)])) for r, row in enumerate(board)]

# Flood fill again
outsiders = set(outsiders)
open_list = list(outsiders)
while len(open_list) > 0:
    node = open_list.pop(0)
    for direction in ["up", "right", "down", "left"]:
        next_cell = move(node, direction)
        if next_cell and next_cell not in outsiders and next_cell not in path_cells:
            outsiders.add(next_cell)
            open_list.append(next_cell)


total = len(board) * len(board[0])
print("Total", total)
print("Outsiders", len(outsiders))
print("Path", len(path_cells))
assert len(path_cells) == len(path) == len(set(path_cells))
print("Part 2 answer:", total - len(outsiders) - len(path_cells))

print("Board")
[print("".join([c for c in row])) for row in board]
print("Path")
[print("".join(['X' if Cell(r, c) in path_cells else '.' for c, _ in enumerate(row)]))
 for r, row in enumerate(board)]
print("Outsiders")
[print("".join(['X' if Cell(r, c) in outsiders else '.' for c, _ in enumerate(row)]))
 for r, row in enumerate(board)]
# print("Insiders")
# [print("".join([str('X' if Cell(r, c) in insiders else '.') for c, _ in enumerate(row)]))
#  for r, row in enumerate(board)]

# print('Union insiders and outsiders')
# [print("".join([str('X' if Cell(r, c) in set(path_cells).union(outsiders) else '.') for c, _ in enumerate(row)]))
#  for r, row in enumerate(board)]


# print("Direction")
# dir_to_arrow = {'left': '<', 'right': '>', 'up': '^', 'down': 'v', '.': '.'}
# for r in range(len(board)):
#     for c in range(len(board[0])):
#         node = Cell(r, c)
#         node = next((n for n in path if n.cell == node), None)
#         if node and node.direction:
#             print(dir_to_arrow[node.direction], end='')
#         else:
#             print('.', end='')
#     print()


# endregion

# .XXXXXXXXXXXXXXXXXXX
# .XXXXXXXXXXXXXXXXXXX
# .XXXXXXXXXXXXXXXXXX.
# XXXXXXXXXXXXXX.XXXX.
# XXXXXXXXXX....XXXX..
# ...XXXXXXXX...XX....
# ..XXXXXXXXXXX..XXXXX
# ..XXXXXXXXXXXXXXXXXX
# .....XXXXXXXXXXXXXXX
# .....XXXXXXXXXXXXX..

# X...................
# X...................
# X..................X
# ...................X
# ..................XX
# XXX.............XXXX
# XX..................
# XX..................
# XXXXX...............
# XXXXX.............XX


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXX
# XXXXXXXXXXXXXXX...XXXX..XXXXXXXXX
# XXXXXXXXXXXXXX.........XXXXXXXXXX
# XXXXXXXXXXXXXX.........XXXXXXXXXX
# XXXXXXXXXXXXX........XXXXXXXXXXXX
# XXXXXXXXXXXX......XXXXXXXXXXXXXXX
# XXXXXXXXXXX......XXXXXXXXXXXXXXXX
# XXXXXXX..........XXXXXXXXXXXXXXXX
# XXXXXX...........XXXXXXXXXXXXXXXX
# XXXXXXXX..........XXXXXXXXXXXXXXX
# XXXXXXXXX.........XXXXXXXXXXXXXXX
# XXXXXXXXX.........XXXXXXXXXXXXXXX
# XXXXXXXXXX.........XXXXXXXXXXXXXX
# XXXXXXXXXX...........XXXXXXXXXXXX
# XXXXXXXXXXX.........XXXXXXXXXXXXX
# XXXXXXXXXXXXX.......XXXXXXXXXXXXX
# XXXXXXXXXXXXXX..XX...XXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXX..XXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXX..XXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
