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

Service | Description | URL | Method | Payload
--- | --- | --- | --- | ---
Admin | Admin Page | `{{url}}/admin` | - | -
Authentication | Register Manual User | `{{url}}/api/v1/authentication/manual-user/` | GET, POST | -
Authentication | Register Google User | `{{url}}/api/v1/authentication/google-user/` | GET, POST | -
Authentication | Login Manual User | `{{url}}/api/v1/authentication/manual-user/login/` | POST | -
Authentication | Login Google User | `{{url}}/api/v1/authentication/google-user/login/` | POST | -
Authentication | Edit Password Manual User | `{{url}}/api/v1/authentication/manual-user/edit/password/` | PUT | -
Profile | Get Profile Manual User | `{{url}}/api/v1/profile/manual-user/` | GET | -
Profile | Get Profile Google User | `{{url}}/api/v1/profile/google-user/` | GET | -
Profile | Edit Profile Manual User | `{{url}}/api/v1/profile/manual-user/edit/` | PUT | -
Profile | Edit Profile Google User | `{{url}}/api/v1/profile/google-user/edit/` | PUT | -
Contact | Create Contact Manual User | `{{url}}/api/v1/contact/manual-user/create/` | POST | -
Contact | Create Contact Google User | `{{url}}/api/v1/contact/google-user/create/` | POST | -
Contact | Get Contacts Manual User | `{{url}}/api/v1/contact/manual-user/` | POST | -
Contact | Get Contacts Google User | `{{url}}/api/v1/contact/google-user/` | POST | -
Contact | Edit Contact Manual User | `{{url}}/api/v1/contact/manual-user/edit/` | PUT | -
Contact | Edit Contact Google User | `{{url}}/api/v1/contact/google-user/edit/` | PUT | -
Contact | Delete Contact Manual User | `{{url}}/api/v1/contact/manual-user/delete/` | DELETE | -
Contact | Delete Contact Google User | `{{url}}/api/v1/contact/google-user/delete/` | DELETE | -

## Deployment

- Create a new project in Google Cloud Platform
- Activate Google SDK in your terminal
- Create python virtual environment 'venv' that will be used for deployment, activate it, and install required requirements.txt
- Run `gcloud init` in your terminal
- Run `gcloud app deploy` in your terminal