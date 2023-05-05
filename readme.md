# Cords Vector Database

Import records from the [Cords Data Service](https://github.com/Cords-Connect/Data-Service), get and store their vectors in [Chroma](https://www.trychroma.com/), retrieve nearest neighbours.

Uses OpenAPI [text-embedding-ada-002](https://openai.com/blog/new-and-improved-embedding-model) if an OpenAI API key is provided. If not, falls back to [universal-sentence-encoder-multilingual](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3).

## Environment Variables

*Set these in your .env file. See the .env.j2 template for reference.*

| Variable             | Notes                                                                            |
|----------------------|----------------------------------------------------------------------------------|
| DATA_SERVICE_URL     | [Cords Data Service](https://github.com/Cords-Connect/Data-Service) instance url |
| DATA_SERVICE_API_KEY | API key for your Data Service instance                                           |
| OPENAI_API_KEY       | https://platform.openai.com/account/api-keys                                     |

## Usage

Import from data service

```shell
docker compose run -w /app/src app python3 import.py
```

Start the server

```shell
docker compose up -d
```

Run a query

```shell
docker compose exec app curl http://localhost?q=learn+to+code
```
