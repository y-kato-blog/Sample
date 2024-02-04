package main

import (
	"bytes"
	"encoding/json"
	"fmt"
)

func main() {
	var input string
	fmt.Scan(&input)

	var buf bytes.Buffer
	err := json.Indent(&buf, []byte(input), "", "  ")
	if err != nil {
		panic(err)
	}
	fmt.Println(buf.String())

} // main
