check_requirements() {
command -v docker >/dev/null 2>&1 || { echo "Docker nie jest zainstalowany"; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "Docker Compose nie jest zainstalowany"; exit 1; }
}

start_application() {
echo "Uruchamianie 4Forum..."

docker-compose up -d

docker-compose ps

echo "Aplikacja została uruchomiona!"

}

main() {
check_requirements
start_application
}

main