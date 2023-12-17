install | i:
	@echo "installing dependencies..."
	@pip install -r requirements.txt
run:
	@echo "running the program..."
	@python3 main.py