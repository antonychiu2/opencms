package main

import (
    "errors"
    "fmt"
    "io"
    "net/http"
    "os"
)

func getRoot(w http.ResponseWriter, r *http.Request) {
    w.Header().Add("Content-Type", "text/html")
    w.WriteHeader(http.StatusOK)

    username := r.URL.Query().Get("username")
    fmt.Printf("got / request\n")
    io.WriteString(w, fmt.Sprintf("Hello, %s!\n", username))
}

func main() {
    http.HandleFunc("/", getRoot)

    err := http.ListenAndServe(":3333", nil)

    if errors.Is(err, http.ErrServerClosed) {
        fmt.Printf("server closed\n")
    } else if err != nil {
        fmt.Printf("error starting server: %s\n", err)
        os.Exit(1)
    }
}
