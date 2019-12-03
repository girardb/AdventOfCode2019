module Main where

import Lib
import System.IO
import Control.Monad

main = do
        contents <- readFile "../Day1Input.txt" 
        let singleWords = words contents
            masses = readInt singleWords
        print(sum (map fuel_req_1 masses))

readInt :: [String] -> [Integer] 
readInt = map read

fuel_req_1 :: Integer -> Integer
fuel_req_1 n = floor (max (n/3 - 2) 0)
