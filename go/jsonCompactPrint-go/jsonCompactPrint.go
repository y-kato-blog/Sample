package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	var fileName string
	fmt.Scan(&fileName)
	byte, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	var buf bytes.Buffer
	err2 := json.Compact(&buf, byte)
	if err2 != nil {
		panic(err2)
	}
	fmt.Println(buf.String())

} // main
