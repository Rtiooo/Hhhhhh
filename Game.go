package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

func main() {
    router := gin.Default()

    router.GET("/", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{
            "message": "Welcome to the Game Website!",
        })
    })

    // Add more routes and handlers here

    router.Run(":8080") // Listen and serve on localhost:8080
}

