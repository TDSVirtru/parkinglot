
PL_VIRTUAL_ENVIRONMENT=".venv"

echo "****************************************"
if [ -d $PL_VIRTUAL_ENVIRONMENT ]; then
  echo "*** Parking Log Virtual Environment Exists"
else
  echo "*** Creating Parking Lot Virtual Environment"
  python3 -m venv $PL_VIRTUAL_ENVIRONMENT
fi

echo "*** Upgrading PIP"
pip install --upgrade pip

echo "*** Installing needed packages"
pip install -U pytest-watch
pip install -U flake8

echo "*** Setup complete"
echo "****************************************"

source $PL_VIRTUAL_ENVIRONMENT/bin/activate
