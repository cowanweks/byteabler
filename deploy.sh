# Deployment script
cd api
python --version ; pip --version  # For debugging
pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
pytest

