var testInput = @"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

var games = testInput.Split(Environment.NewLine);

// 12 red cubes, 13 green cubes, and 14 blue cubes
var maxReds = 12;
var maxGreens = 13;
var maxBlues = 14;
var sum = 0;
foreach(var game in games)
{
    var parts = game.Split(':');
    
    var gameNumber = int.Parse(parts[0].Split(' ')[1]);
    var draws = parts[1].Split(';');
    var ok = true;
    foreach(var draw in draws)
    {
        var cubes = draw.Split(',');
        foreach(var cube in cubes)
        {
            var x = cube.Trim().Split(' ');
            var color = x[1];
            var count = int.Parse(x[0]);
            Console.WriteLine($"{color} {count}");
            if ((color == "red" && count > maxReds) ||
                (color == "green" && count > maxGreens) ||
                (color == "blue" && count > maxBlues))
                {
                    ok = false;
                }
        }
    }
    if (ok) {
        sum += gameNumber;
    }
    Console.WriteLine($"Game {gameNumber}");
    
}
Console.WriteLine($"Sum {sum}");
