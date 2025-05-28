help:
	@echo "Command List:"
	@echo ""
	@echo "dvwa:         run dvwa app"
	@echo "dvwa-down:    stop dvwa app"
	@echo "sqlitei:      run sqlite-injection app"
	@echo "sqlitei-down: stop sqlite-injection app"

# for linux, use:
# sed -i '/      - DB_SERVER=db/ a\ \n      - DEFAULT_SECURITY_LEVEL=low' DVWA/compose.yml;

dvwa:
	@if [ ! -d "DVWA" ]; then \
		git clone https://github.com/digininja/DVWA.git; \
		sed -i '' '/      - DB_SERVER=db/ a\ '$$'\n''      - DEFAULT_SECURITY_LEVEL=low'$$'\n' DVWA/compose.yml; \
	fi
	@docker compose -f DVWA/compose.yml up -d
	@echo "DVWA app is running at http://localhost:4280"
	@echo "username: admin, password: password"

dvwa-down:
	@docker compose -f DVWA/compose.yml down

sqlitei:
	@docker run --rm --name sqlitei -p 8000:80 -d gitlab.cylab.be:8081/cylab/play/sqlite-injection
	@echo "SQLite Injection app is running at http://localhost:8000"

sqlitei-down:
	@docker stop sqlitei

.PHONY: help dvwa dvwa-down sqlitei sqlitei-down
