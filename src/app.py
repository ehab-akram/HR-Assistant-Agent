from flask import Flask, render_template, request, jsonify
import requests
import time
import uuid

app = Flask(__name__)

# Your RAG API endpoint
RAG_API_URL = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/generate_session", methods=["POST"])
def generate_session():
    """Generate a new session ID for the chat"""
    session_id = str(uuid.uuid4()).replace("-", "")
    return jsonify({
        "sessionId": session_id,
        "success": True
    })


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.json
    user_message = data.get("message", "")
    session_id = data.get("sessionId", "")

    if not session_id or len(session_id) < 10:
        return jsonify({
            "reply": "⚠️ Session ID غير صالح. يرجى إعادة تحديث الصفحة.",
            "error": True
        })

    if not user_message.strip():
        return jsonify({
            "reply": "⚠️ يرجى كتابة رسالة صالحة.",
            "error": True
        })

    payload = {
        "sessionId": session_id,
        "action": "sendMessage",
        "chatInput": user_message
    }

    try:
        # Add a small delay to simulate processing time for better UX
        time.sleep(0.5)

        response = requests.post(RAG_API_URL, json=payload, timeout=140)
        response.raise_for_status()

        response_data = response.json()
        bot_reply = response_data.get("output", "عذراً، لم أستطع معالجة طلبك في الوقت الحالي.")

        return jsonify({
            "reply": bot_reply,
            "error": False,
            "timestamp": int(time.time())
        })

    except requests.exceptions.Timeout:
        return jsonify({
            "reply": "⏰ انتهت مهلة الانتظار. يرجى المحاولة مرة أخرى.",
            "error": True
        })
    except requests.exceptions.ConnectionError:
        return jsonify({
            "reply": "🔌 خطأ في الاتصال بالخادم. يرجى التحقق من الاتصال بالإنترنت.",
            "error": True
        })
    except Exception as e:
        return jsonify({
            "reply": f"⚠️ حدث خطأ غير متوقع. يرجى المحاولة مرة أخرى لاحقاً.",
            "error": True
        })


@app.errorhandler(404)
def not_found(error):
    return render_template("home.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "reply": "⚠️ خطأ داخلي في الخادم. يرجى المحاولة لاحقاً.",
        "error": True
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)