package handler

import (
	"log"

	"github.com/RNubla/api_gateway/model"
	"github.com/gofiber/fiber/v2"
)

func VideoInfo(c *fiber.Ctx) error {
	video := new(model.Video)

	if err := c.BodyParser(&video); err != nil {
		return err
	}

	request := fiber.Post("http://localhost:8000/video/")
	request.JSON(fiber.Map{"link": video.Link})

	code, data, err := request.Bytes()
	if err != nil {
		log.Fatal(err)
	}
	if code == 404 {
		return fiber.NewError(fiber.StatusNotFound, string(data))
	}
	// fmt.Println("data", code == 404)
	return c.SendString(string(data))
}
