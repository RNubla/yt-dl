package router

import (
	"github.com/RNubla/api_gateway/handler"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
)

func SetupRoutes(app *fiber.App) {
	// Middleware
	api := app.Group("/api", logger.New())
	api.Get("/", handler.Hello)
	// Video
	video := api.Group("/video")
	video.Post("/", handler.VideoInfo)
}
