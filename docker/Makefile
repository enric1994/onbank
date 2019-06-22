run:
	@docker-compose up -d --build onbank_container
face:
	@docker-compose up -d --build face
dev:
	@docker exec -it onbank_container bash
devface:
	@docker exec -it face bash
build:
	@docker-compose build onbank_container
down:
	@docker-compose down -v
status:
	@docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
logs:
	@docker logs onbank_container -f