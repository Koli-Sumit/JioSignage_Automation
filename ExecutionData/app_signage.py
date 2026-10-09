import sys

from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import os
import configparser
import subprocess
from flask import Flask, Response, abort
import os

app = Flask(__name__, template_folder='templates')

print(f"Templates folder: {os.path.join(os.getcwd(), 'templates')}")

app.secret_key = os.urandom(24)

CONFIG_PATH = os.path.join(os.getcwd(), '../ConfigurationData', 'testData.ini')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUN_SCRIPT = os.path.join(BASE_DIR, "reportGeneration+API.py")
BATCH_FILE_DETAILED = os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_DetailedTest.bat')
BATCH_FILE_SMOKE = os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SmokeTest.bat')
BATCH_FILE_MODULEWISE = {
    "Dashboard": os.path.join(os.getcwd(), 'BatchFiles', 'Dashboard.bat'),
    "Displays": os.path.join(os.getcwd(), 'BatchFiles', 'Displays.bat'),
    "DisplayStatus": os.path.join(os.getcwd(), 'BatchFiles', 'DisplayStatus.bat'),
    "EmergencyAlerts": os.path.join(os.getcwd(), 'BatchFiles', 'EmergencyAlerts.bat'),
    "Layout": os.path.join(os.getcwd(), 'BatchFiles', 'Layout.bat'),
    "LayoutApproval": os.path.join(os.getcwd(), 'BatchFiles', 'LayoutApproval.bat'),
    "LoginAndProfile": os.path.join(os.getcwd(), 'BatchFiles', 'LoginAndProfile.bat'),
    "Media": os.path.join(os.getcwd(), 'BatchFiles', 'Media.bat'),
    "Playlists": os.path.join(os.getcwd(), 'BatchFiles', 'Playlists.bat'),
    "Schedules": os.path.join(os.getcwd(), 'BatchFiles', 'Schedules.bat'),
    "UserAccess": os.path.join(os.getcwd(), 'BatchFiles', 'UserAccess.bat'),
}

BATCH_FILE_SMOKE_WITH_VALIDATION_MODE = {
    "client_only": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SmokeTest_onlyClient.bat'),
    "portal_only": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SmokeTest_onlyWebPortal.bat'),
    "portal_client": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SmokeTest_webPortal +Client.bat'),
}

BATCH_FILE_SANITY_WITH_VALIDATION_MODE = {
    "client_only": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SanityTest_onlyClient.bat'),
    "portal_only": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SanityTest_onlyWebPortal.bat'),
    "portal_client": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_SanityTest_webPortal +Client.bat'),
}

BATCH_FILE_DETAILED_WITH_VALIDATION_MODE = {
    "client_only": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_DetailedTest_onlyClient.bat'),
    "portal_only": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_DetailedTest_onlyWebPortal.bat'),
    "portal_client": os.path.join(os.getcwd(), 'BatchFiles', 'JioSignage_DetailedTest_webPortal +Client.bat'),
}

ALLURE_REPORT_BAT = os.path.join(os.getcwd(), 'BatchFiles', 'reportGeneration_signage.bat')

DOWNLOAD_REPORT_BAT = os.path.join(os.getcwd(), 'BatchFiles', 'reportDownload_signage.bat')

API_BAT = os.path.join(os.getcwd(), 'BatchFiles', 'apiCall.bat')

@app.route('/')
def index():
    return render_template('index_signage.html')

@app.route('/check_adb')
def check_adb():
    try:
        result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        lines = result.stdout.strip().split('\n')[1:]
        devices = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 2:
                devices.append({'id': parts[0], 'status': parts[1]})
        if not devices:
            return jsonify({'status': 'no_device'})

        device = devices[0]
        if device['status'] == 'device':
            return jsonify({'status': 'online'})
        elif device['status'] == 'offline':
            return jsonify({'status': 'offline'})
        else:
            return jsonify({'status': 'unknown', 'raw_status': device['status']})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)})


@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"status": "missing_ip"})

    try:
        result = subprocess.check_output(["adb", "connect", ip], stderr=subprocess.STDOUT, text=True)
        if "connected to" in result or "already connected to" in result:
            return jsonify({"status": "reachable", "message": result.strip()})
        else:
            return jsonify({"status": "unreachable", "message": result.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "unreachable", "error": e.output.strip()})

@app.route('/disconnect')
def disconnect():
    try:
        result = subprocess.check_output(["adb", "disconnect"], stderr=subprocess.STDOUT, text=True)
        return jsonify({"status": "disconnected", "message": result.strip()})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "error": e.output.strip()})


