package main

import "fmt";

func fact(n int) int {
	result := 1
	for i := 1; i <=n; i++ {
		result *= i
	}
	return result
}

func main() {
	x := 10
	y := fact(5)
	fmt.Println(x)
	fmt.Println(y)
}

