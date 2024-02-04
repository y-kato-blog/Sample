package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
)

type Data struct {
	Str string `json:"str"`
}

func main() {
	var fileName string
	fmt.Scan(&fileName)
	byte, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	data := Data{string(byte)}
	bytes, err := json.Marshal(data)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(bytes))

} // main
