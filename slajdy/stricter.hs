import Data.String.Utils (join)

list2Str :: [[Char]] -> [Char]
list2Str xs = if xs then "No elements" else (join "," xs) -- Error

main = do
	putStrLn $ list2Str []
	putStrLn 10 -- Error
