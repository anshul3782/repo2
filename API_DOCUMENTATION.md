# Health Data API Documentation

## Base URL
Your Render deployment URL will be: `https://your-app-name.onrender.com`

## Authentication
Currently, no authentication is required (public API).

## Endpoints

### 1. List All Health Data
- **URL:** `GET /api/health-data/`
- **Description:** Get all health data entries with pagination
- **Response:**
```json
{
  "count": 10,
  "results": [
    {
      "phone_number": "1111111111",
      "username": "user_1111",
      "steps": 1000,
      "avg_heart_rate": 65,
      "resting_calories": 1100,
      "sleep_hours": 8,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ]
}
```

### 2. Create New Health Data
- **URL:** `POST /api/health-data/`
- **Description:** Create a new health data entry
- **Request Body:**
```json
{
  "phone_number": "1234567890",
  "steps": 5000,
  "avg_heart_rate": 75,
  "resting_calories": 1200,
  "sleep_hours": 7
}
```

### 3. Get Specific User Data
- **URL:** `GET /api/health-data/{phone_number}/`
- **Description:** Get health data for a specific phone number
- **Example:** `GET /api/health-data/1111111111/`

### 4. Update User Data (Complete)
- **URL:** `PUT /api/health-data/{phone_number}/`
- **Description:** Update all fields for a user
- **Request Body:**
```json
{
  "steps": 6000,
  "avg_heart_rate": 80,
  "resting_calories": 1300,
  "sleep_hours": 8
}
```

### 5. Update User Data (Partial)
- **URL:** `PATCH /api/health-data/{phone_number}/`
- **Description:** Update specific fields for a user
- **Request Body:**
```json
{
  "steps": 7000
}
```

### 6. Delete User Data
- **URL:** `DELETE /api/health-data/{phone_number}/`
- **Description:** Delete health data for a specific user

### 7. Get Statistics
- **URL:** `GET /api/health-data/stats/`
- **Description:** Get overall statistics of all health data
- **Response:**
```json
{
  "message": "Health data statistics",
  "stats": {
    "total_users": 10,
    "avg_steps": 5000.5,
    "avg_heart_rate": 75.2,
    "avg_sleep_hours": 7.5,
    "max_steps": 10000,
    "min_steps": 1000
  }
}
```

### 8. Update Steps Only
- **URL:** `PATCH /api/health-data/{phone_number}/update_steps/`
- **Description:** Update only the steps for a specific user
- **Request Body:**
```json
{
  "steps": 8000
}
```

### 9. Update Heart Rate Only
- **URL:** `PATCH /api/health-data/{phone_number}/update_heart_rate/`
- **Description:** Update only the heart rate for a specific user
- **Request Body:**
```json
{
  "avg_heart_rate": 85
}
```

## Example Usage with curl

### Create a new entry:
```bash
curl -X POST https://your-app.onrender.com/api/health-data/ \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "9876543210",
    "steps": 343,
    "avg_heart_rate": 343,
    "resting_calories": 1500,
    "sleep_hours": 8
  }'
```

### Update steps:
```bash
curl -X PATCH https://your-app.onrender.com/api/health-data/9876543210/update_steps/ \
  -H "Content-Type: application/json" \
  -d '{"steps": 5000}'
```

### Get user data:
```bash
curl https://your-app.onrender.com/api/health-data/9876543210/
```

## Testing the API
You can test the API using:
- Browser (for GET requests)
- Postman
- curl commands
- Any HTTP client

## Error Responses
The API returns appropriate HTTP status codes:
- 200: Success
- 201: Created
- 204: No Content (for DELETE)
- 400: Bad Request (validation errors)
- 404: Not Found
- 500: Server Error
