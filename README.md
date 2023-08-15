# SafeWalk Backend

## Overview

Step untuk repository backend <br>

### Installation

- Clone this repository (with HTTPS preferred)

  ```bash
  $ git clone https://github.com/SafetyWalk/belerion.git
  ```

** Run locally in your computer**  
<br>

- Activate virtual environment, or create one if none has been created <br>
  - Create virtual environment
    - Windows
      ```bash
      $ python -m venv env
      ```
    - Mac
      ```bash
      $ virtualenv env
      ```
  - Activate virtual environment
    - Windows
      ```bash
      $ env\Scripts\activate
      ```
    - Mac
      ```bash
      $ env/bin/activate
      ```
- Install required packages
  ```bash
  $ pip install -r requirements.txt
  ```
- Migrate if needed
  ```bash
  $ python manage.py migrate
  ```
- Run the server in your local (`localhost:8000`)
  ```bash
  $ python manage.py runserver
  ```

## Development

- Run this script for auto migrate, populate data, and runserver 
  ```bash
  sh auto.sh
  ```
- Admin, Go to `localhost:8000/admin`
- Login with
  ```
  Username: admin
  Email: eugeniusms@gmail.com
  Password: admin123
  ```

## URLs

Service | URL | Type
--- | --- | ---
Admin | `localhost:8000/admin` | Special 
Authentication | `localhost:8000/authentication/manual-user/` | GET, POST 
Authentication | `localhost:8000/authentication/google-user/` | GET, POST

## Deployment

- Create a new project in Google Cloud Platform
- Activate Google SDK in your terminal
- Create python virtual environment 'venv' that will be used for deployment, activate it, and install required requirements.txt
- Run `gcloud init` in your terminal
- Run `gcloud app deploy` in your terminal