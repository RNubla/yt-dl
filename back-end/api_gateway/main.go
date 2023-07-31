package main

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/gofiber/fiber/v2"
)

type Person struct {
	Email string
}

type VideoURL struct {
	Link string `json: "link"`
}

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World 👋!")
	})

	app.Get("/api/v1/*", func(c *fiber.Ctx) error {
		user := Person{
			Email: "hello",
		}

		u, err := json.Marshal(user)
		if err != nil {
			panic(err)
		}

		// msg := fmt.Sprintf("✋ %s", c.Params("*"))
		return c.SendString(string(u)) // => ✋ register
	}).Name("api")

	app.Post("/api/v1/info", func(c *fiber.Ctx) error {
		link := new(VideoURL)

		if err := c.BodyParser(&link); err != nil {
			return err
		}

		fmt.Println("payload: ", link.Link)

		request := fiber.Post("http://localhost:8000/video/")

		request.JSON(fiber.Map{"link": link.Link})

		_, data, err := request.Bytes()
		if err != nil {
			log.Fatal(err)
		}
		return c.SendString(string(data))
	}).Name("info")

	// app.Post("api/v1/download_info/", func(c *fiber.Ctx) error {
	// 	client := http.Client{}
	// 	link := new(VideoURL)

	// 	if err := c.BodyParser(&link); err != nil {
	// 		return err
	// 	}

	// 	// this will convert struct into json buffer
	// 	// var buf bytes.Buffer
	// 	// err := json.NewEncoder(&buf).Encode(&link)

	// 	// if err != nil {
	// 	// 	log.Fatal(err)
	// 	// }
	// 	req, err := http.NewRequest(http.MethodPost, "http://127.0.0.1:8000/video/", &link.Link)
	// 	if err != nil {
	// 		log.Fatal(err)
	// 	}
	// 	fmt.Println(req)

	// 	resp, err := client.Do(req)
	// 	if err != nil {
	// 		log.Fatal(err)
	// 	}
	// 	defer resp.Body.Close()

	// 	if resp.StatusCode != http.StatusOK {
	// 		return fiber.NewError(resp.StatusCode, "Error invoking the API")
	// 	}
	// 	fmt.Println(resp)

	// 	body, err := io.ReadAll(resp.Body)
	// 	if err != nil {
	// 		log.Fatal(err)
	// 	}
	// 	fmt.Println(body)

	// 	return c.SendString(string(body))

	// }).Name("download_info")

	app.Listen("localhost:3000")
}
