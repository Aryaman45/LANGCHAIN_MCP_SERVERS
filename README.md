# LangChain MCP Servers

A powerful, multi-server application that integrates LangChain with multiple servers to solve math problems, perform searches, and fetch weather data. This project uses FastAPI and LangChain for seamless communication and AI-powered functionality. The backend can dynamically connect to different servers for varied purposes, making it flexible and easy to extend.

## Project Overview

LangChain MCP Servers is a multi-functional server setup that allows interaction with different services such as:

- **Math Solver**: Solve math problems programmatically.
- **Search Server**: Perform search queries and get AI-generated answers.
- **Weather Server**: Fetch weather details based on user location.

The application uses LangChain for leveraging OpenAI's GPT models, and it allows dynamic connections to different servers, making it highly customizable.

### Key Features:
- Dynamic connection to multiple servers (e.g., search, math, weather).
- Support for user-defined prompts.
- Integration with OpenAI's GPT-4 model for generating responses.
- Utilizes server-sent events (SSE) for real-time communication with backend services.

## Technologies Used
- **FastAPI**: For creating the server endpoints and managing the services.
- **LangChain**: For seamless integration with OpenAI's GPT model.
- **SSE (Server-Sent Events)**: For real-time communication between the client and server.
- **OpenAI GPT-4**: Used for generating responses based on the user's prompts.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.8 or later
- Git
- A virtual environment manager (e.g., `venv`, `conda`)

### Environment Variables

This project requires an OpenAI API key. Set it up in your environment by creating a `.env` file with the following content:

