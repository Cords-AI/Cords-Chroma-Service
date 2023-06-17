# Cords Vector Database

Import records, store their vectors in [Chroma](https://www.trychroma.com/), retrieve nearest neighbours.

Uses OpenAPI [text-embedding-ada-002](https://openai.com/blog/new-and-improved-embedding-model) if an OpenAI API key is provided. If not, falls back to [universal-sentence-encoder-multilingual](https://tfhub.dev/google/universal-sentence-encoder-multilingual/3).

## Environment Variables

*Set these in your .env file. See the .env.j2 template for reference.*

| Variable               | Notes                                        |
| ---------------------- | -------------------------------------------- |
| OPENAI_API_KEY         | https://platform.openai.com/account/api-keys |
| DATA_DIR               | Persistent storage directory                 |

## Usage

**Start the server**

```shell
docker compose up -d
```

**Add a record**

```shell
docker compose exec app curl -X POST http://localhost -H 'Content-Type: application/json' -d '{"id": "123", "partner": "211", "document": "hello world"}'
```

**Run a query**

```shell
docker compose exec app curl -X POST http://localhost/search?q=learn+to+code -H 'Content-Type: application/json' -d '{"ids": "'\''262e7a66-8dc5-40c7-8920-e026ee538bf6'\'','\''a5b99de9-1288-4915-be5f-1bfcf74834dc'\''"}'
```

Include an optional list of ids in the post body to limit the results.

