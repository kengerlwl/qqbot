docker build -t qqbot:v1 .
docker run --rm  -d --name="qqbot" --network host qqbot:v1