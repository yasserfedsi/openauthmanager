# OpenAuthManager (OPM)

**Author:** Yasser Fedsi
<br />
**Version:** Alpha Pretest
<br />
**License:** MIT
<br />
**Repository:** [GitHub - OpenAuthManager](https://github.com/yasserfedsi/openauthmanager)

---

## Overview

OpenAuthManager (OPM) is a lightweight, framework-free Python-based authentication system designed for simplicity, security, and educational value. It securely manages user registration, authentication, and profile updates using hashed passwords and JSON-based storage. Ideal for small-scale applications or educational projects.

---

## Features

### ✓ Secure Password Hashing

Uses **bcrypt** to hash passwords securely:

$H(p) = bcrypt(salt,\ p)$

Where:

* $p$: Plaintext password
* $salt$: Random salt value for added entropy

### ✓ Email Validation

Restricts registration to authorized domains:

$\text{Valid Email}(e) = \exists d \in D \text{ such that } e \text{ ends with } d$

* $e$: Email
* $D$: Allowed domains (e.g., `@gmail.com`)

### ✓ User Authentication

Authentication succeeds if:

$\text{Auth}(e, p) = \text{Valid Email}(e) \land (H(p)_{stored} = H(p)_{input})$

### ✓ JSON-Based Storage

All user data is stored as a list of dictionaries in `users.json`, e.g.:

```json
[
  {
    "email": "user@gmail.com",
    "password": "hashed_password",
    "personalInformation": {
      "Full name": "John Doe",
      "Phone number": "1234567890",
      "City": "New York"
    }
  }
]
```

### ✓ Full CRUD Support

* Add, search, modify, delete users
* Modify email and password after authentication
* Add personal information securely

### ✓ Access Control

* Authenticated users can view/edit full profile
* Unauthenticated users can only see emails

---

## How It Works

### Initialization

```python
users = load_users()
```

If `users.json` does not exist, a new file is initialized with default content.

### Registration Flow

1. Validate Email:
   $\text{Valid Email}(e) = \exists d \in D \text{ such that } e \text{ ends with } d$
2. Hash Password:
   $H(p) = bcrypt(salt,\ p)$
3. Store User:

```python
{ "email": e, "password": H(p) }
```

### Authentication Flow

1. Match email from existing users
2. Compare hashed password input with stored hash

### Modification & Deletion

* Update email/password after verification
* Remove users based on email search

### Personal Info Addition

```json
"personalInformation": {
  "Full name": "Jane Smith",
  "Phone number": "0987654321",
  "City": "Algiers"
}
```

---

## Security Principles

### 1. **bcrypt Hashing**

Each password is hashed with a unique salt:
$H(p) = bcrypt(\text{random salt}, p)$

### 2. **No Plaintext Storage**

Passwords are never stored in plaintext.

### 3. **Minimum Password Requirements**

$\text{Length}(p) \geq 5 \quad \land \quad p_{input} = p_{confirm}$

### 4. **Domain Restriction**

Only emails ending with allowed domains are accepted.

---

## System Requirements

### Software

* **Python:** ≥ 3.13
* **Libraries:** `bcrypt`, `json`

```bash
pip install bcrypt
```

### Hardware

* Any modern CPU
* 8GB RAM recommended
* Minimal disk space (1GB+)

### OS Compatibility

* Windows 7, 8, 10, 11
* MacOS
* Linux distributions

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yasserfedsi/openauthmanager
cd openauthmanager
```

### 2. Run the Program

```bash
python main.py
```

---

## Usage Menu

```text
1. Add User
2. Search User
3. Modify User
4. Delete User
5. Display Users
6. Switch to Authentication System
7. Exit
```

### Auth System Menu

```text
1. Authenticate User
2. Modify User Password
3. Modify User Email
4. Add Personal Info
5. Display Users (Authenticated)
6. Logout
```

---

## Future Enhancements

* Database backend support (e.g., SQLite, MongoDB)
* Role-based access control (Admin/User)
* Multi-factor authentication (OTP/email)
* RESTful API integration
* Advanced UI (CLI/GUI)

---

## Contact

**Author:** Yasser Fedsi
<br />
**Email:** [fedsi.yasser@gmail.com](mailto:fedsi.yasser@gmail.com)
<br />
**GitHub:** [https://github.com/yasserfedsi/openauthmanager](https://github.com/yasserfedsi/openauthmanager)
