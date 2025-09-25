from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)

SAP_BASE_URL = "http://slnxsaps4h19.marc.fr.ssg:50001/sap/opu/odata/sap/UI_MAINTWORKREQUESTOVW_V2"
SAP_USER = "piaggarwal"
SAP_PASS = "Sopra@123"

@app.route('/api/create-notification', methods=['POST'])
def create_notification():
    data = request.json

    # First, fetch CSRF Token
    csrf_headers = {
        "X-CSRF-Token": "Fetch",
        "Accept": "application/json"
    }

    csrf_response = requests.get(
        f"{SAP_BASE_URL}/C_MaintWorkRequestOverviewTP",
        auth=(SAP_USER, SAP_PASS),
        headers=csrf_headers
    )

    if csrf_response.status_code != 200:
        return jsonify({"status": "error", "message": "Failed to fetch CSRF token", "code": csrf_response.status_code}), 500

    csrf_token = csrf_response.headers.get("X-CSRF-Token")
    cookies = csrf_response.cookies

    # Now prepare the POST
    post_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-CSRF-Token": csrf_token
    }

    payload = {
        "NotificationType": data.get("NotificationType"),
        "NotificationText": data.get("NotificationText"),
        "MaintPriorityType": data.get("MaintPriorityType"),
        "MaintPriority": data.get("MaintPriority"),
        "ReportedByUser": data.get("ReportedByUser"),
        "MaintenancePlanningPlant": data.get("MaintenancePlanningPlant"),
        "MaintenancePlannerGroup": data.get("MaintenancePlannerGroup")
    }

    response = requests.post(
        f"{SAP_BASE_URL}/C_MaintWorkRequestOverviewTP",
        data=json.dumps(payload),
        auth=(SAP_USER, SAP_PASS),
        headers=post_headers,
        cookies=cookies  # Required for session handling
    )

    if response.status_code in (200, 201):
        return jsonify({"status": "success", "sap_response": response.json()}), 201
    else:
        return jsonify({
            "status": "error",
            "code": response.status_code,
            "message": response.text
        }), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
