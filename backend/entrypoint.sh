echo "Verificando o banco de dados..."

echo "Aplicando as migrações no banco de dados..."
python manage.py migrate

echo "Iniciando o servidor Python..."

exec "$@"

