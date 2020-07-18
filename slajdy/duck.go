package main
import "fmt"

type Duck interface {
	swim(x int, y int)
	quack() string
}

type Mallard struct {
	x, y int
}

func (m *Mallard) swim(x, y int) {
	m.x += x
	m.y += y
}

func (m Mallard) quack() string {
	return "Quack quaaaack"
}

func swimThenQuack(d Duck) {
	d.swim(1, 1)
	fmt.Println(d.quack())
}

func main() {
	donald := Mallard{x: 0, y: 0}
	swimThenQuack(&donald)
	fmt.Println(donald)
}
