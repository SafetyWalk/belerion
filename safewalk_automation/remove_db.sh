# Description: remove db.sqlite3 and all migrations files except __init__.py
rm -rf db.sqlite3;
find . -path "*/authentication/migrations/*.py" -not -name "__init__.py" -delete;
find . -path "*/contact/migrations/*.py" -not -name "__init__.py" -delete;
find . -path "*/maps/migrations/*.py" -not -name "__init__.py" -delete;