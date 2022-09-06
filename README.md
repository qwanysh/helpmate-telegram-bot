# helpmate-telegram-bot

###### Install dependencies
```bash
pipenv install --dev
```

###### Run database
```bash
docker run -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:alpine
```

###### Run application
```bash
pipenv run hupper -m code.main
```

###### Run tests
```bash
pipenv run pytest
```
