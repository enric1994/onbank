run:
	@docker-compose up -d --build onbank_container
dev:
	@docker exec -it onbank_container bash
build:
	@docker-compose build onbank_container
down:
	@docker-compose down -v
status:
	@docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
logs:
	@docker logs onbank_container -f