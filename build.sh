python3 -m venv venv
if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    echo "Unsupported OS"
    exit 1
fi
if [[ ! -f .env ]] || \
   ! grep -q "^DATA_PATH=" .env || \
   ! grep -q "^USD=" .env || \
   ! grep -q "^COIN_RATE=" .env || \
   ! grep -q "^HOUR_RATE=" .env; then
cat > .env <<EOF
DATA_PATH=./Data/
USD=94.53
COIN_RATE=2.5
HOUR_RATE=20
EOF
    echo ".env created/updated"
fi
pip install --upgrade pip
pip install -r requirements.txt
echo ""
echo ""
echo "setup successful"
pyinstaller --onefile --add-data ".env:." main.py
echo ""
echo ""
echo "build successful"