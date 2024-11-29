# **Crowd-Level-Prediction-Flask-Back-End-API**

## **Project Summary**  
This Flask-based back-end API is designed to predict crowd levels on public transport routes. By analyzing factors such as time of day, day of the week, and specific routes, the system provides users with a crowd-level prediction to enhance their commuting experience.

---

## **Sample `POST` Request**  
The API accepts a JSON payload to predict the crowd level. Below is a sample request format:

```json
{
    "Time": 18,
    "Day": 0,
    "Route_100": 1,
    "Route_101": 0,
    "Route_154": 0,
    "Route_163": 0,
    "Route_176": 0
}
