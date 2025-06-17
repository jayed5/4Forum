echo "Sprawdzanie stanu systemu 4Forum..."

Sprawdź status usług
systemctl status nginx
systemctl status redis
systemctl status postgresql
systemctl status 4forum
df -h /opt/4forum
tail -n 50 /opt/4forum/logs/error.log
netstat -tulpn | grep -E ':(80|443|5432)'
EOL
chmod +x /opt/4forum/scripts/diagnostic.sh