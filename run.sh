#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"
if [ -d ".env" ];
then
    echo "Enabling virtual env"
    . .env/bin/activate

else
    echo "No Virtual env."
    echo "Creating the virtual env"
    python3 -m venv .env
    . .env/bin/activate
    if [ -f "requirements.txt" ];
    then
        echo "Installing all the python libraries"
        pip install -r requirements.txt
    else
        echo "No requirements.txt present in $(pwd)"
    fi
fi

# Activate virtual env
export FLASK_APP=startup.py:app
export FLASK_ENV=development
flask run 
deactivate