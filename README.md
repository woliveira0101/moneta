<img height="170em" src="http://i.imgur.com/eVj2DWl.png">

money management, simplified.

### Running moneta
- Install dependencies:
  - Python 2
  - MySQL
  - `pip install -r requirements.txt`
- Configure APIs
  - Set Plaid API keys in `settings.py`
- Migrate database
  - `python manage.py migrate`
- Run moneta
  - `python manage.py runserver`
