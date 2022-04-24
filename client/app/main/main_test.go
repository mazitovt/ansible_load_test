package main

import (
	"flag"
	"testing"
)

var host = flag.String("host", "0.0.0.0", "Name of location to greet")

func BenchmarkMain(b *testing.B) {
	url := "http://" + *host + ":8000/"
	ServerRequest(url, b.N)
}

// chmod +x ./rip
// ./rip -concurrent 100 -interval 10 http://server:8000