@app.route('/submit', methods=['POST'])
def submit():
    environment = request.form.get('environment')
    UserName = request.form.get('UserName')
    Password = request.form.get('Password')
    releaseCycle = request.form.get('rs')
    test_type = request.form.get('testType')
    if test_type in ['smoke', 'sanity', 'detailed']:
        validation_type = str(request.form.get('validation_type', 'none'))
    else:
        validation_type = 'none'
    module = request.form.get('module') if test_type == 'modulewise' else 'none'
    config = configparser.ConfigParser()
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    config.read(CONFIG_PATH)
    if not config.has_section('TestData'):
        config.add_section('TestData')
    config.set('TestData', 'Environment', environment)
    config.set('TestData', 'UserName', UserName)
    config.set('TestData', 'Password', Password)
    config.set('TestData', 'release_cycle', releaseCycle)
    config.set('TestData', 'Test_type', test_type)
    config.set('TestData', 'validation_type', validation_type)
    config.set('TestData', 'Module', module)
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)

    try:
        if test_type == 'detailed' and validation_type in BATCH_FILE_DETAILED_WITH_VALIDATION_MODE:
            subprocess.run(f'start "" /wait cmd /c "{BATCH_FILE_DETAILED_WITH_VALIDATION_MODE[validation_type]}"',
                           shell=True)
            subprocess.run(API_BAT, shell=True)
            flash("Detailed test execution completed successfully!, and the report has been generated!", "success")

        elif test_type == 'sanity' and validation_type in BATCH_FILE_SANITY_WITH_VALIDATION_MODE:
            subprocess.run(f'start "" /wait cmd /c "{BATCH_FILE_SANITY_WITH_VALIDATION_MODE[validation_type]}"',
                           shell=True)
            subprocess.run(API_BAT, shell=True)
            flash("Sanity test execution completed successfully!, and the report has been generated!", "success")

        elif test_type == 'smoke' and validation_type in BATCH_FILE_SMOKE_WITH_VALIDATION_MODE:
            subprocess.run(f'start "" /wait cmd /c "{BATCH_FILE_SMOKE_WITH_VALIDATION_MODE[validation_type]}"',
                           shell=True)
            subprocess.run(API_BAT, shell=True)
            flash("Smoke test execution completed successfully!, and the report has been generated!", "success")

        elif test_type == 'modulewise' and module in BATCH_FILE_MODULEWISE:
            subprocess.run(f'start "" /wait cmd /c "{BATCH_FILE_MODULEWISE[module]}"', shell=True)
            subprocess.run(API_BAT, shell=True)
            flash(f"Modulewise test execution for '{module}' completed successfully!, and the report has been generated!", "success")

        else:
            flash("Invalid module selected for modulewise test.", "error")
            return redirect(url_for('result'))

        return redirect(url_for('result'))

    except subprocess.CalledProcessError as e:
        flash(f"An error occurred while executing the batch file: {e.stderr}", "error")
        return redirect(url_for('result'))

    except FileNotFoundError as e:
        flash(f"File not found: {e.filename}. Please check if the file path is correct.", "error")
        return redirect(url_for('result'))

    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")
        return redirect(url_for('result'))


from flask import send_file, abort

from flask import send_file, render_template_string
import os

@app.route('/latest_report_view', methods=['POST'])
def latest_report_view():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    report_path = os.path.join(base_dir, 'AutomationResult', 'latest_report', 'index.html')

    if os.path.exists(report_path):
        return send_file(report_path)
    else:
        return render_template_string("""
        <html>
        <head>
            <title>404 - Report Not Found</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f3f4f6; text-align: center; padding: 50px; }
                h1 { font-size: 60px; color: #ef4444; margin-bottom: 10px; }
                p { font-size: 20px; color: #374151; }
                .box { display: inline-block; padding: 40px; border-radius: 15px; background: #fff; box-shadow: 0 5px 20px rgba(0,0,0,0.1); }
                .btn { display: inline-block; margin-top: 20px; padding: 10px 20px; background: #3b82f6; color: #fff; text-decoration: none; border-radius: 8px; transition: 0.3s; }
                .btn:hover { background: #2563eb; }
            </style>
        </head>
        <body>
        <br>
        <br>
        <br>
        <br>
        <br>
            <div class="box">
                <h1>🚫 404</h1>
                <p>Allure report not found.<br><br>Please reach out to the VIT Automation Team..</p>
                
            </div>
        </body>
        </html>
        """), 404






@app.route('/download_allure_report', methods=['POST'])
def download_allure_report():
    """Route to trigger the Allure report generation process."""
    try:
        result = subprocess.run([DOWNLOAD_REPORT_BAT], check=True, capture_output=True, text=True)
        flash("CSV report successfully downloaded! Go to the 'Result_Detail' folder to view it.", "success")
    except subprocess.CalledProcessError as e:
        flash(f"An error occurred while downloading the Allure report: {e.stderr}", "error")
    except FileNotFoundError as e:
        flash(f"File not found: {e.filename}. Please check if the file path is correct.", "error")
    except Exception as e:
        flash(f"An unexpected error occurred: {str(e)}", "error")

    return redirect(url_for('result'))


@app.route('/result')
def result():
    try:
        subprocess.Popen(['adb', 'disconnect'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error running adb disconnect: {e}")
    return render_template('result_signage.html')


if __name__ == '__main__':
    app.run(debug=True, port=6004)
