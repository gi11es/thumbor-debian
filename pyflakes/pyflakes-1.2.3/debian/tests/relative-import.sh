# LP: #1560134

cd $ADTTMP

cat > relative.py <<EOF
from . import foo

foo()
EOF

python -m pyflakes relative.py
python3 -m pyflakes relative.py