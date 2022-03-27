package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"sync"
)

func ServerRequest(url string, max int) {
	wg := &sync.WaitGroup{}

	for i := 0; i <= max; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			resp, err := http.Get(url)
			if err != nil {
				fmt.Println(err)
			} else {
				resp.Body.Close()
			}
		}()
	}

	wg.Wait()
}

func main() {

	args := os.Args

	if len(args) != 2 {
		log.Fatal("program takes exactly one argument")
	}

	url := "http://" + args[1] + ":8000/"

	ServerRequest(url, 10)
}
