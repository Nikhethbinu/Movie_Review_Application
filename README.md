# Movie_Review_Management

A Django REST Framework (DRF) backend application for managing movies and user reviews. Users can add movies to the catalog and submit reviews for existing movies.

---

## Project Overview

- **Project Name:** `Movie_Review_Management`
- **App Name:** `movies`
- **Framework:** Django & Django REST Framework

---

## Database Models & Relationships

### Models

| Model | Description |
| :--- | :--- |
| **`User`** | Represents registered users who can create movie entries and post reviews. |
| **`MovieDb`** | Stores movie details added by users. |
| **`ReviewDb`** | Stores user reviews and ratings linked to specific movies. |

### Entity Relationships

1. **`User` - `MovieDb` (One-to-Many)**
   - One user can add multiple movies.
   - Each movie belongs to a single user.
2. **`User` - `ReviewDb` (One-to-Many)**
   - One user can write multiple reviews.
   - Each review belongs to a single user.
3. **`MovieDb` - `ReviewDb` (One-to-Many)**
   - Each movie can receive multiple reviews.
   - Each review is associated with one specific movie.

---
